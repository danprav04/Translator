import speech_recognition as sr
from googletrans import Translator as translator
import keyboard
import ctypes
import time

r = sr.Recognizer()
tr = translator()

def main():
	while True:
		if keyboard.is_pressed('F7'):  
			with sr.Microphone() as source:
				audio = r.listen(source)
			try:
				rs = r.recognize_google(audio).lower()
				print(rs)
				res = tr.translate(rs, src='en', dest='ru')
				print(res.text)
				ctypes.windll.user32.MessageBoxW(0, f"{rs}\n{res.text}", "Translator", 0)
			except sr.UnknownValueError:
				print("Could not understand audio")
			except sr.RequestError as e:
				print(e)
		else:
			time.sleep(0.1)	


if __name__ == "__main__":
	main()

