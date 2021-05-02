# code_distancing
A simple script that separates the content of a given file.

## How it works!

It takes a file as input and generates another file with separated lines!

```sh

$ ./distancing.py -f main.c 

[*] Before Corona: 

#include <stdio.h>
int main() {
   printf("Hello, World!");
   return 0;
}

[*] After Corona: 

#include <stdio.h>

int main() 

{

   printf("Hello, World!");

   return 0;

}


[*] The modified version of your file has been generated as main_out.c!

```