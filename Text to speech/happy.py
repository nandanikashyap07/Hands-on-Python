import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import os, time, re, json, random, psutil, subprocess
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import datetime
import pandas as pd

REMINDERS_FILE = "reminders.txt"

contacts = {
    "mom": "+91XXXXXXXXXX",
    "dad": "+91XXXXXXXXXX",
    "khushi": "+91XXXXXXXXXX",
    "brother": "+91XXXXXXXXXX"
}

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

try:
    mic_list = sr.Microphone.list_microphone_names()
    use_mic = True if mic_list else False
except:
    use_mic = False


def speak(t):
    print("Happy:", t)
    try:
        engine.say(t)
        engine.runAndWait()
    except:
        pass


def listen(timeout=5, phrase_time=6):
    if not use_mic:
        try:
            return input("You: ").lower().strip()
        except:
            return ""
    try:
        with sr.Microphone() as src:
            r.adjust_for_ambient_noise(src, duration=0.5)
            audio = r.listen(src, timeout=timeout, phrase_time_limit=phrase_time)
            text = r.recognize_google(audio, language="en-IN")
            return text.lower()
    except:
        return ""


def norm(t):
    return t.lower().strip() if t else ""


def extract_numbers(text):
    try:
        return [int(x) for x in re.findall(r"\d+", text)]
    except:
        return []


def extract_intent_and_target(t):
    t = norm(t)
    if not t:
        return None, ""

    keys = [
        "send scheduled message","list reminders","clear reminders","how are you",
        "set reminder","remind","open","search","play","plot","message","close",
        "shutdown","restart","lock","sleep","exit","stop","goodnight"
    ]

    for k in sorted(keys, key=len, reverse=True):
        if k in t:
            parts = t.split(k, 1)
            return k, parts[1].strip() if len(parts) > 1 else ""

    for kw in ["open","search","play","message","plot"]:
        f = re.search(rf"\b{kw}\b(.*)", t)
        if f:
            return kw, f.group(1).strip()

    return None, t


def plot_bar(vals):
    plt.figure()
    plt.bar(range(len(vals)), vals)
    plt.show()


def plot_line(vals):
    plt.figure()
    plt.plot(vals, marker="o")
    plt.show()


def plot_sin():
    x = np.linspace(0, 10, 400)
    y = np.sin(x)
    plt.figure()
    plt.plot(x, y)
    plt.show()


def handle_plot(t):
    nums = extract_numbers(t)
    if "bar" in t:
        if nums: plot_bar(nums)
        else: speak("I need numbers.")
    elif "line" in t:
        if nums: plot_line(nums)
        else: speak("Numbers?")
    elif "sin" in t:
        plot_sin()
    else:
        speak("I can plot bar, line or sine.")


def send_instant(t):
    if not t:
        speak("Whom should I text?")
        return

    who = next((c for c in contacts if c in t), "")
    if not who:
        speak("Contact missing.")
        return

    num = contacts[who]
    if "saying" in t:
        msg = t.split("saying", 1)[1].strip()
    else:
        msg = re.sub(who, "", t).replace("message", "").replace("to", "").strip()

    if not msg:
        speak("Message empty.")
        return

    try:
        pywhatkit.sendwhatmsg_instantly(num, msg, wait_time=8)
        speak(f"Text sent to {who}.")
    except:
        speak("Couldn't send.")


def send_schedule(t):
    nums = extract_numbers(t)
    if len(nums) < 2:
        speak("Tell hour and minute.")
        return

    h, m = nums[0], nums[1]
    who = next((c for c in contacts if c in t), "")
    if not who:
        speak("Contact?")
        return

    msg = re.sub(r"\d+|send|scheduled|message|to|at|" + who, "", t).strip()
    if not msg:
        speak("Message?")
        return

    try:
        pywhatkit.sendwhatmsg(contacts[who], msg, h, m)
        speak(f"Scheduled for {who}.")
    except:
        speak("Schedule error.")


def open_site(txt):
    if "." in txt:
        link = "https://" + txt
    else:
        sites = {
            "youtube":"https://youtube.com",
            "google":"https://google.com",
            "github":"https://github.com"
        }
        link = sites.get(txt, "https://www.google.com/search?q=" + txt)

    speak("Opening " + txt)
    try:
        webbrowser.open(link)
    except:
        speak("Unable.")


browsers = ["chrome.exe","msedge.exe","firefox.exe","opera.exe","brave.exe"]

def close_browser():
    for p in psutil.process_iter(['pid','name']):
        n = (p.info['name'] or "").lower()
        if any(b in n for b in browsers):
            try: p.kill()
            except: pass
    speak("Browser closed.")


APPS = {
    "notepad":"notepad.exe",
    "calculator":"calc.exe",
    "paint":"mspaint.exe",
    "cmd":"cmd.exe",
    "chrome":r"C:\Program Files\Google\Chrome\Application\chrome.exe"
}

FOLDERS = {
    "downloads": os.path.expandvars(r"C:\Users\%USERNAME%\Downloads"),
    "documents": os.path.expandvars(r"C:\Users\%USERNAME%\Documents"),
    "desktop": os.path.expandvars(r"C:\Users\%USERNAME%\Desktop"),
    "pictures": os.path.expandvars(r"C:\Users\%USERNAME%\Pictures"),
}


