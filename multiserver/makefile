CC = gcc
ARGS = -Wall -O2 -I .

all: echoserver echoclient

echoserver: echo_server.c
	$(CC) $(ARGS) -o echoserver echo_server.c

echoclient: echo_client.c
	$(CC) $(ARGS) -o echoclient echo_client.c

clean:
	rm -f *.o echoclient echoserver *~
