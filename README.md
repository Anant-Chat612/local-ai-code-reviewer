# Local AI-Powered Python Code Reviewer

A private, offline Python code review and debugging tool built for macOS, utilizing Streamlit and local Ollama (Llama 3). 

## Features
* **Local Syntax Check:** Instantly validates Python syntax using Python's built-in `ast` module.
* **Line-Numbered Code Reference:** Displays code with explicit line numbers to easily spot errors.
* **AI Code Quality Review:** Powered locally by Llama 3 via Ollama to evaluate code quality, identify logic bugs, and provide actionable fix suggestions.
* **100% Private:** Runs entirely on your machine—no internet connection or cloud API keys required.

## Tech Stack
* **Python**
* **Streamlit** (for the web interface)
* **Ollama & Llama 3** (for local AI code analysis)

## How to Run It Locally

1. Make sure Ollama is installed and running on your machine:
   
   ollama serve
   
2. Ensure you have the Llama 3 model pulled:
   
   ollama pull llama3

3. Install the required dependencies:

   pip install streamlit

4. Run the Streamlit app:

   streamlit run app.py
