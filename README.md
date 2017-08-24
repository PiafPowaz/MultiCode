# MultiCode
Python code witch allow to use serveral programming languages.

# 1.1.0

Allow to use #DEFINE_PATH_TYPE_CODE#c#path to change the path to create the new .c file and #DEFINE_NAME_FILE_TYPE_CODE#c#newName to change the name of the created .c file. 

# How to Use

# To create a .c file:

Use #DEFINE_TYPE_CODE#c before the c code and #END_DEFINE_TYPE_CODE#c at the end of of the c code.

Use #DEFINE_PATH_TYPE_CODE#c#path to change the path to create the new .c file.

Use #DEFINE_NAME_FILE_TYPE_CODE#c#newName to change the name of the created .c file. 

Example:

#DEFINE_NAME_FILE_TYPE_CODE#c#newName

#DEFINE_PATH_TYPE_CODE#c#Dir/

#DEFINE_TYPE_CODE#c

#include <stdio.h>

int main()

{

  printf("Hello World");
  
}

This Example create a file newName.c in the Dir directory and contains the code :

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
