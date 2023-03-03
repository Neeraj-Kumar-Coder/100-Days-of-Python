import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

names = ["Mummy", "Papa", "Neeraj", "Neha"]

for name in names:
    speaker.Speak(f"Shoutout to {name}")
