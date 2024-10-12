import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = st.secrets["OPEN_API_KEY"]

# Function to generate text with continuous stream
def generate_text(prompt):
    # Initialize an empty string for the response
    response_text = ""

    # Start the chat message display (initial placeholder for the bot message)
    chat_message = st.chat_message("assistant").markdown("Thinking...")

    # Get the response from the OpenAI API with stream=True for continuous streaming
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a well-read journalist aware of India's recent performance in the 2024 Paralympics."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,  # Adjust token limit based on your need
        stream=True
    )

    # Update the response message chunk by chunk to simulate streaming
    for chunk in response:
        # Extract the latest part of the response content
        chunk_content = chunk['choices'][0]['delta'].get('content', '')
        
        # Append the latest part to the response_text
        response_text += chunk_content

        # Update the chat message displayed to the user with the new content
        chat_message.update(response_text)

    # Return the final response text (optional, since we're streaming directly)
    return response_text

# Streamlit UI setup
st.title("My first chatbot")
st.write("Ask me anything")

# User input
user_input = st.text_input("You:", placeholder="Type your question here...")

# If there's a user input, get the response from the chatbot
if user_input:
    # Display user's input as a chat message
    st.chat_message("user").markdown(user_input)
    
    # Generate and display the bot's response with continuous streaming
    generate_text(user_input)
