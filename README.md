# MG ZS Car Manual Chatbot – FastAPI Application

This is a production-ready REST API built with FastAPI to provide intelligent answers about **MG ZS vehicle warning messages**. It uses **Retrieval-Augmented Generation (RAG)** with **LangChain**, **OpenAI GPT-4o**, and **Chroma vectorstore** to extract answers from an HTML-based car manual.

## Features

- ⚙️ Retrieval-Augmented Generation (RAG) pipeline
- 🚀 FastAPI backend with `/ask` endpoint for questions
- 📄 Knowledge base loaded from a real HTML manual
- 🔐 API key securely handled via `.env`
- 📦 Ready for deployment, extension, and frontend integration

## Project Structure

```
mgzs_rag_chatbot/
│
├── app/
│   ├── main.py                 # FastAPI app entry point
│   ├── rag_pipeline.py         # RAG logic: loading, chunking, retrieval
│   └── data/
│       └── mg-zs-warning-messages.html  # Source car manual
│
├── .env                       # OpenAI API key (not committed)
├── requirements.txt           # Python dependencies
├── .gitignore                 # Ignored files and folders
├── README.md                  # This documentation
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mgzs-rag-chatbot.git
cd mgzs-rag-chatbot
```

### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your OpenAI API key

Create a `.env` file at the root of the project:

```
OPENAI_API_KEY=your-api-key-here
```

### 4. Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

Go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the API.

## API Usage

### POST `/ask`

Send a JSON body like this:

```json
{
  "question": "What does the Gasoline Particular Filter Full warning mean?"
}
```

### Sample Response

```json
{
  "answer": "The Gasoline Particulate Filter Full warning means that the filter is saturated with soot. Driving at high speed for some time may help regenerate the filter. If the warning persists, contact a service center."
}
```

## Technologies Used

- **FastAPI** – REST API framework
- **LangChain** – RAG orchestration
- **OpenAI GPT-4o** – LLM backend
- **Chroma** – Vectorstore for semantic search
- **Unstructured** – HTML document loader
- **Dotenv** – For API key management


## Author

Mohamed Oussama Bouriga
