# AI TUTOR

## Description
AI TUTOR is an AI-powered application designed to assist learners by utilizing models for image handling, audio handling, and PDF handling. This tool operates entirely on the user's computer, eliminating the need for paid APIs and ensuring accessibility for everyone.

###Project Structure
AI TUTOR    
  ├───__pycache__
  ├───aitutorenv
  │
  ├───chat_icons
  │       bot_image.png
  │       user_image.png
  │
  ├───chat_sessions
  │       chat_sessions.db
  │
  ├───chroma_db
  │   │   chroma.sqlite3
  │
  ├───models
  │   │   mistral-7b-instruct-v0.1.Q4_K_M.gguf
  │   │   mistral-7b-instruct-v0.1.Q5_K_M.gguf
  │   │
  │   └───llava
  │           ggml-model-q4_k.gguf
  │           mmproj-model-f16.gguf
  │
  └───__pycache__
          audio_handler.cpython-312.pyc
          database_operations.cpython-312.pyc
          html_templates.cpython-312.pyc
          image_handler.cpython-312.pyc
          llm_chains.cpython-312.pyc
          pdf_handler.cpython-312.pyc
          prompt_templates.cpython-312.pyc
          utils.cpython-312.pyc
