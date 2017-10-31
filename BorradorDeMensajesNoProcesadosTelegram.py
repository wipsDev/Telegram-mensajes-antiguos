
#El objetivo de este .py es borrar mensajes sin procesar por el bot central para que no se ejecuten al ser ejecutado de nuevo

import urllib, json
import TokenAccess

token = TokenAccess.bot()

def MayorDeLista(lista): #Elige el mayor valor de una lista
    mayor = lista[0] 
    for valor in lista: 
        if valor > mayor: 
            mayor = valor 
    return mayor 

def BorraMensajesAntiguos(data):

	# Numero de mensajes Antiguos
	NMensajes = len(data)

	#Lsitado de los mensajes
	ListadoUpdate=[]
	for x in data:
		#print x["update_id"]
		ListadoUpdate.append(x["update_id"])

	#Se extrae el mayor update_id, y se le suma una unidad
	MayorMasUno = MayorDeLista(ListadoUpdate)+1

	# Se crea una llamada a borrar los mensajes 
	urlF = "https://api.telegram.org/bot%s/getUpdates?timeout=10&offset=%s" % (token,MayorMasUno)
	urllib.urlopen(urlF)

def CompruebaQueNoHayMensajes(url):

	response = urllib.urlopen(url)
	data = json.loads(response.read())
	data = data["result"]
	#return data == []



def main():
	# Monta la url para las comprobaciones

	url = "https://api.telegram.org/bot%s/getUpdates" % (token)

	response = urllib.urlopen(url)
	data = json.loads(response.read())
	data = data["result"]


	#Si hay mensajes antiguos, los borra, si no los hay, imprime que no hay mensajes
	if data != []:
		print "Hay mensajes nuevos, borrando..."
		BorraMensajesAntiguos(data)
		print "Borrados"
	else:
		print CompruebaQueNoHayMensajes(url)
		print "No hay mensajes nuevos"

	
def LimpiezaMensajes():
	main()

if __name__ == "__main__":
    main()
