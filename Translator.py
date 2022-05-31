import speech_recognition as sr
from googletrans import Translator as translator
import keyboard
import ctypes
import time
from datetime import datetime

r = sr.Recognizer()
tr = translator()
now = datetime.now()
path = "C://Users//DANPRAV//OneDrive//Документы//Python2.0//Translator//TranslatedWords.txt"

def main():
	time_string = now.strftime("%d/%m/%Y %H:%M:%S")
	file_object = open(path, 'a')
	file_object.write(f"\n\n\n{time_string}\n")
	file_object.close()

	while True:
		if keyboard.is_pressed('F7'):  
			with sr.Microphone() as source:
				audio = r.listen(source)
			try:
				rs = r.recognize_google(audio).lower()
				print(rs)

				res = tr.translate(rs, src='en', dest='ru')
				print(res.text)

				orig = rs
				translated = res.text

				file_object = open(path, 'a')
				file_object.write(f"\n{orig} - {translated}")
				file_object.close()

				ctypes.windll.user32.MessageBoxW(0, f"{orig}\n{translated}", "Translator", 0)

			except sr.UnknownValueError:
				print("Could not understand audio")
			except sr.RequestError as e:
				print(e)
		else:
			time.sleep(0.1)	


if __name__ == "__main__":
	main()

