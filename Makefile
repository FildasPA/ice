all: compile_server
	@echo "Compilation terminée"
	@echo "Exécuter './server' et 'make execute_client' dans des terminaux différents"


# SERVER

server: compile_server
	./server

coll_cpp:
	@slice2cpp Coll.ice

compile_server: coll_cpp Server.cpp
	@c++ -I. -c Coll.cpp Server.cpp
	@c++ -o server Coll.o Server.o -lIce -lIceUtil -pthread


# PYTHON CLIENT

python_client: coll_python
	python client.py

coll_python:
	@slice2py Coll.ice


# Autres

clean:
	@rm -f *.o
	@rm -f *.pyc
	@rm -f server
	@rm -f Coll.cpp
	@rm -f Coll.h
	@rm -f TP/*
	@rm -f Coll_ice.py

