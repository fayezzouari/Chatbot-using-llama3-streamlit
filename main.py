import streamlit as st
from groq import Groq

# Initialize the conversation history in Streamlit's session state otherwise the LLM wont be able to memorize previous responses
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []


def add_to_history(user_input, model_response):
    st.session_state.conversation_history.append(
        {"user": user_input, "response": model_response}
    )


def format_conversation_history():
    formatted_history = ""
    for entry in st.session_state.conversation_history:
        formatted_history += f"User: {entry['user']}\nBot: {entry['response']}\n"
    return formatted_history


MAX_TOKENS = 2048


def get_limited_context():
    context = format_conversation_history()
    tokens = context.split()
    if len(tokens) > MAX_TOKENS:
        context = " ".join(tokens[-MAX_TOKENS:])
    return context


# Generate responses based on the conversation's history
def generate_response(user_input):
    global MAX_TOKENS, conversation_history
    context = get_limited_context()
    prompt = f"{context}User: {user_input}\nBot:"
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )
    model_response = chat_completion.choices[0].message.content
    add_to_history(user_input, model_response)
    print(conversation_history)
    return model_response


client = Groq(
    api_key="your_groq_api_key_here",
)


# Streamlit UI
st.title("Chatbot using LLMs with Replicate")
conversation_history = []

prompt = st.text_area("Enter your prompt here:")

if st.button("Generate"):
    if prompt:
        st.write("Generating text...")

        st.write(generate_response(prompt))

    else:
        st.write("Please enter a prompt.")
