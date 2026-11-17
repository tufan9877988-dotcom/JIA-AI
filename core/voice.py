
import subprocess

def speak(text):
    try:
        subprocess.run(
            ["termux-tts-speak", str(text)],
            check=True
        )
        return True
    except Exception as e:
        print("Voice Error:", e)
        return False
