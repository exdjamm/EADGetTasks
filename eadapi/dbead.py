from abc import ABC, abstractmethod 

class DbEadInterface(ABC):
	"""docstring for DBead"""
	
	@abstractmethod
	def add_course(self, data) -> None:
		pass

	@abstractmethod
	def add_task(self, data) -> None:
		pass

	@abstractmethod
	def select_courses(self) -> list:
		pass

	@abstractmethod
	def select_tasks(self) -> list:
		pass

	@abstractmethod
	def save_changes(self) -> None:
		pass
