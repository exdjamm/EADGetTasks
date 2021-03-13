from dbead.dbinterface import DbEadInterface

import os.path as sys_path
from json import loads, dumps

class DbEadJson(DbEadInterface):
	"""docstring for DbJson"""
	def __init__(self, path="", file="db.json"):
		self.__db_instance = None

		self.path = path
		self.file = file

		self.__init_db_instance()
		pass

	def add_course(self, data) -> None:
		if type(data) == type([]):
			self.__db_instance['courses_table'] += data
		else:
			self.__db_instance['courses_table'].append(data)
		pass

	def add_task(self, data) -> None:
		if type(data) == type([]):
			self.__db_instance['tasks_table'] += data
		else:
			self.__db_instance['tasks_table'].append(data)
		pass
	
	def select_all_courses(self) -> list:
		return self.__db_instance['courses_table']

	def select_all_tasks(self) -> list:
		return self.__db_instance["tasks_table"]

	def select_courses(self, field: str, data) -> list:

		def filter_courses(course):
			if course[field] == data:
				return course

		courses_selected = list(map(filter_courses, self.__db_instance['courses_table']))

		return courses_selected
	
	def select_tasks(self, field, data) -> list:
		def filter_tasks(task):
			if task[field] == data:
				return task

		tasks_selected = list(map( filter_tasks, self.__db_instance['tasks_table']))

		return tasks_selected
	
	def save_changes(self) -> None:
		path = f'{self.path}{self.file}'
		with open(path, 'w') as db_json:
			db_json.write(dumps(self.__db_instance))
		pass

	def __init_db_instance(self):
		path = f'{self.path}{self.file}'
		method = "r" if sys_path.exists(path) else 'w'

		with open(path, method) as db_json:
			if method == 'r':
				self.__db_instance = loads(db_json.read())
			else:
				self.__db_instance = {'courses_table':[], 'tasks_table':[]}

				self.save_changes()

		pass

def main():
	db = DbEadJson()
	pass

if __name__ == '__main__':
	main()