#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from shlex import split
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines the BnB command interpreter"""

    prompt = "(hbnb) "

    
    def do_quit(self, arg):
        """command  exit the program."""
        return True
    
    def emptyline(self):
        """Do not do anything for recieving an empty line."""
        pass

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True
    
    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if len(argl) == 0:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)
            
    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            key = args[0] + "." + args[1]
            if key not in objs:
                print("** no instance found **")
            else:
                print(objs[key])

    def do_destroy(self, arg):
        """Deletes an"""            

if __name__ == '__main__':
    TurtleShell().cmdloop()

