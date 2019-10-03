import json
#Este algoritmo lê os dados do JSON

#Tenho ciência de que os dados deveriam ser importados de uma URL, porém realizei localmente afim de obter mais certezas nos testes
#Caso seja para importar o JSON de uma URL basta adicionar/modificar para as seguintes linhas:

#import requests
#r = requests.get('url')

lista = []

def read_json():
	with open("arquvio_json", "r", encoding = "utf8") as f:
		return json.load(f)

def creat_data_to_pass():
	myobj = read_json()
	lista.append(myobj.get("acess_time",""))
	lista.append(myobj.get("id",""))
	lista.append(myobj.get("request_method",""))
	lista.append(myobj.get("uri",""))
	lista.append(myobj.get("user_agent",""))
	lista.append(myobj.get("user_id",""))
	return lista

