# Pio

Pio is a simple personal AI chatbot.

## Run it

1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Install dependencies:

   pip install -r requirements.txt

4. Set your OpenAI API key.

macOS/Linux:
   export OPENAI_API_KEY="your-key"

Windows PowerShell:
   $env:OPENAI_API_KEY="your-key"

5. Start Pio:

   python app.py

6. Open http://127.0.0.1:5000 in your browser.

You can change the model with OPENAI_MODEL if your account has access to another model.

Never put an API key directly into index.html or expose it in client-side JavaScript.
