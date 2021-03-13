from eadapi import scrapead 
from dbead import dbjson
from tasksplataform import googletasks

import os.path as path
from json import loads, dumps

def get_login():
	name_file = 'login.json'
	file_exists = path.exists(name_file)

	login = list()

	if file_exists:
		with open(name_file, 'r') as login_data:
			login = loads(login_data.read())	

	else:
		with open(name_file, 'w') as login_data:
			login = [
					input('Login: '), 
					input('Password: ')
				]

			login_data.write(dumps(login))


	return login

def filter_tasks(task_data) -> bool:
	global db

	filter_result = bool()	
	field = "title"

	field_data = task_data[field]
	query_result = db.select_tasks(field, field_data)

	filter_result = True if len(query_result) > 0 else False

	return filter_result

def upload_to_tasks_plataform(tasks_list):
	global db

	tasks_plataform = googletasks.GoogleTask()

	for task in tasks_list:
		data_task = {
			"title": task['title'], 
			"notes": task['link']
		}

		task_course_id = task['course_id']

		task_course = db.select_courses('course_id', task_course_id)
		task_course = [ i for i in task_course if i != None]
		task_course = task_course[0]
		
		name_course = task_course['course_name']

		id_tasklist = tasks_plataform.create_list(name)
		tasks_plataform.add_task_to_list(id_tasklist, data_task)		

	pass

def main():
	global db

	db = dbjson.DbEadJson()

	login, password = get_login()

	ead_data = scrapead.ScrapEad(login, password, ['2021-1', '2021/2'],filter_tasks)

	courses_list = ead_data.get_courses_data()
	tasks_list = ead_data.get_tasks_data()

	db.add_course(courses_list)
	db.add_task(tasks_list)

	db.save_changes()

	upload_to_tasks_plataform(tasks_list)

	pass

if __name__ == '__main__':
	main()