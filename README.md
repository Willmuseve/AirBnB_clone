# AirBnB clone project

## Context
The AirBnB project goal is to build a complete web application that clone the current AirBnB website.
We need to implement many steps such as HTML/CSS templates, database storage, API, front-end integration...
The objective here is to write a command interpreteur to manage AirBnB objects around these points:

* put in place a parent class,`BaseModel`, that take care of initialization, serialization and deserialization of instances
* create a simple flow of serialization/deserialization
* create that are useful for AirBnB (`User`,`State`, `City`, `Place`...) and that inherit from `BaseModel`
* create the first abstracted storage engine: File Storage
* create all unnitests to validate all classes and the storage engine

## What does the command interpreteur

It's just similar to a shell but limited to a specific use-case. IN our case, we want to be able too manage the objects of our project:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from the database (or file storage just in that project)
* Do operations on object (count, compuute stats, etc...)
* Update attributes of an object
* Destroy an object

## Resources

Read or watch:

* [cmd module](https://docs.python.org/3.8/library/cmd.html)
* [cmd module in depth](http://pymotw.com/2/cmd/)
* [uuid module](https://docs.python.org/3.8/library/uuid.html)
* [datetime](https://docs.python.org/3.8/library/datetime.html)
* [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
* [cmd module wiki page](https://wiki.python.org/moin/CmdModule)
* [Python unittest](https://realpython.com/python-testing/)

## Requirements

### Python Scripts

* Allowed editors: **vi**, **vim**, **emacs**
* All your files will be interpreted/compiled on Ubuntu **20.04 LTS** using python3 (version **3.8.5**)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A **README.md** file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version **2.8.***)
* All your files must be executable
* The length of your files will be tested using ``wc``
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
### Python Unit Tests

* Allowed editors: **vi**, **vim**, **emacs**
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: **.py**)
* All your test files and folders should start by **test_**
* Your file organization in the tests folder should be the same as your project
    * e.g., For **models/base_model.py**, unit tests must be in: **tests/test_models/test_base_model.py**
    * e.g., For **models/user.py**, unit tests must be in: **tests/test_models/test_user.py**
* All your tests should be executed by using this command: python3 -m unittest discover tests
* You can also test file by file by using this command:` python3 -m unittest tests/test_models/test_base_model.py`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

## Execution

Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`