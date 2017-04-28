# dopy
A simple taskrunner

do.py (a.k.a. dopy) is a very simple python file that allows execution of methods placed in the Tasks class from the command line. It is intended to be a tool to execute tasks like Fabric, Invoke or (Ruby's) Rake, only does not require any external libraries, therefore it is ideal to use as a bootstrap tool, e.g. 

$ ./do/py install_dependencies

(^^ assuming you have written an approporiate install_dependencies method!)

You can also pass in arguments as follows:

$ ./do/py method_name arg1=this arg2=that

That's pretty much all it does. If you want more advanced functionality, try invoke :-)
