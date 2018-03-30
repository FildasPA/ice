all: compile_server
	@echo "Compilation terminée"
	@echo "Exécuter './server' et 'make execute_client' dans des terminaux différents"

#-=-=-=-=-
# SERVER
#-=-=-=-=-

# server: compile_server
# 	./server
#
# coll_cpp:
# 	@slice2cpp Coll.ice
#
# compile_server: coll_cpp Server.cpp
# 	@c++ -I. -c Coll.cpp Server.cpp
# 	@c++ -o server Coll.o Server.o -lIce -lIceUtil -pthread

#-=-=-=-=-=-=-=-=
# SERVER PYTHON
#-=-=-=-=-=-=-=-=

server: compile_server
	python server

coll_py:
	@slice2py Coll.ice

compile_server:
	slice2py Coll.ice
	python server.py

#-=-=-=-=-=-=-=-=
# PYTHON ADMIN
#-=-=-=-=-=-=-=-=

admin:
	@slice2py Coll.ice
	python admin.py

#-=-=-=-=-=-=-=-=
# PYTHON CLIENT
#-=-=-=-=-=-=-=-=

client:
	@slice2py Coll.ice
	python client.py

#-=-=-=-=-=
# AUTRES
#-=-=-=-=-=

clean:
	@rm -f *.o
	@rm -f *.pyc
	@rm -f server
	@rm -f Coll.cpp
	@rm -f Coll.h
	@rm -f Vocal/*
	@rm -f Coll_ice.py

