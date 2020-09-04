from TaskAPI import *
from EADscrapping import *
import os.path
from os import remove

if __name__ == '__main__':
	print("[EADAPP]\t>> starting...")
	print("[EADAPP]\t>> get login...")
	if os.path.exists("login.json"):
		with open("login.json", 'r') as login:
			json = loads(login.read())
			user = json['user']
			senha = json['senha']
	else:
		user = input("Digite o seu login >\t>> ")
		senha = input("Digite a sua senha >\t>> ")
		with open("login.json", "w") as login:
			json = {"user":user, 'senha':senha}
			login.write(dumps(json))
	print("[EADAPP]\t>> Done.")
	try:
		SITE = ScrapEAD(user, senha)
		SITE.setToken()
		SITE.login()
		SITE.setSessionKey()
		SITE.setCourses()
		SITE.setCoursesTasks()
		courses = SITE.getCourses()


		API = TaskAPI()
		nameTasklists = API.getNameTasksLists()
		print("[EADAPP]\t>> add tasks to google task.")
		for course in courses:
			if course not in nameTasklists:
				courseID = API.createNewTaskList({'title': course})['id']
				
			else:
				courseID = API.getTasklistIDByName(course)

			for task in courses[course]['tasks']:
				#tasklist_id = courses[course]['id'] if courses[course]['id'] != '' else '@default'
				if task != []:
					API.insertNewTask(body=task, tasklist=courseID)
		print("[EADAPP]\t>> Exiting.")
	except Exception as e:
		with open('copy.json', 'r') as backup:
			with open('tasks.json', 'w') as issue:
				issue.write(backup.read())
		
		
	
