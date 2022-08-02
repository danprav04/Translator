import pymysql

try:
	connection = pymysql.connect(
		host = "sql11.freesqldatabase.com", 
		port = 3306, 
		user = "sql11509619", 
		password = "AbsVEzJH82", 
		database = "sql11509619",
		cursorclass = pymysql.cursors.DictCursor
	)
	print("Successfully connected to the database...")

	def add_translation(time, orig, translted):
		try :
			with connection.cursor() as cursor:
				command = "INSERT INTO `translations` (`id`, `date_time`, `original_word`, `translated_word`) VALUES (NULL, %s, %s, %s);"
				cursor.execute(command, (time, orig, translted))
				connection.commit()
		except Exception:
			print("Didn't save the translation. Problem with the connection to the database.")

except Exception as ex:
	print("Database connection refused...")
	print(ex)