def open_app(t):
    for k,v in APPS.items():
        if k in t:
            speak("Opening " + k)
            try: subprocess.Popen(v)
            except: speak("Can't open.")
            return

    for k,v in FOLDERS.items():
        if k in t:
            speak("Opening " + k)
            try: os.startfile(v)
            except: speak("Couldn't open.")
            return

    speak("Not found.")


def close_app(t):
    for k in APPS:
        if k in t:
            speak("Closing " + k)
            for p in psutil.process_iter(['pid','name']):
                nm = (p.info['name'] or "").lower()
                if k in nm:
                    try: p.kill()
                    except: pass
            return

    if "browser" in t:
        close_browser()
        return

    speak("Nothing to close.")


def play_youtube(t):
    try:
        speak("Playing.")
        pywhatkit.playonyt(t)
    except:
        speak("Can't play.")


def system_cmd(c):
    if "shutdown" in c:
        speak("Bye.")
        os.system("shutdown /s /t 3")
    elif "restart" in c:
        speak("Restarting.")
        os.system("shutdown /r /t 3")
    elif "lock" in c:
        speak("Locking.")
        os.system("rundll32.exe user32.dll,LockWorkStation")
    elif "sleep" in c:
        speak("Sleeping.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


jokes = [
    "My PC went to sleep. I guess it was bored.",
    "I tried to catch some fog. I mist.",
    "Why was the computer cold? It forgot to close Windows."
]

fallbacks = ["Come again?", "Didn't catch that.", "Try saying it differently."]


def load_reminders():
    if not Path(REMINDERS_FILE).exists():
        return []
    try:
        with open(REMINDERS_FILE,"r") as f:
            return [json.loads(x) for x in f]
    except:
        return []


def save_reminders(d):
    with open(REMINDERS_FILE,"w") as f:
        for x in d:
            f.write(json.dumps(x) + "\n")


def add_rem(t):
    now = datetime.datetime.now()
    nums = extract_numbers(t)

    if len(nums)>=2:
        h,m = nums[0],nums[1]
    else:
        future = now + datetime.timedelta(minutes=5)
        h,m = future.hour, future.minute

    msg = re.sub(r"\d+|reminder|set|at|in|minutes","",t).strip()
    if not msg:
        msg = "Reminder"

    when = datetime.datetime(now.year, now.month, now.day, h%24, m%60)
    if when <= now:
        when += datetime.timedelta(days=1)

    data = load_reminders()
    data.append({"time": when.strftime("%Y-%m-%d %H:%M"), "msg": msg, "done": False})
    save_reminders(data)
    speak("Reminder added.")


def check_rem():
    now = datetime.datetime.now()
    data = load_reminders()
    changed = False

    for r in data:
        try:
            t = datetime.datetime.strptime(r["time"], "%Y-%m-%d %H:%M")
            if not r["done"] and now >= t:
                speak("Reminder: " + r["msg"])
                r["done"] = True
                changed = True
        except:
            pass

    if changed:
        save_reminders(data)


def list_rem():
    d = [x for x in load_reminders() if not x["done"]]
    if not d:
        speak("Nothing pending.")
        return
    for r in d:
        speak(r["time"] + " → " + r["msg"])


def greet():
    hr = datetime.datetime.now().hour
    if hr < 12: speak("Good morning.")
    elif hr < 17: speak("Good afternoon.")
    else: speak("Good evening.")


def run_assistant():
    speak("Happy online.")
    greet()
    check_rem()

    while True:
        check_rem()
        t = listen()

        if not t:
            speak(random.choice(fallbacks))
            continue

        if "hello happy" in t:
            speak("Yes, I'm here.")
            continue

        if "how are you" in t:
            speak("All good.")
            continue

        if "joke" in t:
            speak(random.choice(jokes))
            continue

        if "time" in t:
            speak(datetime.datetime.now().strftime("%I:%M %p"))
            continue

        if "date" in t:
            speak(datetime.datetime.now().strftime("%A, %d %B %Y"))
            continue

        if "remind" in t:
            add_rem(t)
            continue

        if "list reminders" in t:
            list_rem()
            continue

        if "clear reminders" in t:
            save_reminders([])
            speak("Cleared.")
            continue

        if "send scheduled message" in t:
            send_schedule(t)
            continue

        if "message" in t:
            send_instant(t)
            continue

        if "plot" in t:
            handle_plot(t)
            continue

        if "open" in t:
            if any(x in t for x in list(APPS.keys()) + list(FOLDERS.keys())):
                open_app(t)
            else:
                open_site(t.replace("open","").strip())
            continue

        if "close" in t:
            close_app(t)
            continue

        if "search" in t:
            q = t.replace("search","").strip()
            if q:
                speak("Searching.")
                pywhatkit.search(q)
            else:
                speak("What should I search?")
            continue

        if "play" in t:
            play_youtube(t.replace("play","").strip())
            continue

        if any(x in t for x in ["shutdown","restart","lock","sleep"]):
            system_cmd(t)
            continue

        if any(x in t for x in ["exit","stop","bye","goodnight"]):
            speak("See you soon. Happy offline.")
            break

        speak(random.choice(fallbacks))


run_assistant()
