# 🟡 Happy – Python Voice Assistant

Happy is a lightweight, offline-friendly **desktop voice assistant** built in Python.
It can understand voice commands, speak responses, set reminders, send WhatsApp messages, open apps/websites, plot graphs, and perform OS-level actions like shutdown or restart.
Designed especially for **Windows** and supports both **microphone mode** and **manual text mode**.

---

## 🚀 Features

### 🎤 Voice Interaction

* Speech recognition using `SpeechRecognition`
* Text-to-speech via `pyttsx3`
* Works with or without a microphone

### 🗂️ Assistant Capabilities

* Set, list, and clear reminders (saved in `reminders.txt`)
* Tell jokes, date, and time
* Search the web
* Play YouTube videos
* Open/close apps and folders
* Open browsers or search queries
* System actions (shutdown, restart, lock, sleep)

### 💬 WhatsApp Messaging

* Instant message sending
  — Uses `pywhatkit.sendwhatmsg_instantly`
* Scheduled WhatsApp messages
  — Uses `pywhatkit.sendwhatmsg`
* Contacts stored in a Python dictionary

### 📊 Plotting

* Bar chart
* Line graph
* Sine wave demo
  — Uses `matplotlib` and `numpy`

---

## 📂 Project Structure

```
|-- assistant.py         # Main program
|-- reminders.txt        # Auto-generated reminders database
|-- README.md            # Documentation
|-- .gitignore
```

---

## 🛠️ Requirements

Install dependencies:

```bash
pip install SpeechRecognition pyttsx3 pywhatkit matplotlib numpy psutil
```

Optional (for microphone input):

```bash
pip install PyAudio
```

---

## ▶️ How to Run

```bash
python assistant.py
```

Once running, say:

* **"open chrome"**
* **"set reminder for 5 PM saying buy milk"**
* **"send message to mom saying I'm on my way"**
* **"plot bar 10 20 40 15"**
* **"play shape of you"**
* **"shutdown system"**

Or type commands if microphone isn’t available.

---

## 🧠 How It Works

The assistant follows a simple pipeline:

1. **Listen** (speech → text)
2. **Normalize input**
3. **Detect intent** using keyword matching
4. **Trigger handler** (messaging, plotting, reminders, etc.)
5. **Speak output** to the user

Reminders are saved in JSON-line format inside `reminders.txt`.

---

## 🔐 Notes & Safety

* Phone numbers should be added manually inside the **contacts** dictionary.
* WhatsApp sending requires your machine to have WhatsApp Web logged in.
* System commands (shutdown/restart) should be used carefully.

---

## 🧩 Future Enhancements

* Wake-word detection (e.g., "Hey Happy")
* GUI dashboard for reminders & activity logs
* Improved NLP intent detection
* Background service mode

---


