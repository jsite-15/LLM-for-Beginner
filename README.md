# LLM-for-Beginner

A beginner-friendly repository for learning how to work with Large Language Models (LLMs) using **LangChain**, **Mistral AI**, and **Hugging Face**.

This repository documents my journey while learning Generative AI and contains examples ranging from basic chatbot interactions to local models and embeddings.

---

## Topics Covered

- API Keys with `.env`
- LangChain Basics
- Mistral AI Models
- Hugging Face Endpoints
- Local LLMs
- Embedding Models
- Chat History and Memory
- System Prompts
- Prompting with `invoke()`
- Dependency Management with `uv`

---

## Files

### `chatbot.py`
A basic chatbot with memory using LangChain.

**Concepts covered**
- HumanMessage
- AIMessage
- Conversation history
- `invoke()`

---

### `mistral_model.py`
Using Mistral AI models with LangChain.

**Concepts covered**
- API keys
- ChatMistralAI
- Temperature
- Max tokens

---

### `huggingface_endpoint.py`
Using Hugging Face models through API endpoints.

**Concepts covered**
- HuggingFaceEndpoint
- Hugging Face tokens
- Hosted models
- API-based inference

---

### `local_tinyllama.py`
Running TinyLlama locally.

**Concepts covered**
- Local LLMs
- Transformers
- PyTorch
- Local inference

---

### `huggingface_embedding.py`
Using embedding models with Hugging Face.

**Concepts covered**
- Embeddings
- Vector representations
- Semantic similarity

---

## Personality Chatbot with UI

Built using **Streamlit** and **Mistral AI**.

### Features

- Angry Mode 😡
- Funny Mode 😂
- Sad Mode 😢
- Conversation history
- Chat interface
- Multiple personalities

---

## Local Models vs API Models

| Local Models | API Models |
|---------------|------------|
| Run on your machine | Run on provider servers |
| Require RAM and storage | Require internet |
| Need model downloads | No downloads |
| Slower | Faster |
| Free after download | May have rate limits |

---

## Installation

Create a virtual environment

```bash
uv venv
```

Install dependencies

```bash
uv pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file

```env
MISTRAL_API_KEY=
HF_TOKEN=
GOOGLE_API_KEY=
GROQ_API_KEY=
```

---

## Running Files

### Mistral Model

```bash
python mistral_model.py
```

### Basic Chatbot

```bash
python chatbot.py
```

### Hugging Face Endpoint

```bash
python huggingface_endpoint.py
```

### Local TinyLlama

```bash
python local_tinyllama.py
```

### Streamlit Chatbot

```bash
streamlit run uichatbot.py
```

---

## Common Errors I Faced

### No module named `dotenv`
Cause:
- Package not installed in the current environment.

---

### API key not found
Cause:
- Wrong environment variable name.
- `.env` file not loaded.

---

### No module named `transformers`
Cause:
- Transformers package missing.

---

### PyTorch not found
Cause:
- Local models require PyTorch.

---

### Hugging Face token not detected
Cause:
- Using old variable names instead of `HF_TOKEN`.

---

### Local model downloading large files
Cause:
- Running the model locally instead of using APIs.

---

## Tech Stack

- Python
- LangChain
- Mistral AI
- Hugging Face
- Transformers
- PyTorch
- Streamlit
- python-dotenv
- uv

---

## Future Topics

- Prompt Templates
- Chains
- Text Splitters
- Vector Databases
- FAISS
- ChromaDB
- RAG
- Memory
- Agents
- LangGraph

---

## Goal

This repository is intended for beginners who are starting their journey in Generative AI and want simple examples to understand how LLMs work in practice.

⭐ Feel free to explore, learn, and build upon these examples!
