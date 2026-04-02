# JarvisTunes - Terminal Edition 🎧
# Save as jarvistunes.py

import time
import webbrowser

songs_by_mood = {
    "romantic": {
        "Raataan Lambiyan": "https://www.youtube.com/watch?v=gvyUuxdRdR4",
        "Tum Se Hi": "https://www.youtube.com/watch?v=2vUq5ONmIRU",
        "Kesariya": "https://www.youtube.com/watch?v=BddP6PYo2gs"
    },
    "chill": {
        "Phir Le Aaya Dil": "https://www.youtube.com/watch?v=oj0PYv3IUBE",
        "Shayad": "https://www.youtube.com/watch?v=SYF8f3v6G0A",
        "Suno Na Sangemarmar": "https://www.youtube.com/watch?v=qEBz6nF-z6A"
    },
    "sad": {
        "Agar Tum Saath Ho": "https://www.youtube.com/watch?v=oj0PYv3IUBE",
        "Tujhe Bhula Diya": "https://www.youtube.com/watch?v=ZGOyMTKkpug",
        "Channa Mereya": "https://www.youtube.com/watch?v=284Ov7ysmfA"
    },
    "study": {
        "Lo-fi Tum Hi Ho": "https://www.youtube.com/watch?v=G3lmxh8mYF8",
        "Lo-fi Shayad": "https://www.youtube.com/watch?v=_Q2EGqAQpA4",
        "Lo-fi Khairiyat": "https://www.youtube.com/watch?v=fRbUeKeUDFM"
    },
    "pumped": {
        "Zinda": "https://www.youtube.com/watch?v=E0qDrRJT0vA",
        "Apna Time Aayega": "https://www.youtube.com/watch?v=xtI-75CwBGE",
        "Sultan Title Track": "https://www.youtube.com/watch?v=wPxqcq6Byq0"
    }
}

print("🎧 Welcome to JarvisTunes - Your Mood Based Music Recommender!\n")

while True:
    mood = input("🧠 What's your mood? (romantic/chill/sad/study/pumped or 'exit' to quit): ").lower()

    if mood == "exit":
        print("👋 Exiting JarvisTunes... Keep vibing, boss!")
        break

    if mood in songs_by_mood:
        print(f"\nHere are some {mood} songs you might love:\n")
        for song, link in songs_by_mood[mood].items():
            print(f"🎵 {song}")
        print("\nWant to open any song? Type the name (or press Enter to skip):")
        choice = input("▶️ Song: ").strip()
        if choice in songs_by_mood[mood]:
            print("Opening in browser...")
            webbrowser.open(songs_by_mood[mood][choice])
        else:
            print("Skipping playback. Back to mood selection...\n")
    else:
        print("❌ Sorry, I don't recognize that mood yet.\n")# JarvisTunes - Terminal Edition 🎧
# Save as jarvistunes.py

import time
import webbrowser

songs_by_mood = {
    "romantic": {
        "Raataan Lambiyan": "https://www.youtube.com/watch?v=gvyUuxdRdR4",
        "Tum Se Hi": "https://www.youtube.com/watch?v=2vUq5ONmIRU",
        "Kesariya": "https://www.youtube.com/watch?v=BddP6PYo2gs"
        
    },
    "chill": {
        "Phir Le Aaya Dil": "https://www.youtube.com/watch?v=oj0PYv3IUBE",
        "Shayad": "https://www.youtube.com/watch?v=SYF8f3v6G0A",
        "Suno Na Sangemarmar": "https://www.youtube.com/watch?v=qEBz6nF-z6A"
    },
    "sad": {
        "Agar Tum Saath Ho": "https://www.youtube.com/watch?v=oj0PYv3IUBE",
        "Tujhe Bhula Diya": "https://www.youtube.com/watch?v=ZGOyMTKkpug",
        "Channa Mereya": "https://www.youtube.com/watch?v=284Ov7ysmfA"
    },
    "study": {
        "Lo-fi Tum Hi Ho": "https://www.youtube.com/watch?v=G3lmxh8mYF8",
        "Lo-fi Shayad": "https://www.youtube.com/watch?v=_Q2EGqAQpA4",
        "Lo-fi Khairiyat": "https://www.youtube.com/watch?v=fRbUeKeUDFM"
    },
    "pumped": {
        "Zinda": "https://www.youtube.com/watch?v=E0qDrRJT0vA",
        "Apna Time Aayega": "https://www.youtube.com/watch?v=xtI-75CwBGE",
        "Sultan Title Track": "https://www.youtube.com/watch?v=wPxqcq6Byq0"
    }
}

print("🎧 Welcome to JarvisTunes - Your Mood Based Music Recommender!\n")

while True:
    mood = input("🧠 What's your mood? (romantic/chill/sad/study/pumped or 'exit' to quit): ").lower()

    if mood == "exit":
        print("👋 Exiting JarvisTunes... Keep vibing, boss!")
        break

    if mood in songs_by_mood:
        print(f"\nHere are some {mood} songs you might love:\n")
        for song, link in songs_by_mood[mood].items():
            print(f"🎵 {song}")
        print("\nWant to open any song? Type the name (or press Enter to skip):")
        choice = input("▶️ Song: ").strip()
        if choice in songs_by_mood[mood]:
            print("Opening in browser...")
            webbrowser.open(songs_by_mood[mood][choice])
        else:
            print("Skipping playback. Back to mood selection...\n")
    else:
        print("❌ Sorry, I don't recognize that mood yet.\n")