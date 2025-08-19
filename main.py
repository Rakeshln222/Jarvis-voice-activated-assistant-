import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from bs4 import BeautifulSoup
import openai

openai.api_key = "YOUR_API_KEY_HERE"

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://www.whatsapp.com/")
    elif "open linked in" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        parts = c.lower().split(" ", 1)
        if len(parts) > 1:
            song = parts[1]
            link = musiclibrary.music.get(song)
            if link:
                webbrowser.open(link)
            else:
                print(f"Song '{song}' not found in music library.")
                speak(f"Sorry, I couldn't find the song {song}.")
        else:
            print("No song specified to play.")
            speak("Please specify a song to play.")
    elif "news" in c.lower():
        try:
            url = "https://news.google.com/news/rss"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "xml")
            headlines = soup.find_all("title")[2:7]
            for i, headline in enumerate(headlines, start=1):
                news_title = headline.text
                print(f"{i}. {news_title}")
                speak(news_title)
        except Exception as e:
            print("Error while fetching news:", e)
            speak("Sorry, I could not fetch the news right now.")
    else:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
                    {"role": "user", "content": c}
                ]
            )
            reply = response["choices"][0]["message"]["content"]
            print("Jarvis:", reply)
            speak(reply)
        except Exception as e:
            print("OpenAI Error:", e)
            speak("Sorry, I couldn't process that with OpenAI.")

def main():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("listening...")
            try:
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                word = r.recognize_google(audio)
            except sr.UnknownValueError:
                print("Could not understand audio")
                continue
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                continue

            if word.lower() == "jarvis":
                speak("Ya")
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source)
                    try:
                        command = r.recognize_google(audio)
                        processCommand(command)
                    except sr.UnknownValueError:
                        print("Could not understand command")
                        speak("Sorry, I did not understand the command.")
                    except sr.RequestError as e:
                        print(f"Could not request results; {e}")
                        speak("Sorry, I could not process your command.")

if __name__ == "__main__":
    main()
