CC = gcc
ARGS = -Wall -O2 -I .

all: echoserver echoclient

echoserver: echo_server.c
	$(CC) $(ARGS) -o server echo_server.c

echoclient: echo_client.c
	$(CC) $(ARGS) -o client echo_client.c

clean:
	rm -f *.o client server *~
