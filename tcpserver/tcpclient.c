#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <signal.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

 
#define SERVER_PORT 80

#define MAXLINE 4096

#define SA struct sockaddr

int main(int argc, char** argv){
    int sockfd,n;
    int sendbytes;
    
    char sendline[MAXLINE];
    char receline[MAXLINE];

    struct sockaddr_in servaddr;

    //create a new socket
    sockfd = socket(AF_INET, SOCK_STREAM, 0);

    bzero(&servaddr, sizeof(servaddr));

    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(SERVER_PORT);

    //translate address
    inet_pton(AF_INET,argv[1], &servaddr.sin_addr);

    //connect to server
    connect(sockfd,(SA*)&servaddr , sizeof(servaddr));

    //connected
    sprintf(sendline, "GET / HTTP/1.1\r\n\r\n");
    sendbytes = strlen(sendline);

    //send the request
    n = write(sockfd,sendline,sendbytes);
    if(n < 0){
        printf("wirte error");
    }

    //receive the response
    memset(receline, 0, MAXLINE);

    while((n = read(sockfd, receline, MAXLINE-1))>0){
        printf("%s",receline);
    }

    exit(0);
}
