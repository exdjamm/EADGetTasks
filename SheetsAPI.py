from __future__ import print_function
import pickle
import os.path

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

class SheetsAPI:
	"""docstring for TaskAPI"""
	def __init__(self, SCOPES=['https://www.googleapis.com/auth/spreadsheets']):
		self._creds = None
		self._service = None

		self.__getToken()
		self.__testCreds(SCOPES)
		self.__createService()

		self.__idSheet = '1vNwO9QB0RhjbntqBwPKkS_ns5-O7SdzvdhbC7RaEaYs'
		self.__range = "A2:D"

		self.addrow = self._service.values()
		#self.tasks = self._service.tasks()
		#self.setTasklistsItems()
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
		print("[SHEETS]\t\t>> connecting to google...")
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
		self._service = build('sheets', 'v4', credentials=self._creds)
		self._service = self._service.spreadsheets()
		print("[SHEETS]\t\t>> Done.")
		pass


	def insertNewRow(self, list=[]):
		body = {
			"majorDimension": "COLUMNS",
        	"values": list
		}
		print("[SHEETS]\t\t>> adding new task...")
		if body != None:
			task = self.addrow.append(spreadsheetId=self.__idSheet,
                                range=self.__range,
                                body=body, valueInputOption="USER_ENTERED").execute()
			print("[SHEETS]\t\t>> Done.")
			return task

if __name__ == '__main__':
	API = SheetsAPI()
	