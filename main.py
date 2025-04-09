
import tkinter as tk
from tkinter import scrolledtext
import cohere
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate


COHERE_API_KEY = "YOUR_COHERE_API_KEY"  # Replace with your Cohere API key
co = cohere.Client(COHERE_API_KEY)

with open("knowledge_base.json", "r") as file:
    knowledge_base = json.load(file)

# Function to embed knowledge base using Cohere
def embed_knowledge_base(knowledge_base):
    texts = [item["content"] for item in knowledge_base]
    response = co.embed(texts=texts, model="embed-english-v2.0")
    return np.array(response.embeddings)

knowledge_embeddings = embed_knowledge_base(knowledge_base)

# Function to retrieve relevant information using Cohere embeddings
def retrieve_relevant_context(query, top_n=1):
    query_embedding = np.array(co.embed(texts=[query], model="embed-english-v2.0").embeddings)
    similarities = cosine_similarity(query_embedding, knowledge_embeddings)[0]
    top_indices = similarities.argsort()[-top_n:][::-1]
    relevant_contexts = [knowledge_base[i]["content"] for i in top_indices]
    return " ".join(relevant_contexts)

# Initialize memory
memory = ConversationBufferMemory()

# RESPONSE WITH RAG
def get_response_with_rag(prompt):
    try:
        # Retrieve previous conversation context from memory
        conversation_context = memory.load_memory_variables({}).get("history", "")
        relevant_context = retrieve_relevant_context(prompt)
        
        augmented_prompt = (
            f"Context: {relevant_context}\n\n"
            f"Conversation History:\n{conversation_context}\n\n"
            f"User Query: {prompt}\n\n"
            "Provide a detailed and complete answer."
        )
        
        # Generate a response using Cohere
        response = co.generate(
            model='command-xlarge-nightly',
            prompt=augmented_prompt,
            max_tokens=300,
            temperature=0.7,
        )
        ai_response = response.generations[0].text.strip()
        
        memory.save_context({"input": prompt}, {"output": ai_response})
        
        if not ai_response.endswith('.'):
            ai_response += '.'
        
        return f"{ai_response}\n\nThat's it. Do you have any other questions?"
    except Exception as e:
        return f"Error: {str(e)}"

def handle_user_input():
    user_input = user_entry.get()
    if not user_input.strip():
        return
    
    chat_history.insert(tk.END, f"You: {user_input}\n")
    user_entry.delete(0, tk.END)
    
    ai_response = get_response_with_rag(user_input)
    chat_history.insert(tk.END, f"AI: {ai_response}\n\n")
    chat_history.see(tk.END)

# GUI SETUP
root = tk.Tk()
root.title("RAG-Enhanced Chatbot with Memory")
root.geometry("500x500")

chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='normal', width=60, height=20, bg="#f1f1f1")
chat_history.pack(pady=10)
chat_history.insert(tk.END, "AI: Hello! How can I assist you today?\n\n")

user_entry = tk.Entry(root, width=60)
user_entry.pack(pady=10)

send_button = tk.Button(root, text="Send", command=handle_user_input, bg="#4CAF50", fg="white")
send_button.pack(pady=5)

root.mainloop()
