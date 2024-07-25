import os
import pyaudio
import vosk
import json
from langdetect import detect
import openai
import tkinter as tk
from tkinter import Label
import socket
import threading

# Set up OpenAI API key
openai.api_key = 'sk-proj-2mQBIZvnOALIyBmvWVO1T3BlbkFJlnNHv44VowF9Pj9c6TEv'

# Base path to vosk models
base_model_path = 'C:\\Jikanshin\\vosk_models'

# Load Vosk models for different languages using absolute paths
models = {
    'ar': vosk.Model(os.path.join(base_model_path, "vosk-model-ar-mgb2-0.4")),
    'br': vosk.Model(os.path.join(base_model_path, "vosk-model-br-0.8")),
    'cn': vosk.Model(os.path.join(base_model_path, "vosk-model-small-cn-0.22")),
    'cs': vosk.Model(os.path.join(base_model_path, "vosk-model-small-cs-0.4-rhasspy")),
    'de': vosk.Model(os.path.join(base_model_path, "vosk-model-small-de-0.15")),
    'en': vosk.Model(os.path.join(base_model_path, "vosk-model-small-en-us-0.15")),
    'en-us-zamia': vosk.Model(os.path.join(base_model_path, "vosk-model-small-en-us-zamia-0.5")),
    'eo': vosk.Model(os.path.join(base_model_path, "vosk-model-small-eo-0.42")),
    'es': vosk.Model(os.path.join(base_model_path, "vosk-model-small-es-0.42")),
    'fa': vosk.Model(os.path.join(base_model_path, "vosk-model-small-fa-0.4")),
    'fr': vosk.Model(os.path.join(base_model_path, "vosk-model-small-fr-0.22")),
    'gu': vosk.Model(os.path.join(base_model_path, "vosk-model-small-gu-0.42")),
    'hi': vosk.Model(os.path.join(base_model_path, "vosk-model-small-hi-0.22")),
    'it': vosk.Model(os.path.join(base_model_path, "vosk-model-small-it-0.22")),
    'ja': vosk.Model(os.path.join(base_model_path, "vosk-model-small-ja-0.22")),
    'ko': vosk.Model(os.path.join(base_model_path, "vosk-model-small-ko-0.22")),
    'kz': vosk.Model(os.path.join(base_model_path, "vosk-model-small-kz-0.15")),
    'nl': vosk.Model(os.path.join(base_model_path, "vosk-model-small-nl-0.22")),
    'pl': vosk.Model(os.path.join(base_model_path, "vosk-model-small-pl-0.22")),
    'pt': vosk.Model(os.path.join(base_model_path, "vosk-model-small-pt-0.3")),
    'ru': vosk.Model(os.path.join(base_model_path, "vosk-model-small-ru-0.22")),
    'sv': vosk.Model(os.path.join(base_model_path, "vosk-model-small-sv-rhasspy-0.15")),
    'tg': vosk.Model(os.path.join(base_model_path, "vosk-model-small-tg-0.22")),
    'tr': vosk.Model(os.path.join(base_model_path, "vosk-model-small-tr-0.3")),
    'uk': vosk.Model(os.path.join(base_model_path, "vosk-model-small-uk-v3-small")),
    'uz': vosk.Model(os.path.join(base_model_path, "vosk-model-small-uz-0.22")),
    'vn': vosk.Model(os.path.join(base_model_path, "vosk-model-small-vn-0.4")),
    'tl': vosk.Model(os.path.join(base_model_path, "vosk-model-tl-ph-generic-0.6")),
    # Add more models as needed
}

# Enhanced mapping with dialect handling and fallback
lang_code_map = {
    'ar': 'ar',
    'pt-br': 'br',
    'zh-cn': 'cn',
    'zh': 'cn',  # Fallback for generic Chinese to Simplified Chinese
    'cs': 'cs',
    'de': 'de',
    'en-us': 'en-us-zamia',  # Handling dialects
    'en-gb': 'en',  # Example fallback for British English to generic English
    'en': 'en',  # Default English model
    'eo': 'eo',
    'es': 'es',
    'fa': 'fa',
    'fr': 'fr',
    'gu': 'gu',
    'hi': 'hi',
    'it': 'it',
    'ja': 'ja',
    'ko': 'ko',
    'kk': 'kz',
    'nl': 'nl',
    # Additional mappings as needed
}

# Consider adding a function to handle fallbacks or alternative mappings dynamically
def get_model_for_lang_code(lang_code):
    # Direct mapping or fallback logic
    model_key = lang_code_map.get(lang_code, 'en')  # Default to 'en' if no match found
    return models[model_key]

# Usage example
detected_lang_code = 'en-us'  # Example detected language code
model = get_model_for_lang_code(detected_lang_code)

# Function to capture audio and recognize speech using Vosk
def recognize_speech(language='en'):
    model = models.get(language, models['en'])  # Default to English model if language is not supported
    recognizer = vosk.KaldiRecognizer(model, 16000)
    
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()
    
    print("Listening...")
    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text = json.loads(result)["text"]
            print("Recognized Text:", text)
            return text

# Function to detect language of the text
def detect_language(text):
    try:
        lang = detect(text)
        print("Detected Language:", lang)
        return lang_code_map.get(lang, 'en')
    except Exception as e:
        print(f"Language detection error: {e}")
        return 'en'

# Function to translate text using OpenAI GPT-4o Mini API
def translate_text(text, target_lang='en'):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a translation assistant. Only provide the translated text without any explanations."},
                {"role": "user", "content": f"Translate the following text to {target_lang}: {text}"}
            ]
        )
        translated_text = response.choices[0]['message']['content'].strip()
        print("Translated Text:", translated_text)
        return translated_text
    except Exception as e:
        print(f"Translation error: {e}")
        return text

# Function to create a topmost window displaying subtitles
def display_subtitle(text):
    print(f"Displaying subtitle: {text}")
    
    root = tk.Tk()
    root.overrideredirect(1)  # Remove border
    root.attributes('-topmost', True)  # Keep on top

    # Create a frame with the same background color as the text background
    frame = tk.Frame(root, bg='white')
    frame.pack(padx=10, pady=10)

    # Add the label to the frame
    label = Label(frame, text=text, font=('Helvetica', 20), bg='white', fg='black')
    label.pack()

    # Calculate window size based on text length
    num_chars = len(text)
    text_width = 15 * num_chars + 40  # Adjust width based on number of characters
    text_height = 50 + 20
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{text_width}x{text_height}+{(screen_width - text_width) // 2}+{screen_height - text_height - 100}")

    root.after(3000, lambda: root.destroy())  # Destroy after 3 seconds
    root.mainloop()

# Function to send subtitles to display
def send_to_display_app(text):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 65432))
        client_socket.sendall(text.encode('utf-8'))
        client_socket.close()
    except Exception as e:
        print(f"Error sending to display app: {e}")

# Server to handle incoming subtitle display requests
def display_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen()
    
    while True:
        conn, addr = server_socket.accept()
        with conn:
            data = conn.recv(1024)
            if data:
                display_subtitle(data.decode('utf-8'))

# Main function to run the program
def main():
    threading.Thread(target=display_server, daemon=True).start()
    
    while True:
        text = recognize_speech()
        if text:
            detected_lang = detect_language(text)
            if detected_lang != 'en':
                translated_text = translate_text(text, target_lang='en')
                send_to_display_app(translated_text)
            else:
                send_to_display_app(text)

if __name__ == "__main__":
    main()