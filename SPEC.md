# Lifetime Financial Consulting AI - Specification Memo

## Overview
This service provides an AI-powered financial consulting agent. Users can discuss their financial health, check if they can afford major purchases, and understand life insurance options. The AI leverages dedicated backend tools to perform exact mathematical calculations and comparisons.

## Tech Stack
- **Frontend**: Next.js (TypeScript, Tailwind CSS)
- **Backend**: Python (FastAPI, SQLAlchemy, LangChain/LangGraph)
- **Database**: PostgreSQL (for users, profiles, chat history)
- **Deployment**: Docker Compose
- **State Management**: Zustand
- **Internationalization (i18n)**: react-i18next (English & 繁體中文)

## Core Features
1. **AI Provider Registry**:
   - A dropdown registry in the UI allows users to select which AI model to use.
   - Supported providers: OpenAI, Anthropic (Claude), Google (Gemini), OpenRouter, Local LLaMA.
   - Using LiteLLM/LangChain for abstractions.

2. **AI Tools (Skills)**:
   - **Affordability Check**: A calculator function that compares item cost, down payment, loan term, income, and expenses to determine if a user can safely afford an item.
   - **Life Insurance Policy Check**: Compares Term vs Whole Life Insurance estimates based on the user's age and desired coverage amount.
   - **Life Stage Check**: Extracts demographic info (age, marital status, dependents, income) from conversation to build a user profile.

3. **Authentication**:
   - JWT-based authentication via FastAPI to allow users to register and login.
   - Persists chat history for the user session.

4. **Language Support**:
   - UI fully supports English and Traditional Chinese (繁體中文).
   - System prompts dynamically instruct the AI Agent to reply in the user's currently selected language.

## Design Patterns
- **Provider Registry**: A Python singleton registry storing factory methods to spawn LangChain Chat Models.
- **Agentic Architecture**: Uses LangChain's Structured Chat Agent with function calling (Tools) to execute calculations instead of hallucinating math.
