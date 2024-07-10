from groq import Groq


def add_to_history(user_input, model_response):
    conversation_history.append({"user": user_input, "response": model_response})


def format_conversation_history():
    formatted_history = ""
    for entry in conversation_history:
        formatted_history += f"User: {entry['user']}\nBot: {entry['response']}\n"
    return formatted_history


MAX_TOKENS = 2048


def get_limited_context():
    context = format_conversation_history()
    tokens = context.split()
    if len(tokens) > MAX_TOKENS:
        context = " ".join(tokens[-MAX_TOKENS:])
    return context


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
    return model_response


# Define the Replicate API endpoint and your API token
client = Groq(
    api_key="your_groq_api_key_here",
)


conversation_history = []

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    model_response = generate_response(user_input)
    print(f"Bot: {model_response}")
