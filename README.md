# AirBnB_clone

This is the very first step towards building a full web application: the AirBnB clone.

The command interpreter or console create the data model and allows for some defined operations, like:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file(JSON-file), a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object and saves into a JSON-file
* Destroy an object


## Objectives

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

## Execution(How to)
* Firstly clone this Repository
* cd into the cloned Repo(i.e. cd AirBnB_clone)
* execute/run consoole.py file

## Commands and Usage
|  *help*  |  ***help*** **;* ***help*** <command name>|
|  *quit*  |  ***quit***  |
|  *EOF*  |  ***EOF***  |
|  *create*  |  ***create***  <class name>|
|  *show*  |  ***show*** <class name> <object id>|
|  *destroy*  |  ***destry*** <class name> <object id>|
|  *all*  |  ***all*** **;** ***all*** <class name>|
|  *update*|  ***update*** <class name> <object id> <attribute name> <attribute value>|

## Example 1

This console works like this in interactive mode:
'''
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

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
'''
## Example 2
'''
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb)
'''

## Example 3
'''
vagrant@ubuntu-focal:~/AirBnB_clone$ ./console.py
(hbnb)create User
4a1f0fdc-bd29-492f-b9ae-2256acbecfd0
(hbnb)update User 4a1f0fdc-bd29-492f-b9ae-2256acbecfd0 email quesses1@gmail.com
(hbnb)show User 4a1f0fdc-bd29-492f-b9ae-2256acbecfd0
[User] (4a1f0fdc-bd29-492f-b9ae-2256acbecfd0) {'id': '4a1f0fdc-bd29-492f-b9ae-2256acbecfd0', 'created_at': datetime.datetime(2022, 11, 27, 23, 15, 34, 41135), 'updated_at': '2022-11-27T23:15:34.041142', 'email': 'quesses1@gmail.com'}
(hbnb)update User 4a1f0fdc-bd29-492f-b9ae-2256acbecfd0 name Abdulquadir
** no instance found **
(hbnb)update User 4a1f0fdc-bd29-492f-b9ae-2256acbecfd0 first_name Abdulq
uadir
(hbnb)all User
["[User] (73d448a9-bd9b-448e-b777-f0f21822c6ff) {'id': '73d448a9-bd9b-448e-b777-f0f21822c6ff', 'created_at': datetime.datetime(2022, 11, 27, 22, 29, 55, 649358), 'updated_at': '2022-11-27T22:29:55.649363', 'email': 'quesses1@gmail.com'}", "[User] (4a1f0fdc-bd29-492f-b9ae-2256acbecfd0) {'id': '4a1f0fdc-bd29-492f-b9ae-2256acbecfd0', 'created_at': datetime.datetime(2022, 11, 27, 23, 15, 34, 41135), 'updated_at': '2022-11-27T23:15:34.041142', 'email': 'quesses1@gmail.com', 'first_name': 'Abdulquadir'}"]
(hbnb)all
["[BaseModel] (5f54056c-7235-4588-b4f7-c492185e91dc) {'id': '5f54056c-7235-4588-b4f7-c492185e91dc', 'created_at': datetime.datetime(2022, 11, 26, 23, 17, 6, 86689), 'updated_at': '2022-11-26T23:17:06.086696'}", "[BaseModel] (9e2bab50-b0cb-4b5b-9d6a-954e169f2b1f) {'id': '9e2bab50-b0cb-4b5b-9d6a-954e169f2b1f', 'created_at': datetime.datetime(2022, 11, 26, 23, 17, 48, 510932), 'updated_at': '2022-11-26T23:17:48.510940'}", "[User] (73d448a9-bd9b-448e-b777-f0f21822c6ff) {'id': '73d448a9-bd9b-448e-b777-f0f21822c6ff', 'created_at': datetime.datetime(2022, 11, 27, 22, 29, 55, 649358), 'updated_at': '2022-11-27T22:29:55.649363', 'email': 'quesses1@gmail.com'}", "[User] (4a1f0fdc-bd29-492f-b9ae-2256acbecfd0) {'id': '4a1f0fdc-bd29-492f-b9ae-2256acbecfd0', 'created_at': datetime.datetime(2022, 11, 27, 23, 15, 34, 41135), 'updated_at': '2022-11-27T23:15:34.041142', 'email': 'quesses1@gmail.com', 'first_name': 'Abdulquadir'}"]
(hbnb)
'''
