# CHATBOT-AI-LOKAL
Menjalankan AI lokal pribadi (Chatbot / LLM)
Chatbot AI lokal berbasis GUI (Web) yang berjalan di atas Docker Desktop dengan menggunakan Ollama sebagai otak AI-nya, dan Gradio sebagai tampilan web interaktif-nya.

🎯 Tujuan:
Menjalankan chatbot AI lokal (mirip ChatGPT)

GUI (via browser lokal)

Semua berjalan di Docker Desktop

Tanpa internet, tanpa biaya API

🔧 Komponen:
Komponen	Fungsi
ollama/ollama	Menjalankan model LLM (seperti llama3)
gradio + Python	UI Web Chatbot
Dockerfile + docker-compose	Untuk menjalankan semua secara otomatis

✅ LANGKAH-LANGKAH

🟢 1. Buat Folder Proyek
Buat folder bernama chatbot-ollama-gui, lalu isi dengan:

chatbot-ollama-gui/
│
├── Dockerfile
├── app.py
└── docker-compose.yml

📄 2. Isi File Dockerfile
Dockerfile

🧠 3. Isi File app.py
Ini adalah script Gradio yang akan panggil model dari Ollama:

⚙️ 4. Isi File docker-compose.yml

▶️ 5. Jalankan dengan Docker Compose
Buka terminal di folder chatbot-ollama-gui, lalu ketik:

🌐 6. Akses Chatbot
Setelah semua berjalan, buka browser kamu:

http://localhost:7860
Kamu bisa mulai chatting dengan AI secara lokal!


