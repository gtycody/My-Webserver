#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 

#define BUFSIZE 1024
#define SERVER_PORT 18000

void error(char *msg) {
    perror(msg);
    exit(0);
}

int main(int argc, char **argv) {
    int sockfd, n;
    struct sockaddr_in serveraddr;
    char buf[BUFSIZE];

    /* socket: create the socket */
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0)
        error("ERROR opening socket");

    /* build the server's Internet address */
    bzero((char *) &serveraddr, sizeof(serveraddr));
    serveraddr.sin_family = AF_INET;
    serveraddr.sin_port = htons(SERVER_PORT);

    /* connect: create a connection with the server */
    if (connect(sockfd, (struct sockaddr *)&serveraddr, sizeof(serveraddr)) < 0) 
        error("ERROR connecting");

    /* get message line from the user */
    while(1){
        printf("Please enter msg: ");
        bzero(buf, BUFSIZE);
        fgets(buf, BUFSIZE, stdin);

        /* write: send the message line to the server */
        if ((n = write(sockfd, buf, strlen(buf)))< 0) 
            error("ERROR writing to socket");

        /* read: print the server's reply */
        bzero(buf, BUFSIZE);
        if ((n = read(sockfd, buf, BUFSIZE)) < 0) 
            error("ERROR reading from socket");

        printf("Echo from server: %s\n", buf);
    } 
    close(sockfd);
    return 0;
}   