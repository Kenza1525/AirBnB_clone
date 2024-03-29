#!/usr/bin/python3
""" console for the project """
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex

class HBNBCommand(cmd.Cmd):
    """ Handles the command"""

    prompt = "(hbnb)"

    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        print("")
        return True

    def emptyline(self):
        """ Emptyline command that executes nothing """
        pass

    def do_create(self, arg):
        """ Create command to create a new object """
        if not arg:
            print("** class name missing **")
        elif arg in self.classes.keys():
            obj = self.classes[arg]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Show Command that prints the string representation
        of an object """
        if arg:
            args = shlex.split(arg)

            if args[0] not in self.classes.keys():
                print("** class doesn't exist **")
                return
            try:
                self.show_obj(storage.all(), args)
            except KeyError:
                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """ Destroy command that destroys an object """
        if arg:
            args = shlex.split(arg)

            if args[0] not in self.classes.keys():
                print("** class doesn't exist **")
                return
            try:
                self.destroy(storage.all(), args)

            except KeyError:
                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """" All command that prints all instances
        in string representation """
        obj_dict = storage.all()
        obj_list = []

        if not arg:
            for obj in obj_dict.values():
                obj_list.append(str(obj))
        else:
            try:
                args = shlex.split(arg)
                name = args[0]
                class_name = self.classes[name]
                for obj in obj_dict.values():
                    if type(obj) == class_name:
                        obj_list.append(str(obj))
            except KeyError:
                print("** class doesn't exist **""")
                return
        print(obj_list)

    def do_update(self, arg):
        """ Update command that updates an instance """
        if arg:
            args = shlex.split(arg)
            if args[0] not in self.classes.keys():
                print("** class doesn't exist **")
                return
            try:
                dic = storage.all()
                obj = dic[args[0] + "." + args[1]]
                self.change_value(obj, args)
                storage.save()
            except KeyError:
                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")
        else:
            print("** class name missing **")

    def show_obj(self, dic, args):
        """Print out a particular object"""
        dic = storage.all()
        obj = dic[args[0] + "." + args[1]]
        print(obj)

    def destroy(self, dic, args):
        """Destroy an object"""
        del dic[args[0] + "." + args[1]]
        storage.save()

    def change_value(self, obj, args):
        """change values of attributes of an object"""
        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        try:
            if hasattr(obj, args[2]):
                value = type(getattr(obj, args[2]))(args[3])
                setattr(obj, args[2], value)
            else:
                setattr(obj, args[2], args[3])
        except TypeError:
            print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
