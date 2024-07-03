# AI TUTOR

## Description
AI TUTOR is an AI-powered application designed to assist learners by utilizing models for image handling, audio handling, and PDF handling. This tool operates entirely on the user's computer, eliminating the need for paid APIs and ensuring accessibility for everyone.

### Project Structure

## Components

- **`__pycache__`**: Contains compiled Python files (.pyc) for the project.
- **`aitutorenv`**: Main environment directory for the AI Tutor project.
  - **`chat_icons`**: Contains image files for the chat interface.
  - **`chat_sessions`**: Database file for storing chat sessions.
  - **`chroma_db`**: Database file for Chroma.
  - **`models`**: Directory for model files.
    - **`mistral-7b-instruct-v0.1`**: Contains GGUF model files.
    - **`llava`**: Contains additional model files for LLAVA.
- **`app.py`**: Main application file to run the AI Tutor.
- **`audio_handler.py`**: Handles audio processing tasks.
- **`config.yaml`**: Configuration file for project settings.
- **`database_operations.py`**: Manages database interactions.
- **`html_templates.py`**: Contains HTML templates for the UI.
- **`image_handler.py`**: Manages image processing tasks.
- **`llm_chains.py`**: Handles LLM (Language Model) chain functionalities.
- **`pdf_handler.py`**: Manages PDF processing tasks.
- **`prompt_templates.py`**: Contains templates for AI prompts.
- **`utils.py`**: Utility functions used throughout the project.
