from requests import Session
from bs4 import BeautifulSoup
import os.path
from json import dumps, loads
from filterPages import getDataByDict

class ScrapEAD(Session):
	"""docstring for ScrapEAD"""
	def __init__(self, username, password):
		super(ScrapEAD, self).__init__()
		self.__courses = {}
		self.__num_of_courses = 0

		self.__tasks = {}
		self.__url = "https://ead.ifms.edu.br/"
		self.__ssl_cert = "ead-ifms-edu-br-chain.pem"
		self.headers.update({'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'})
		self.__html_doc = None
		self.__type =  'html.parser'

		self.__username = username
		self.__password = password
		self.__login_token = ""
		self.__session_key = ""

		self._payload = None

		self.__setTaskVar()		
		pass

	def __setTaskVar(self):
		if os.path.exists("tasks.json"):
			self.__exists = True
			with open("tasks.json", 'r') as doc:
				self.__tasks = loads(doc.read())
		else:
			self.__exists = False

	def setSessionKey(self):
		print("[SCRAP]\t\t>> get SessionKey...")
		self.__session_key = getDataByDict(self.__html_doc, tag='a', filter={'data-title':'logout,moodle'}, data='href').split('=')[1]
		#BeautifulSoup(self.__html_doc, self.__type).find("a", {'data-title':'logout,moodle'})["href"].split("=")[1]
		print("[SCRAP]\t\t>> Done")
		pass

	def setToken(self):
		print("[SCRAP]\t\t>> get Token...")
		self.__html_doc = self.get(self.__url, verify=self.__ssl_cert).text
		self.__login_token = getDataByDict(self.__html_doc, tag='input', filter={'name':'logintoken'}, data='value')
		#self.__login_token = BeautifulSoup(self.__html_doc, self.__type).find('input', {'name':'logintoken'}).get("value")
		print("[SCRAP]\t\t>> Done")
		pass

	def setCourses(self):
		print("[SCRAP]\t\t>> filter courses...")
		self._payload = {"sesskey":self.__session_key}
		self.__html_doc =self.get(self.__url+"blocks/custom_course_menu/interface.php", params=self._payload, verify=self.__ssl_cert).text
		tags_a = getDataByDict(self.__html_doc, tag='a', filter={"class":"courselist_course scrollable"}, method='all')
		#tags_a = BeautifulSoup(self.__html_doc, self.__type).find_all('a', {"class":"courselist_course scrollable"})
		for a in tags_a:
			course_name = a.span.string 

			if "2020" in course_name:
				course_name = course_name.split('-')[-1].strip()
				self.__courses[course_name] = {"link":a['href'], 'tasks':[]}
		print("[SCRAP]\t\t>> Done.")
		pass

	def setCoursesTasks(self):
		print("[SCRAP]\t\t>> make sintax of Task...")
		for course in self.__courses:
			url = self.__courses[course]['link']
			self.__html_doc = self.get(url).text
			self.__html_doc = BeautifulSoup(self.__html_doc, self.__type)

			if course not in self.__tasks:
				self.__tasks[course] = {'tasks':[]}

			if not self.__html_doc.find('ul', {'id':"multi_section_tiles"}):

				span_tags = self.__html_doc.find_all("span", {"class":"instancename"})

				for span in span_tags:
					title = span.text
					task_type = title.split(' ')[-1]
					title =  task_type + " - " + title.replace(task_type, '')#course + " - "+

					if "Avisos" not in title and title not in self.__tasks[course]['tasks']:
						
						notes = span.parent.get('href')
						if notes is None:
							continue
						#self.__courses[course]['id'] = self.__tasks[course]['id']
						self.__courses[course]['tasks'].append({"title":title, "notes":notes})
						self.__tasks[course]['tasks'].append(title)
			else: 
				pass
		
		print("[SCRAP]\t\t>> Done")
		pass

	def login(self):
		print("[SCRAP]\t\t>> login...")
		self._payload = {"username":self.__username, "password":self.__password, "logintoken":self.__login_token}
		self.__html_doc = self.post(self.__url+'login/index.php', data=self._payload, verify=self.__ssl_cert).text
		print("[SCRAP]\t\t>> Done")
		pass

	def getCourses(self):
		print("[SCRAP]\t\t>> returning courses...")
		self.saveTaskJSON()
		print("[SCRAP]\t\t>> Done")
		return self.__courses

	def saveTaskJSON(self):
		print("[SCRAP]\t\t>> Saving task.json...")
		with open("tasks.json", 'w') as doc:
			doc.write(dumps(self.__tasks))
		print("[SCRAP]\t\t>> Done")
		pass

if __name__ == '__main__':
	login = input("Digite o seu login >>> ")
	senha = input("Digite a sua senha >>> ")
	main =  ScrapEAD(login, senha)
	main.setToken()
	main.login()
	main.setSessionKey()
	main.setCourses()
	main.setCoursesTasks()
	main.saveTaskJSON()
	courses = main.getCourses()
	for course in courses:
		for task in courses[course]['tasks']:
			print(str(task))
	#print(res.status_code)