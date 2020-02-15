#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXLINE 1024

/*variables*/
char sub_buf[MAXLINE];
char status_buff[MAXLINE];

int enter_1,enter_2,enter3;

/*function*/
char* http_split(char buf[]);


char* http_split(char buf[]){
  enter_1 = 0;
  while(buf[enter_1] != '\n'){
    enter_1++;
  }
  memcpy(sub_buf,buf,sizeof(char)*enter_1);
  return sub_buf;
}