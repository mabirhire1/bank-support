# Bank Support AI Agent

A simple AI-powered customer complaint handler for a bank using OpenRouter and large language models.

This system analyzes customer complaints, extracts intent and key information, determines the category, and generates a polite, professional response.

---

## Features

- Multi-step reasoning using LLM (Intent → Category → Details → Response)
- Powered by OpenRouter (supports GPT-4o, Claude, Gemini, etc.)
- Clean modular design with separate reasoning steps
- Command-line interface
- Environment-based configuration

---

---

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd bank-support

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate    # On Linux/Mac
   # .venv\Scripts\activate    # On Windows

3. **Install Deendencies**
   ```bash
   pip install -r requirements.txt

## Setup
Create a .env file in the root directory:
```bash
   OPENROUTER_API_KEY=sk-or-v1-your-actual-key-here
   MODEL_NAME=openai/gpt-4o-mini

Get your API key from: https://openrouter.ai/keys
```
## Usage
Run the script with a customer complaint:
```Bash
   python main.py
```
## Requirements
Create requirements.txt:
```txt
requests
python-dotenv
```

## How It Works
The system processes each complaint through 5 logical steps:

- Intent Detection – Identifies the core purpose of the complaint
- Category Suggestion – Suggests relevant complaint categories
- Category Assignment – Chooses the best matching category
- Information Extraction – Pulls out key details (e.g., amount, date, transaction ID, etc.)
- Response Generation – Creates a friendly, professional reply

## License
MIT License