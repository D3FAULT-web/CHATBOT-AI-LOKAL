FROM python:3.11-slim

# Install tools
RUN pip install gradio requests

# Copy file app
COPY app.py /app.py

CMD ["python", "/app.py"]
