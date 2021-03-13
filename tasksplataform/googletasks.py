from tasksplataform.tasksinterface import TasksInterface
from tasksplataform.googleapi import GoogleApi

class GoogleTask(TasksInterface, GoogleApi):
	"""docstring for GoogleTask"""
	def __init__(self, scopes="https://www.googleapis.com/auth/tasks"):
		service = 'tasks'
		version = 'v1'

		super(GoogleTask, self).__init__(scopes, service, version)

		self.__lists = None

		self.__tasklists = self.google_service.tasklists()
		self.__tasks = self.google_service.tasks()

		self.__update_list()

		pass

	def create_list(self, name) -> str:
		id_list = ''

		if name not in self.get_lists_name():
			result = self.__tasklists.insert(body={'title': name}).execute()
			id_list = result['id']
		else:
			id_list = self.search_list(name)

		return id_list
	
	def __update_list(self) -> None:	
		self.__lists = self.__tasklists.list().execute()['items']
		pass

	def get_lists(self) -> list:
		self.__update_list()
		
		return self.__lists
	
	def get_lists_name(self) -> list:
		self.__update_list()
		
		lists_name = []

		for list_item in self.__lists:
			list_name = list_item['title']

			lists_name.append(lists_name)

			pass

		return lists_name

	def search_list(self, name) -> str:
		id_list = ''

		for list_item in self.__lists:
			if list_item['title'] == name:
				id_list = list_item['id']

			continue

		return id_list

	def add_task_to_list(self, id_list, data) -> None:
		self.__tasks.insert(tasklist=id_list, body=data).execute() 
		pass
