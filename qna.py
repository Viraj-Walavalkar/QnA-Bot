import streamlit as st
from groq import Groq
import os
# Initialize the Groq client
client = Groq(api_key="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")

def save_qa_to_file(chapter, verse, qa_text):
    # Create a folder named 'QnA' if it doesn't exist
    folder_path = 'QnA'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Generate file name
    file_name = f'QNA_{chapter}_{verse}.txt'
    file_path = os.path.join(folder_path, file_name)
    
    # Save Q&A text to file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(qa_text)


# Define the system prompt
system_prompt = """ Based on the input provided by the user, generate a series of insightful and well-structured questions that cover different aspects of the topic.
Ensure that each question is designed to provoke thoughtful responses and explore the topic in depth.
After generating the questions, provide comprehensive answers to each, offering detailed explanations, examples, and additional context where necessary.
The goal is to enrich the user's understanding and encourage further exploration of the subject.
"""

# Streamlit UI
st.title("QnA Generator using LLAMA-3")

# Generate button


input_text = st.text_input("Text")

if input_text:
                with st.spinner("Generating..."):
                    # Generate chat completion
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "system",
                                "content": f"{system_prompt}"
                            },
                            {
                                "role": "user",
                                "content": f"{input_text}",
                            }
                        ],
                        model="llama3-70b-8192",
                        temperature=0.1
                    )
                    output = chat_completion.choices[0].message.content

                    # Display output
                    st.markdown(output)

