# 🤖 RAG-Enhanced AI Chatbot with Memory (Tkinter GUI + Cohere)

Welcome to the **AI Chatbot with Retrieval-Augmented Generation (RAG)** and conversational memory! This project integrates:

- **Tkinter** for GUI 🖥️  
- **Cohere's LLM** for response generation 🧠  
- **Cohere Embeddings** for context-aware knowledge retrieval 📚  
- **Langchain Memory** to maintain conversation history 🗂️  

It answers health and fitness-related questions based on a custom knowledge base.

---

## 📦 Features

- ✅ **Conversational Memory**: Remembers previous questions and responses.
- ✅ **Retrieval-Augmented Generation (RAG)**: Dynamically fetches the most relevant context.
- ✅ **Cohere Embeddings + Generation**: Embeds text and generates human-like responses.
- ✅ **Simple GUI with Tkinter**: Easy-to-use chat interface.
- ✅ **Custom Knowledge Base**: Fitness and health facts stored in a JSON file.

---

## 🧠 Example Questions to Ask

You can ask the chatbot things like:

- 💪 *What are the benefits of strength training?*  
- 💧 *Why is hydration important before and after workouts?*  
- 🍎 *What does a balanced diet include?*  
- 😴 *Why is sleep important for recovery?*  
- 🧘 *How does yoga help mental health?*  
- 🏃 *What is HIIT and why is it effective?*  
- 🧘‍♂️ *What are the benefits of meditation on mental well-being?*  
- 🥦 *Why should we eat more fiber-rich foods?*  

---

## ⚙️ Technologies Used

| Symbol | Technology                          | Description                                      |
|--------|-------------------------------------|--------------------------------------------------|
| 🧠     | [Cohere](https://cohere.com/)        | Embedding and generating human-like responses    |
| 🖼️     | Tkinter (Python GUI)                | GUI library for creating the chat interface      |
| 🧮     | NumPy                               | Numerical computing and array operations         |
| 📊     | scikit-learn                        | Cosine similarity for comparing embeddings       |
| 🧩     | Langchain                           | Managing conversation history (memory buffer)    |


---

## 🚀 How to Run
```bash
1. **Install dependencies**  
pip install cohere numpy scikit-learn langchain

2. **Add your Cohere API Key**
COHERE_API_KEY = "YOUR_API_KEY_HERE"

3. **Run the script**
python chatbot.py
