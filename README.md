# Lifetime Financial Consulting AI

Welcome to the Lifetime Financial Consulting AI service! This project is a comprehensive full-stack application designed to help users understand their financial health, check affordability for major purchases, and compare life insurance options using artificial intelligence.

## 🎯 Project Purpose

This AI acts as a personal, lifetime financial consultant. Rather than simply generating text, the AI uses an **Agentic framework** with access to dedicated, deterministic backend tools to ensure mathematical accuracy when performing calculations and comparisons.

**Core Capabilities:**
1. **Affordability Check:** Calculates whether a user can safely afford a specific item (like a house or car) based on their income, expenses, and loan terms.
2. **Life Insurance Comparison:** Compares Term Life Insurance vs. Whole Life Insurance estimates based on the user's age and desired coverage.
3. **Life Stage Check:** Intelligently extracts demographic information (age, marital status, dependents, income) from natural conversation to build a long-term user profile.
4. **Multilingual Support:** Fully supports English and Traditional Chinese (繁體中文).
5. **AI Provider Registry:** Allows users to easily switch between OpenAI, Claude (Anthropic), Gemini (Google), OpenRouter, and local LLaMA models.

## 🏗️ Architecture

- **Frontend:** Next.js (TypeScript, Tailwind CSS, Zustand, react-i18next)
- **Backend:** Python (FastAPI, SQLAlchemy, LangChain Agents)
- **Database:** PostgreSQL
- **Deployment:** Docker Compose

For a detailed technical specification, please refer to [SPEC.md](SPEC.md).

---

## 🚀 How to Start the Service

The easiest way to run the entire stack (Frontend, Backend, and Database) is using Docker Compose.

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.

### Step 1: Set up Environment Variables
Before starting the service, you need to provide your API keys for the AI models you wish to use. You can set these directly in your shell or create an `.env` file in the root directory (the `docker-compose.yml` will pick them up if exported).

For example, export your keys:
```bash
export OPENAI_API_KEY="your-openai-key-here"
export ANTHROPIC_API_KEY="your-anthropic-key-here"
export GEMINI_API_KEY="your-gemini-key-here"
export OPENROUTER_API_KEY="your-openrouter-key-here"
# Optional: If you have a local LLaMA instance running via Ollama
export LLAMA_API_BASE="http://host.docker.internal:11434/v1"
```

### Step 2: Build and Run with Docker Compose
Run the following command in the root directory of the project:

```bash
docker-compose up -d --build
```
*(If you are using newer Docker versions, the command might be `docker compose up -d --build`)*

This command will:
1. Spin up a **PostgreSQL** database on port `5432`.
2. Build and start the **FastAPI Backend** on `http://localhost:8000`.
3. Build and start the **Next.js Frontend** on `http://localhost:3000`.

### Step 3: Access the Application
- Open your browser and navigate to: [http://localhost:3000](http://localhost:3000)
- You can create a new account via the "Sign Up" page and then log in to start chatting with the AI.
- The backend API documentation (Swagger UI) is available at: [http://localhost:8000/docs](http://localhost:8000/docs)

### Stopping the Service
To stop the containers, run:
```bash
docker-compose down
```
