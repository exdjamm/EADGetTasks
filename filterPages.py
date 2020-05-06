from bs4 import BeautifulSoup
"""
Objetivos:
Mandar um dicionario para filtrar as informaçoes de uma pagina.
{"tagName":{'id':"text", 'class':"etc", "atributo":"valor"}, "atributoGet":"href"}
"""

	
def getDataByDict(html, **filterDict):
	page = BeautifulSoup(html,"html.parser")

	nameTag = filterDict['tag']
	tagFilter = filterDict['filter']

	if filterDict.get("method") == "all":
		tag = page.find_all(nameTag, tagFilter)
	else:
		tag = page.find(nameTag, tagFilter)

	# print(tagFilter)
	# print(tag)
	# print(filterDict['tagName'])

	if filterDict['data'] == 'text':
		tagValue = tag.text
	else:
		tagValue = tag.get(filterDict['data'])

	return tagValue


if __name__ == '__main__':
	
	page = "<html><a class='tese'>Teste</></html>"
	print(getDataByDict(page, tag='a', filter={'class':"tese"}, data='class'))