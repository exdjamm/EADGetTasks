from TaskAPI import *
from EADscrapping import *
from os import remove
if __name__ == '__main__':
	login = input("Digite o seu login >>> ")
	senha = input("Digite a sua senha >>> ")
	try:
		SITE = ScrapEAD(login, senha)
		SITE.setToken()
		SITE.login()
		SITE.setSessionKey()
		SITE.setCourses()
		SITE.setCoursesTasks()
		courses = SITE.getCourses()


		API = TaskAPI()
		nameTasklists = API.getNameTasksLists()
		
		for course in courses:
			if course not in nameTasklists:
				courseID = API.createNewTaskList({'title': course})['id']
				
			else:
				courseID = API.getTasklistIDByName(course)

			for task in courses[course]['tasks']:
				#tasklist_id = courses[course]['id'] if courses[course]['id'] != '' else '@default'
				if task != []:
					API.insertNewTask(body=task, tasklist=courseID)

	except Exception as e:
		raise e
		#remove("tasks.json")
		
	
