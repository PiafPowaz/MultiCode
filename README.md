# MultiCode
Python code witch allow to use serveral programming languages.

# How to Use

# To create a .c file:

Use #DEFINE_TYPE_CODE#c before the c code and #END_DEFINE_TYPE_CODE#c at the end of of the c code.

Example:

#DEFINE_TYPE_CODE#c

#include <stdio.h>

int main()

{

  printf("Hello World");
  
}

#END_DEFINE_TYPE_CODE#c

Then launch MultiCode.py and write the path to the file.

# Example

Launch MultiCode.py and write the filename "Example" with the Example file in the same directory than MultiCode.py.

Multicode.py should create different new files : Example.c Example.py ...

# To Do

Use #DEFINE_PATH_TYPE_CODE#c#path to change the path to create the new .c file.

Use #DEFINE_NAME_FILE_TYPE_CODE#c#newName to change the name of the created .c file. 
