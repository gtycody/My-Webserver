/*2020-01-18 after watching CMU ICS-15213 I found it is
very interesting to write and construct a echo server
so the whole program are based on the CMU echoserver.c 
on the 15213 web page. But i will modify the unexplain one */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

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

//all functions:
void error(char* msg); //error warper
void listen_sock(int* listenfd); //listening socket create:
void serveraddr_init(struct sockaddr_in* serveraddr); //initialize server's internet address:
void socket_accept(int* connfd, int listenfd, struct sockaddr_in* clientaddr, int* clientlen);

//listening socket create:
void listen_sock(int* listenfd){
  if ((*listenfd = socket(AF_INET, SOCK_STREAM, 0)) < 0){
    error("error opening socket");
  }
}

void socket_accept(int* connfd, int listenfd, struct sockaddr_in* clientaddr, int* clientlen){
  if ((*connfd = accept(listenfd,(struct sockaddr *)&clientaddr,clientlen)) < 0){
    error("error opening socket");
  }else{
    printf("connfd %d accept\n",*connfd);
  }
}

//initialize server's internet address:
void serveraddr_init(struct sockaddr_in* serveraddr){
  serveraddr->sin_family = AF_INET;
  serveraddr->sin_addr.s_addr = htonl(INADDR_ANY); /*allow any connnection*/
  serveraddr->sin_port = htons(SERVER_PORT);
}

//error warper
void error(char *msg){
  perror(msg);
  exit(1);
}

int main(int argc, char **agrv){
  int max_queue = 5; /* max allowable queue length */

  int listenfd; /* listening socket */
  int connfd; /* connection socket */
  int portno; /* port to listen on */
  int clientlen; /* byte size of client's address */
  struct sockaddr_in serveraddr; /* server's addr */
  struct sockaddr_in clientaddr; /* client addr */
  struct hostent *hostp; /* client host info */
  char buf[BUFSIZE]; /* message buffer */
  char *hostaddrp; /* dotted decimal host addr string */
  int optval; /* flag value for setsockopt */
  int n; /* message byte size */


  listen_sock(&listenfd); //creating listening socket
  bzero((char *) &serveraddr, sizeof(serveraddr));


  optval = 1;
  setsockopt(listenfd, SOL_SOCKET, SO_REUSEADDR, (const void *)&optval , sizeof(int));

  serveraddr_init(&serveraddr);//initialize serveraddr_in
    
  /*bind socket with address setting*/
  if (bind(listenfd, (struct sockaddr *) &serveraddr, sizeof(serveraddr)) < 0){
    error("ERROR on binding");
  }

  /*server goes to listen status*/
  if (listen(listenfd, 5) < 0){
    error("ERROR on listen");
  }

  /*main loop*/
  while(1){
    socket_accept(&connfd, listenfd, &clientaddr, &clientlen); // accepting clientaddr info
    hostp = gethostbyaddr((const void *)&clientaddr.sin_addr.s_addr,sizeof(clientaddr.sin_addr.s_addr), AF_INET);
    printf("server established connection with (%s)\n", hostaddrp);
    bzero(buf, BUFSIZE);
    n = read(connfd,buf,BUFSIZE);
    printf("server received %d bytes: %s", n, buf);
    n = write(connfd, buf, strlen(buf));
    close(connfd);
  }
  return 0;
}

