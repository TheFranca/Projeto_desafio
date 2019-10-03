import pika
from pymongo import MongoClient
client = MongoClient("localhost",27017)

lista_de_dados = []

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='dados_json')

#Lê os dados do rabbitmq
def callback(ch, method, properties, body):
    print(" [x] Received " % body) #Tipo de dado recebido: bytes
    db = client.dados_json

    lista_de_dados.append(str(body))

    concat = (str(lista_de_dados[0].replace("\\","").split(",")[4]) + str(lista_de_dados[0].replace("\\","").split(",")[5]))
    
#Insere os dados lidos no mongodb
    db.dados.insert_one({
    	"acess_time": str(lista_de_dados[0].replace("\\","").split(",")[0]),
    	"id": str(lista_de_dados[0].replace("\\","").split(",")[1]),
    	"request_method": str(lista_de_dados[0].replace("\\","").split(",")[2]),
    	"uri": str(lista_de_dados[0].replace("\\","").split(",")[3]),
    	"user_agent": concat,
    	"user_id": str(lista_de_dados[0].replace("\\","").split(",")[6])

    	})

    lista_de_dados.clear()
    

channel.basic_consume('dados_json', callback, auto_ack=True)



print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()

