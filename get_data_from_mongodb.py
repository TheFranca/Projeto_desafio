from pymongo import MongoClient
client = MongoClient("localhost",27017)

lista_id = []
lista_acess_time = []
lista_request_method = []
lista_uri = []
lista_user_agent = []
lista_user_id = []

db = client.dados_json
collection = db.dados
founded_data = collection.find_one()

#Leio os dados do bd
for data in collection.find():
	lista_id.append(founded_data.get("id"))
	lista_acess_time.append(founded_data.get("acess_time"))
	lista_request_method.append(founded_data.get("request_method"))
	lista_uri.append(founded_data.get("uri"))
	lista_user_agent.append(founded_data.get("user_agent"))
	lista_user_id.append(founded_data.get("user_id"))

#OBS: Fiz com que cada key tivesse sua própria lista para poder facilitar os cálculos futuros que são pedidos no desafio. Com essa serapação
#será mais fácil gerar conclusões e realizar levantamento de dados. 
#OBS 2: A separação dos dados também facilitará a formatação dos dados, de acordo com cada requisito.
