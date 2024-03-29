from abc import ABC, abstractmethod 

class TasksInterface(ABC):
	"""docstring for DBead"""
	
	@abstractmethod
	def create_list(self, name) -> str:
		pass

	@abstractmethod
	def get_lists(self) -> list:
		pass

	@abstractmethod
	def search_list(self, name) -> str:
		pass

	@abstractmethod
	def add_task_to_list(self, id_list, data) -> None:
		pass


