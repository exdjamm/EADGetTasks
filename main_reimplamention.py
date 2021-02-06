from eadapi import scrapead 
from dbead import dbjson

import sys.path as path
from json import loads, dumps

def get_login():
	name_file = 'login.json'
	file_exists = path.exists(name_file)

	with open(name_file, 'rw') as login_data:
		login = list()

		if not file_exists:
			login = [
					input('Login: '), 
					input('Password: ')
				]
		else:
			login = loads(login_data.read())

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

	pass

def main():
	global db

	db = dbjson.DbEadJson()

	login, password = get_login()

	ead_data = scrapead.ScrapEad(login, password)

	courses_list = ead_data.get_courses_data()
	tasks_list = ead_data.get_tasks_data(filter_tasks)

	db.add_course(courses_list)
	db.add_task(tasks_list)

	db.save_change()

	upload_to_tasks_plataform(tasks_list)

	pass

if __name__ == '__main__':
	main()