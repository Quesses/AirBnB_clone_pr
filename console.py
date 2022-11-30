#!/usr/bin/python3
""" Personal practice of the airbnb clonbe project """

import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command line interface/console fo airbnb users"""

    prompt = "(hbnb)"
    __cls_list = ["BaseModel", "User", "Place", "State", "City",
                  "Amenity", "Review"]

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

def default(self, args):
        """default method that perfom actions when no command it's given"""
        count = 0
        if len(args.split(".")) > 1:
            class_name = args.split(".")[0]
            if class_name in HBNBCommand.class_list:
                try:
                    if args.split(".")[1] == "all()":
                        self.do_all(class_name)
                    if args.split(".")[1] == "count()":
                        for key, obj in storage.all().items():
                            if key.split(".")[0] == class_name:
                                count += 1
                        print(count)
                    if args.split(".")[1].split("(")[0] == "show":
                        id_ = args.split("\"")[1].split("\"")[0]
                        self.do_show(class_name + " " + id_)                    if args.split(".")[1].split("(")[0] == "destroy":
                        id_ = args.split("\"")[1].split("\"")[0]
                        self.do_destroy(class_name + " " + id_)
                    if args.split(".")[1].split("(")[0] == "update":
                        arg_list = args.split(".", 1)[1]
                        arg_list = arg_list.split("(")[1][:-1].split(",")
                        if "{" not in arg_list[1]:
                            id_ = arg_list[0][1:-1]
                            name = arg_list[1][2:-1]
                            value = arg_list[2][1:]
                            if value[0] == "\"":
                                value = value[1:-1]
                            self.do_update(class_name + "\
 " + id_ + " " + name + " " + value)
                        else:
                            id_ = arg_list[0][1:-1]
                            arg_dict = args.split(".")[1]
                            arg_dict = arg_dict.split("(")[1][:-1]
                            arg_dict = arg_dict.split("{")[1]
                            arg_dict = "{" + arg_dict
                            dictionary = eval(arg_dict)
                            for key, value in dictionary.items():
                                ret = self.do_update(class_name + "\
 " + id_ + " " + key + " " + str(value))
                                if ret == -1:
                                    break
                except Exception:
                    cmd.Cmd.default(self, args)
        else:
            cmd.Cmd.default(self, args)


if __name__ == "__main__":
    HBNBCommand().cmdloop()