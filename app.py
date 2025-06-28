import requests
import gradio as gr

OLLAMA_URL = "http://ollama:11434"
MODEL_NAME = "llama3"

# Fungsi utama chatbot
def chat(prompt, history):
    res = requests.post(f"{OLLAMA_URL}/api/generate", json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })

    reply = res.json()["response"]
    history.append((prompt, reply))
    return history, history

# Desain UI Chatbot
with gr.Blocks(theme=gr.themes.Soft()) as iface:
    gr.Markdown(
        """
        # 🤖 Chatbot AI Lokal  
        Dibuat dengan ❤️ di Docker + Ollama  
        Model: `llama3`  
        """
    )

    chatbot = gr.Chatbot(height=400, label="Percakapan")
    msg = gr.Textbox(placeholder="Ketik pertanyaanmu di sini...", label="Masukkan Prompt")
    clear = gr.Button("🔁 Bersihkan Chat")

    state = gr.State([])

    msg.submit(chat, [msg, state], [chatbot, state])
    clear.click(lambda: ([], []), None, [chatbot, state])

iface.launch(server_name="0.0.0.0", server_port=7860)
