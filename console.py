#!/usr/bin/python3
""" Personal practice of the airbnb clonbe project """

import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command line interface/console fo airbnb users"""

    prompt = "(hbnb)"
    __cls_list = ["BaseModel", "User"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Does nothing when empty line is entered into the console"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a specified Class, saves and prints the id
        USAGE: $ create <class name>
        """
        if arg == "":
            print("** class name missing **")
        elif arg not in HBNBCommand.__cls_list:
            print("** class doesn't exist **")
        else:
            ins = eval(arg)()
            storage.save()
            print(ins.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based\
                on the class name and id"""

        id_flag = 0
        args = arg.split()

        if arg == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__cls_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            _key = args[0] + "." + args[1]
            dic = storage.all()
            for key, obj in dic.items():
                if key == _key:
                    print(obj)
                    id_flag = 1

            if id_flag == 0:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id\
                and save the changes"""

        id_flag = 0
        args = arg.split()

        if arg == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__cls_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            _key = args[0] + "." + args[1]
            dic = storage.all()
            for key, obj in dic.items():
                if key == _key:
                    del dic[key]
                    storage.save()
                    storage.reload()
                    id_flag = 1
                    return

            if id_flag == 0:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances of a class\
                if specified, otherwise prints for all class instances"""

        _list = []
        dic = storage.all()
        if arg == "":
            for key, obj in dic.items():
                _list.append(str(obj))
            print(_list)
        elif arg in HBNBCommand.__cls_list:
            for key, obj in dic.items():
                if arg == key.split('.')[0]:
                    _list.append(str(obj))
            print(_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding\
                or updating attribute, and save the change\n
        USAGE: update <class name> <id> <attribute name> <attribute value>"""

        id_flag = 0
        args = arg.split()

        if arg == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__cls_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            _key = args[0] + "." + args[1]
            dic = storage.all()
            for key, obj in dic.items():
                if key == _key:
                    val_idx = 3 + len(args[0]) + len(args[1]) + len(args[2])
                    if arg[val_idx] == "\"":
                        val_idx += 1
                    value = arg[val_idx:]
                    if hasattr(obj, args[2]):
                        value = type(getattr(obj, args[2]))(arg[val_idx:])
                        setattr(obj, args[2], value)
                        storage.save()
                        storage.reload()
                        id_flag = 1

            if id_flag == 0:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()