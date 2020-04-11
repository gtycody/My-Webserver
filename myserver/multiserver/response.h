#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXLINE 1024

/*variables*/
char sub_buf [MAXLINE];
int ptr_1;

/*function*/
char* http_split(char buf[]){
    while(buf[ptr_1] != '\n'){
        ptr_1 ++;
    }
    memcpy(sub_buf, buf, sizeof(char)*ptr_1);
    return sub_buf;
}
