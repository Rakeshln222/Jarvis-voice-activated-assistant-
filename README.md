

# 🎙️ Jarvis AI Assistant

Jarvis is a **voice-controlled personal assistant** built with Python. It listens to your voice commands, executes tasks like opening websites, playing songs, fetching live news, and even answering general queries using **OpenAI’s GPT model**.

## 🚀 Features

* **Voice Activation**: Wake up Jarvis by saying **“Jarvis”**.
* **Web Navigation**: Open common websites such as:

  * Google
  * YouTube
  * GitHub
  * WhatsApp
  * LinkedIn
* **Music Playback**: Play predefined songs from the `musiclibrary.py` file (links to YouTube).
* **Live News Updates**: Fetches the latest top 5 news headlines using **Google News RSS**.
* **AI Responses**: Uses **OpenAI GPT** to handle general questions or conversations.
* **Text-to-Speech (TTS)**: Speaks responses aloud via `pyttsx3`.


## 📂 Project Structure

```
📁 Jarvis-Assistant
│
├── main.py             # Main program (speech recognition, AI, commands)
├── musiclibrary.py     # Dictionary of songs with YouTube links
└── README.md           # Documentation
```

## ⚙️ Requirements

Install the following Python libraries before running the project:

```bash
pip install speechrecognition pyttsx3 requests beautifulsoup4 openai
```

Also ensure you have:

* **Python 3.8+**
* **Working microphone**
* **Internet connection** (for web requests & GPT responses)
  
## 🔑 Setup

1. Clone or download this repository.
2. Open `main.py`.
3. Replace `"YOUR_API_KEY_HERE"` with your **OpenAI API Key**:

   ```python
   openai.api_key = "your_openai_api_key"
   ```
4. (Optional) Edit `musiclibrary.py` to add or change your favorite songs:

   ```python
   music = {
       "song name": "youtube_link"
   }
   ```

## ▶️ Usage

Run the assistant with:

```bash
python main.py
```

* Say **“Jarvis”** to activate it.
* Example commands:

  * “Open Google”
  * “Play sky fall”
  * “Tell me news”
  * “What is artificial intelligence?”

## 🛠️ How It Works

1. **Speech Recognition**:

   * Listens via microphone using `speech_recognition`.
   * Wake word = **“Jarvis”**.

2. **Command Processing** (`processCommand()` in `main.py`):

   * Matches keywords like *open, play, news*.
   * If no match → forwards to **OpenAI GPT** for response.

3. **Music Library** (`musiclibrary.py`):

   * Dictionary of songs & YouTube links.

4. **News Fetching**:

   * Uses **Google News RSS feed** & `BeautifulSoup` to parse.

5. **Response Delivery**:

   * Outputs text on console.
   * Speaks aloud via **pyttsx3**.
     
## 📌 Limitations

* Needs **stable internet** for GPT & news.
* Songs are limited to those listed in `musiclibrary.py`.
* Accuracy depends on **Google Speech Recognition API**.
* API costs apply if GPT usage exceeds free limits.

## 🌟 Future Enhancements

* Add **Spotify/YouTube API integration** for unlimited music.
* Integrate with **smart home devices**.
* Add **calendar/scheduler** support.
* Improve **wake word detection** with hotword libraries like **Snowboy** or **Porcupine**.

