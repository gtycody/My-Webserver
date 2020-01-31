CC = gcc
ARGS = -Wall -O2 -I .

all: tcpserver tcpclient

tcpserver: tcpserver.c
	$(CC) $(ARGS) -o tcps tcpserver.c

tcpclient: tcpclient.c
	$(CC) $(ARGS) -o tcpc tcpclient.c

clean:
	rm -f *.o tcps tcpc *~
