import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

# Load API key from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# Load and preprocess the document
loader = UnstructuredHTMLLoader(file_path="app/data/mg-zs-warning-messages.html")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(documents)

# Embed and store in Chroma
embedding_model = OpenAIEmbeddings(openai_api_key=openai_api_key)
vectorstore = Chroma.from_documents(documents=chunks, embedding=embedding_model)
retriever = vectorstore.as_retriever()

# Define prompt template
prompt = ChatPromptTemplate.from_template(
    "You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. "
    "If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.\n"
    "Question: {question} \nContext: {context} \nAnswer:"
)

# Load the model
model = ChatOpenAI(
    openai_api_key=openai_api_key,
    model_name="gpt-4o-mini",
    temperature=0
)

# Compose the RAG chain
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
)

# Function to query the model
def answer_question(question: str) -> str:
    return rag_chain.invoke(question).content