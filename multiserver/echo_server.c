/*2020-01-18 after construction the echo server I plan to consturuction the
muti-process server with fork() to dealing with mutiple incoming call at same
time. All the detail shown in the README.md*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

#include "response.h"

#define BUFSIZE 1024 //size of BUFSIZE is 4 BYTEs and its uint_32 
#define SERVER_PORT 18000 //lets define server port at front

#if 0 //can switch between 1 or 0 to turn on/off
/* Internet address */
struct in_addr {
  unsigned int s_addr; 
};

/* Internet style socket address */
struct sockaddr_in  {
  unsigned short int sin_family; /* Address family */
  unsigned short int sin_port;   /* Port number */
  struct in_addr sin_addr;	 /* IP address */
  unsigned char sin_zero[8]; /* Pad size of 8 just in default*/
};

/* Domain name service (DNS) host entry */
struct hostent {
  char    *h_name;        /* official name of host */
  char    **h_aliases;    /* alias list */
  int     h_addrtype;     /* host address type */
  int     h_length;       /* length of address */
  char    **h_addr_list;  /* list of addresses */
}
#endif

/*functions*/
void error(char* msg); /*error warper*/
void listen_sock(int* listenfd); /*listening socket create*/
void serveraddr_init(struct sockaddr_in* serveraddr); /*initialize server's internet address*/

//listening socket create:
void listen_sock(int* listenfd){
  if ((*listenfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    error("error opening socket 1");
}

//initialize server's internet address:
void serveraddr_init(struct sockaddr_in* serveraddr){
  serveraddr->sin_family = AF_INET;
  serveraddr->sin_addr.s_addr = htonl(INADDR_ANY); /*allow any connnection*/
  serveraddr->sin_port = htons(SERVER_PORT); /*set the protal*/
}

//error warper
void error(char *msg){
  perror(msg);
  exit(1);
}

/*--------------------------------------------------------------*/
/*                                                              */
/*                             MAIN                             */
/*                                                              */
/*--------------------------------------------------------------*/

int main(){
  int listenfd; /* listening socket */
  int connfd; /* connection socket */
  socklen_t clientlen; /* byte size of client's address */
  struct sockaddr_in serveraddr; /* server's addr */
  struct sockaddr_in clientaddr; /* client addr */
  struct hostent *hostp; /* client host info */
  char buf[BUFSIZE]; /* message buffer */
  char *hostaddrp; /* dotted decimal host addr string */
  int optval; /* flag value for setsockopt */
  int n; /* message byte size */
  int pid; /*process id*/
  char* sub_buf; /*catch the first line of http request*/

  listen_sock(&listenfd); /*creating listening socket*/
  bzero((char *) &serveraddr, sizeof(serveraddr));

  /*little trick to rerun the server immediately*/
  optval = 1;
  setsockopt(listenfd, SOL_SOCKET, SO_REUSEADDR, (const void *)&optval , sizeof(int));
  
  serveraddr_init(&serveraddr); /*init serveraddress*/

  /*bind socket with address setting*/
  if (bind(listenfd, (struct sockaddr *)&serveraddr, sizeof(serveraddr)) < 0)
    error("ERROR on binding");

  /*server goes to listen status*/
  if (listen(listenfd, 5) < 0)
    error("ERROR on listen");
  
  /*server goes to accept main loop*/
  while(1){
    connfd = accept(listenfd, (struct sockaddr *) &clientaddr, &clientlen);
    if (connfd < 0) 
      error("ERROR on accept");

    /*create child process to deal with connfd creating by accept*/  
    pid = fork();
    if(pid < 0){
      error("ERROR on creating process");
    }
    else if(pid == 0){ /*parent need to return to listen status and close the connfd*/
      printf("parent: %d keep accepting.\n",pid);
      close(connfd);
      continue;
    }
    else{ /*while child close listenfd*/
      printf("child: %d handle the quest.\n",pid);
      close(listenfd);

      while((n = read(connfd,buf,BUFSIZE))>0){

        hostp = gethostbyaddr((const void *)&clientaddr.sin_addr.s_addr,sizeof(clientaddr.sin_addr.s_addr), AF_INET);
        hostaddrp = inet_ntoa(clientaddr.sin_addr);
        printf("server:%d established connection with (%s)\n",pid, hostaddrp);

        /*echo to client*/
        sub_buf = http_split(buf);
        //printf("server:%d received %d bytes: %s\n",pid, n, buf);
        printf("subbuf: %s\n",sub_buf);
        if(sub_buf == "GET / HTTP/1.1" ){
          //fwrite();
        }
        n = write(connfd, buf, strlen(buf));
        if (n < 0) 
          error("ERROR writing to socket");
        bzero(buf, BUFSIZE);
      }
      
      /*catch error if n < 0*/
      if (n < 0){ 
        error("ERROR reading from socket");
        break;
      }
      /*break kill this child if it receiving 0 bytes*/
      else if(n == 0){
        printf("server:%d receive 0 bytes, server stop\n",pid);
        close(connfd);
      }
    }
  }
  return 0;
}

