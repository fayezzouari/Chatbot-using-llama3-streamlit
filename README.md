# Streamlit Chatbot with Groq API for LLAMA-3

This project demonstrates how to build a conversational chatbot using Streamlit and the Groq API for LLAMA-3. The chatbot maintains conversation history to handle full conversations coherently.

## Table of Contents

- [Streamlit Chatbot with Groq API for LLAMA-3](#streamlit-chatbot-with-groq-api-for-llama-3)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
    - [app.py](#apppy)
  - [Contributing](#contributing)

## Introduction

This project utilizes Streamlit to create a web-based interface for a chatbot powered by the LLAMA-3 model via the Groq API. The chatbot can handle continuous conversations by keeping track of the conversation history, ensuring that responses are contextually relevant.

## Features

- Web-based interface using Streamlit.
- Conversational memory to maintain context across exchanges.
- Integration with Groq API to use the LLAMA-3 model for generating responses.

## Requirements

- Python 3.7 or higher
- Streamlit
- Groq API key

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/streamlit-chatbot.git
    cd streamlit-chatbot
    ```

2. Install the required Python packages:

    ```bash
    pip install streamlit groq
    ```

3. Set up your Groq API key:

    Replace `"your_groq_api_token"` in the script with your actual Groq API key.

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Enter your prompt in the text area and click "Generate" to interact with the chatbot.

### app.py

This script contains the main logic for the Streamlit app, including:

- Initialization of conversation history.
- Functions to handle adding to history, formatting history, limiting context size, and generating responses using the Groq API.
- Streamlit UI components for user interaction and displaying conversation history.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes or improvements.
