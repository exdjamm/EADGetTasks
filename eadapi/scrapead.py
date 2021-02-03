from sessionead import SessionEad

# Consts
FILTER_COURSES = ['2020-2', '2020/2', 'F4']

class ScrapEad(SessionEad):
	def __init__(self, login, password):
		super(ScrapEad, self).__init__(login, password)

		# starts variables
		self.__courses_data = list()
		self.__tasks_data = list()

		# init data courses
		self.__set_tasks_courses()

		pass

	def get_tasks_data(self, force_update=False):
		 
		condition = (force_update) or (self.__tasks_data == [])
		if condition:
			self.__set_tasks_courses()
			
		return self.__tasks_data

	def get_courses_data(self):
			
		return self.__courses_data

	def __set_courses_data(self):
		global FILTER_COURSES

		# Limpa o nome pego do site
		def clear_name(name: str) -> str:
			return name.split('-')[-1].strip()

		url_path = "blocks/custom_course_menu/interface.php"
		url = self._url(url_path)
		
		payload = {"sesskey" : self._session_key}
		response_text = self.get(url, params=password).text

		# Pega todas as tags html <a> com o filtro passado
		a_tags = self._filter_data(response_text, tag='a', filter={"class":"courselist_course scrollable"}, all=True)

		for a_tag in a_tags:
			# Para cada tag <a> que esta o nome do curso e seu link, pega o nome do curso e o link.
			# Adiciona a estrutura __courses_data
			
			course_name = clear_name(a_tag.span.string)
			link =  a_tag['href']

			test = [term in course_name for term in FILTER_COURSES]

			# Verifica se o nome do curso passa no filtro passado.
			if any(test):
				data = {"course_name": f"{course_name}", "link": f"{link}" }
				self.__courses_data.append(data)


		pass		

	def __set_tasks_courses(self) -> None:

		def is_task_already_save(task_title: str):
			# Verifica se a tarefa passada ja esta salva no banco de dados

			result = True #test()

			return result

		def get_task_data_from_tag(task_tag) -> dict:
			# Pega os dados de titulo e link de tarefa da tag passada

			# Tratamento do titulo
			title = task_tag.get('data-title')	

			if title is None:
				title = task_tag.text

			# Tratamento do link
			link = task_tag.get('href')	

			if link is None:
				link = task_tag.parent.get('href')
				
			if link is None:
				link = ''

			# Salvando as informações em um dicionario
			dict_data = {'title': f'{title}', 'link': f"{link}"}

			return dict_data

		def save_tasks_data(task_tags, course_data) -> None:
			for task_tag in task_tags:
				
				task_data = get_task_data_from_tag(task_tag)				

				is_to_save = not is_task_already_save(task_data.get('title'))

				if is_to_save:
					course_data['tasks'].append(task_data)
					self.__tasks_data.append(task_data)

			pass

		# Codigo do metodo
		for course_data in self.__courses_data:
			""" Para cada curso, acessa a pagina do proprio e pesquisa por tags HTML 
			que podem conter dados sobre as atividades.
			Salva os dados das atividades na estrutura __courses_data e no __tasks_data
			"""

			link = course_data.get('link')
			response_text = self.get(link).text
			task_tags = self._filter_data(response_text, filter={"class":"instancename"}, all=True)

			# Test if task_tags is empty
			if len(task_tags) != 0:

				save_tasks_data(task_tags, course_data)

			else:

				list_of_section = self._filter_data(response_text, filter={'class':'tile'}, all=True)
				for section in range( len( list_of_section ) ):

					payload = {'section': section}
					response_text = self.get(link, params=payload).text
					task_tags = self._filter_data(response_text, filter={"class":"instancename"}, all=True)

					save_tasks_data(task_tags, course_data)

		# Fim For

		pass

if __name__ == '__main__':
	login, senha = (input('Login:'), input("Senha:"))

	ead = ScrapEad(login, senha)
	courses = ead.get_courses_data()

	for course in courses:
		print(course['title'])
