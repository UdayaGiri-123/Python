# Python

## Datatypes

#####  1.String
##### 2. Numeric

In Numeric it is again divided into int and float 

Python is a dynamically typed language. It means that unlike Java, we do not need to mention data types like # String or # Int before variable names.

Based on the data present on right hand side , it allocates respective data type accordingly

## Keywords in python :

There are few words which are reserved and have particular functionality in python. Those words are not allowed to be used
as variables to store any data as it will conflict and the interpreter can't process them.

Few of those keywords are :
#
##### 1.And
##### 2.Or
##### 3.Not
##### 4.for
##### 5.while
##### 6.if
##### 7.else
##### 8.elif
##### 9.class
##### 10.def

## Variables in python:

##### 1. Local variables 
Variables defined inside a method whose scope is restricted to the method or function are Local variables.


##### 2. Global variables
Variables defined outside of method or block are global variables and they can be used anywhere throughout the program. 

## # Functions:

Importance of using functions in code
##### 1. Reusability
  When we define a function using 'def' keyword, it can be used anywhere in the code.
  Example : addition method once defined can be called multiple times
  ##### def addition():
  #####  add =  num1+num2
  #####  print(add)
##### 2. Readability
   When we define functions, it gives a structured format for our code reducing clumsyness.
##### 3. Debugging
   It is also easier to debug the code
DRY - Don't repeat yourself

## Modules:

Modules are nothing but group of functions. A set of methods can be defined in a file and that can be exported as module.

We use 'import' keyword to get the module and use functions defined under it.

## Packages:

Packages are like group of modules

## Python workspaces
In our machine if there is a need to use different environments holding diff python versions or installed with unique package types , Workspaces can be used.

###### create a new workspace
python -m venv projabc  // this creates a new folder in the current directory

###### activate the workspace
projabc\Scripts\activate
