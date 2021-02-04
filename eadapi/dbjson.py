from dbead import DbEadInterface

import os.path as sys_path
from json import loads, dumps

class DbEadJson(DbEadInterface):
	"""docstring for DbJson"""
	def __init__(self, path="", file="db.json"):
		
		self.path = path
		self.file = file

		self.__init_db_instance()
		pass

	def add_course(self, data) -> None:
		pass

	def add_task(self, data) -> None:
		pass
	
	def select_courses(self) -> list:
		pass
	
	def select_tasks(self) -> list:
		pass
	
	def save_changes(self) -> None:
		pass

	def __init_db_instance(self):
		path = f'{self.path}{self.file}'
		method = "r" if sys_path.exists(path) else 'w'

		with open(path, method) as db_json:
			if method == 'r':
				self.__db_instance = loads(db_json.read())
			else:
				self.__db_instance = {'courses_table':[], 'tasks_table':[]}

				db_json.write(dumps(self.__db_instance))

		pass

def main():
	db = DbEadJson()
	pass

if __name__ == '__main__':
	main()