import read_json as rd
import pika

#Este algoritmo envia os dados lido do JSON para o rabbitmq

def send_message_to_rabbitmq():
	data = rd.read_json()

	#Estabecendo conexão com o rabbitmq
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()

	channel.queue_declare(queue='dados_json')

	channel.basic_publish(exchange='',
	                      routing_key='dados_json',
	                      body=str(rd.creat_data_to_pass())) #envia os dados do json para o rabbitmq

	print(" Dados Enviados")
	connection.close()

send_message_to_rabbitmq()