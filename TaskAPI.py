from __future__ import print_function
import pickle
import os.path

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

class TaskAPI:
	"""docstring for TaskAPI"""
	def __init__(self, SCOPES=['https://www.googleapis.com/auth/tasks']):
		self._creds = None
		self._service = None

		self.__getToken()
		self.__testCreds(SCOPES)
		self.__createService()

		self.tasklists = self._service.tasklists()
		self.tasks = self._service.tasks()
		self.setTasklistsItems()
		pass

	def __getToken(self):
		if os.path.exists('token.pickle'):
			with open('token.pickle', 'rb') as token:
				self.__setCreds(pickle.load(token))
		pass

	def __setCreds(self, creds):
		self._creds = creds

		pass

	def __testCreds(self, SCOPES):
		# If there are no (valid) credentials available, let the user log in.
		if not self._creds or not self._creds.valid:
			if self._creds and self._creds.expired and self._creds.refresh_token:

				self._creds.refresh(Request())
			else:
				self.__getCredentials(SCOPES)
			# Save the credentials for the next run
			self.__saveToken()

	def __saveToken(self):
		with open('token.pickle', 'wb') as token:
			pickle.dump(self._creds, token)

		pass

	def __getCredentials(self, SCOPES):
		flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
		self.__setCreds(flow.run_local_server(port=0))

	def __createService(self):
		self._service = build('tasks', 'v1', credentials=self._creds)

		pass

	def createNewTaskList(self, cmd):
		return self.tasklists.insert(body=cmd).execute()

	def getNameTasksLists(self):
		tasklistName = []
		for tasklist in self.tasklists.list().execute()['items']:
			tasklistName.append(tasklist['title'])
		return tasklistName

	def getTasklistIDByName(self, name):
		for tasklist in self.__itemsTasklists:
			if tasklist['title'] == name:
				tasklistID = tasklist['id']
				break

		return tasklistID

	def setTasklistsItems(self):
		self.__itemsTasklists = self.tasklists.list().execute()['items']
		pass

	def listTask(self, tasklist="@default"):
		try:
			return self.tasks.list(tasklist=tasklist).execute()["items"], True
		except Exception as e:
			return self.tasks.list(tasklist=tasklist).execute(), False
		
	def insertNewTask(self, tasklist="@default", body=None):
		if body != None:
			return self.tasks.insert(tasklist=tasklist, body=body).execute()

if __name__ == '__main__':
	API = TaskAPI()
	items= API.listTasksList()
	print(items)