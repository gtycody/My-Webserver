#include <sys/socket.h>
#include <sys/types.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define SERVER_PORT 18000

#define MAXLINE 4096

#define SA struct sockaddr

char * bin2hex(const unsigned char *input, size_t len);

char * bin2hex(const unsigned char *input, size_t len ){
    char *result;
    char *hexits = "0123456789ABCDEF";

    if(input == NULL || len <= 0){
        return NULL;
    }
    int resultlength = (len*3)+1; 

    result = malloc(resultlength);
    bzero(result, resultlength);

    for(int i = 0; i < len; i++){
        result[i*3] = hexits[input[i]>>4];
        result[(i*3)+1] = hexits[input[i] & 0x0F];
        result[(i*3)+2] = ' ';
    }
    return result;
}

int main(int argc, char** argv){
    int listenfd, connfd, n;
    struct sockaddr_in servaddr;
    uint8_t buff[MAXLINE+1];
    uint8_t recvline[MAXLINE+1];

    //create a socket
    listenfd = socket(AF_INET, SOCK_STREAM, 0);

    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(SERVER_PORT);

    bind(listenfd,(SA *)&servaddr,sizeof(servaddr));

    listen(listenfd,10);

    for(;;){
        struct sockaddr_in addr;
        socklen_t addr_len;
 
        //accept blocks until an incoming connection arrives
        printf("waiting for a connection on port %d\n", SERVER_PORT);
        fflush(stdout);
        connfd = accept(listenfd, (SA* )NULL, NULL);

        memset(recvline, 0 , MAXLINE);

        while((n = read(connfd, recvline, MAXLINE-1)) > 0){
            fprintf(stdout, "\n%s\n\n%s", bin2hex(recvline, n),recvline);

            //hacky way to detect the end of the message.
            if(recvline[n-1] == '\n'){
                 break;
            }
            memset(recvline, 0, MAXLINE);
        }         
    
        snprintf((char*)buff, sizeof(buff),"HTTP/1.0 200 OK\r\n\r\nHello");

        write(connfd, (char*)buff, strlen((char*)buff));
        close (connfd);
    }       
}