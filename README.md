# AI TUTOR

## Description
AI TUTOR application is an application designed to facilitate interactive learning for users. It allows learners to upload a documents. Once files are uploaded, users can engage with the content through an AI-driven interface. The primary goal of the app is to enable users to ask questions about the files they have submitted. The app uses machine learning models to analyze the uploaded files. It then provides users with detailed and contextually relevant information in response to their queries. The user-friendly interface ensures that learners can easily navigate through the process of uploading files and asking questions.

## Project Setup
### Dependencies
- Download python from https://www.python.org/downloads/
- Download and install streamlit locally using this command:
    ```sh
    $ pip install streamlit
    $ streamlit hello  #run this to ensure streamlit is installed
    ```
    Streamlit is an open-source framework for creating interactive web applications directly from Python code.
    
- Download and install Langchain using this command:
    ```sh
    $ pip install langchain
    ```
- Setting Up Local Models: Download the models you want to implement. [Here](https://huggingface.co/mys/ggml_llava-v1.5-7b/tree/main) is the llava model I used for image chat (ggml-model-q5_k.gguf and mmproj-model-f16.gguf). And the [mistral model](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF) from TheBloke (mistral-7b-instruct-v0.1.Q5_K_M.gguf). 


### Installation Steps
cloning the github respository to your desired code editor:
  
   - Copy the Repository URL:
    Go to the GitHub page of the repository you want to clone. Click on the “Code” button and copy the URL from the HTTPS section.

      ![image](https://github.com/TimothyMuigai/ICS-3-project/assets/143069621/9ba82a0c-9bba-44c4-8b05-2396c81a278c)

   - Open a Terminal or Command Prompt:
    On your computer, open the terminal (macOS/Linux) or Command Prompt (Windows).
    
  - Run the Clone Command:
    Use the git clone command followed by the URL you copied. For example:
     ```sh
       git clone https://github.com/username/repository.git
      ```
   - Navigate to the Cloned Repository:
    After cloning, you can navigate to the repository folder with:
        ```sh
              cd repository 
        ```
        Replace repository with the name of the cloned repository.

   - Then [create a virtual environment](https://python.land/virtual-environments/virtualenv#google_vignette) after opening the code editor to your cloned folder:
        ```sh
          python -m venv .env  
        ```
   - Activate the virtual environment:
        ```sh
          .env/Scripts/Activate.ps1   
        ```
   - copy the following command to the termianl to install the all the requirements: 

        ```sh
        pip freeze > requirements.txt
        ```
### Usage Instructions:
- How to Run: 
        To launch the app make sure you have activated the virtual environment then type the following command:
    ```sh
        streamlit run app.py
    ```
    It will autmaically start the server but if not hover then press '** ctrl+click** ' on the '**Network URL:**' to start the server i.e. :
     ```sh
    .env/Scripts/Activate.ps1: streamlit run app.py 
    
    You can now view your Streamlit app in your browser.
      Local URL: http://localhost:8501
      Network URL: http://192.168.142.119:8501
  ```
- Examples: 
        If applicable, provide examples of how to use different features or functionalities of your project.

- Input/Output: 
        Explain the expected input format and the type of output the project generates.
  
### Project Structure
```
        AI TUTOR
        │   .env
        │   app.py
        │   config.yaml
        │   database_operations.py
        │   html_templates.py
        │   llm_chains.py
        │   pdf_handler.py
        │   prompt_templates.py
        │   utils.py
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
        └───models
            │   mistral-7b-instruct-v0.1.Q4_K_M.gguf
            │   mistral-7b-instruct-v0.1.Q5_K_M.gguf
            │
            └───llava
                    ggml-model-q4_k.gguf
                    mmproj-model-f16.gguf
```
### Overview: 

#### Key Files: 
- app.py
    This is the main application file that typically serves as the entry point for your application. It handles the initiation of models, the orchestration of various components, and the main execution flow.

- pdf_handler.py 
    This module processes PDF files. It includes functions for extracting text, parsing content, or any other operations related to PDF files.

- database_operations.py
    This module manages interactions with the database. It includes functions for querying, updating, and managing data.

#### Additional Sections:

##### Project Status: 
Project is still in progress.
##### Known Issues: 
List any known bugs or limitations of the project.
##### Acknowledgements: 
#Give credit to any external resources, tutorials, or libraries you used.
