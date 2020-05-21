from SheetsAPI import *
from EADscrapping import *
import os.path
from os import remove
from time import sleep

if __name__ == '__main__':
	h = 2
	m = 0
	s = 0
	delayDuration = h * 60 * 60 + m * 60 + s

	print("[EADAPP]\t>> starting...")
	print("[EADAPP]\t>> get login...")
	if os.path.exists("login.json"):
		with open("login.json", 'r') as login:
			json = loads(login.read())
			user = json['user']
			senha = json['senha']
	else:
		user = input("Digite o seu login >>> ")
		senha = input("Digite a sua senha >>> ")
		with open("login.json", "w") as login:
			json = {"user":user, 'senha':senha}
			login.write(dumps(json))
	print("[EADAPP]\t>> Done.")

	try:
		API = SheetsAPI()
		SITE = ScrapEAD(user, senha)

		while True:
			SITE.setToken()
			SITE.login()
			SITE.setSessionKey()
			SITE.setCourses()
			SITE.setCoursesTasks()
			courses = SITE.getCourses()


			#nameTasklists = API.getNameTasksLists()
			print("[EADAPP]\t>> add tasks to google task.")
			for course in courses:
				for task in courses[course]['tasks']:
					if task != []:
						API.insertNewRow(list=task)
			sleep(delayDuration)
			
		print("[EADAPP]\t>> Exiting.")
	except Exception as e:
		raise e
		remove("tasks.json")
		
	
