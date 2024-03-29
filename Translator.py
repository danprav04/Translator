import speech_recognition as sr
from googletrans import Translator as translator
import keyboard
import ctypes
import time
from datetime import datetime
import os, subprocess
import _thread as thread
import subprocess
import database as db

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
				# Recognize Audio VTT
				rs = r.recognize_google(audio).lower()
				print(rs)

				# # Translate Via Google Translate
				res = tr.translate(rs, src='en', dest='ru')
				
				# Save To Variables
				orig = rs
				translated = res.text

				# Save Translation To File
				with open(path, 'a', encoding='utf-8') as f:
   					f.write(f"\n{orig} - {translated}")
				# Push To Github
				thread.start_new_thread( push_to_git, ( ) )

				# add to sql database
				try:
					db.add_translation(now.strftime("%d/%m/%Y %H:%M:%S"), orig, translated)
					print("Translation added to database")
				except Exception:
					print("Couldn't add to database")

				# Show Window With The Translation
				ctypes.windll.user32.MessageBoxW(0, f"{orig}\n{translated}", "Translator", 0)

			except sr.UnknownValueError:
				print("Could not understand audio")
			except sr.RequestError as e:
				print(e)
		else:
			time.sleep(0.1)	


def push_to_git():
	subprocess.call(f'git add {path}', shell=True)
	subprocess.call('git commit -m "Translation added', shell=True)
	subprocess.call('git push origin', shell=True)


if __name__ == "__main__":
	main()

