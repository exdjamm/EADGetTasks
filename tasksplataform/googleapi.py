from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

import pickle
import os.path

class GoogleApi:
	def __init__(self, scopes, service, version, credentials_file="credentials.json"):
		self.google_service = None

		self.__scopes = [scopes]
		self.__service = service
		self.__version = version
		self.__credentials_file = credentials_file

		self.__auth()
		self.__create__google_service()

		pass	

	def __auth(self):
		if os.path.exists('token.pickle'):
			self.__load_token_file()
			self.__validate_auth()
		else:
			self.__get_auth()

		# Save the credentials for the next run
		self.__save_token_file()

		pass

	def __set_creds(self, creds):
		self.__creds = creds
		pass

	def __save_token_file(self):
		with open('token.pickle', 'wb') as token:
			pickle.dump(self.__creds, token)

		pass

	def __load_token_file(self):
		with open('token.pickle', 'rb') as token:
			self.__set_creds(pickle.load(token))
		pass

	def __validate_auth(self):
		if not self.__creds or not self.__creds.valid:
			if self.__creds and self.__creds.expired and self.__creds.refresh_token:
				self.__creds.refresh(Request())
		pass

	def __get_auth(self):
		flow = InstalledAppFlow.from_client_secrets_file(self.__credentials_file, self.__scopes)
		self.__set_creds(flow.run_local_server(port=0))

	def __create__google_service(self):
		self.google_service = build(self.__service, self.__version, credentials=self.__creds)
		pass

def test_with_tasks():
	api = GoogleApi("https://www.googleapis.com/auth/tasks", 'tasks', 'v1')
	pass

if __name__ == '__main__':
	test_with_tasks()