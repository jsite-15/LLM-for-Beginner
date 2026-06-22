# Beginner Guide to LLMs with LangChain

A beginner-friendly guide to using Large Language Models with LangChain.

## Topics Covered

### 1. Using API Keys with .env
- Why API keys are needed
- Using python-dotenv
- Protecting secrets

### 2. LangChain Basics
- What LangChain is
- Chat models
- invoke()

### 3. Mistral Models
- Connecting to Mistral AI
- Generating responses

### 4. Hugging Face Models
- HuggingFaceEndpoint
- API-based models
- Local models

### 5. DeepSeek Models
- DeepSeek-R1
- Distilled models
- API usage

### 6. Local vs API Models

| Local Models | API Models |
|---------------|------------|
| Run on your machine | Run on provider servers |
| Need RAM and storage | Need internet |
| Slower | Faster |
| Free after download | May have usage limits |

### 7. Prompting with invoke()

```python
response = model.invoke("Write a poem on AI")
print(response.content)
```

### 8. Dependency Management with uv

Create environment:

```bash
uv venv
```

Install packages:

```bash
uv pip install -r requirements.txt
```

Run:

```bash
uv run chatmodels/chat.py
```

## Common Errors I Faced

### No module named dotenv
Cause: Wrong environment.

### API key not found
Cause: Wrong variable name.

### transformers not found
Cause: Missing dependency.

### PyTorch not found
Cause: Local Hugging Face models require torch.

### HF token not detected
Cause: Using old environment variable name.

### Local model downloading huge files
Cause: Models are being run locally instead of through APIs.

## Future Topics
- Memory
- Prompt Templates
- Chains
- RAG
- Embeddings
- Vector Databases
- Agents
- LangGraph
