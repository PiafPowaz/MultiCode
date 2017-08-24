# MultiCode
Python code witch allow to use serveral programming languages.

# How to Use
To create a .c file:
Use #DEFINE_TYPE_CODE#c before the c code and #END_DEFINE_TYPE_CODE#c at the end of of the c code.

Example:
#DEFINE_TYPE_CODE#c
#include <stdio.h>

int main()
{
  printf("Hello World");
}
#END_DEFINE_TYPE_CODE#c
