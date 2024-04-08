from AnimalModule import Animal
import socket as sc
import pickle

sock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
sock.connect(('localhost',8888))
new_animal = Animal("Барсик", "Кошка")
sock.send(pickle.dumps(new_animal))
sock.close()