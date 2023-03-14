import time
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

TIME_INTERVAL_IN_MINUTES = 60

SLEEP_TIME = TIME_INTERVAL_IN_MINUTES * 60

while True:
    time.sleep(SLEEP_TIME)
    speaker.speak("It's time to drink water")
