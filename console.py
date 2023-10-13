#!usr/bin/python3
import json
import cmd
import models
from models import *


class HBNBCommand(cmd.Cmd):
    """class definition which creates an interactive section with the prompt"""

    prompt = "(hbnb) "

    def do_quit(self, param):
        """Quits the program"""
        return True

    def do_EOF(self, param):
        """Exits the program with an exit message"""

        print("Exiting the session ...bye")
        return True

    def emptyline(self):
        pass

    def do_create(self, param):
        """Creates a new instance of the BaseModel, saves it to the json file
        and prints the id"""

        if not param:
            print("** class name missing **")
        elif param not in models.classes:
            print("** class doesn't exist **")
        else:
            new_inst = models.classes[param]()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, param):
        """prints the string representration of an instance based on the
        class name and id"""

        param = param.split()
        if not param:
            print("** class name missing **")
        elif param[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(param) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            key = "{}.{}".format(param[0], param[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, param):
        """Deletes an instance based on the class name and id
        and saves the changes into the JSON file"""

        param = param.split()
        if not param:
            print("** class name missing **")
        elif param[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(param) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            key = "{}.{}".format(param[0], param[1])
            if key in objects:
                del objects[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, param):
        """Prints all string representation of all instances
        based or not on the class name"""

        param = param.split()
        objects = models.storage.all()
        if not param:
            print([str(obj) for obj in objects.values()])
        elif param[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in objects.items() if\
                 key.split('.')[0] == param[0]])

    def do_update(self, param):
        """Updates an instance based on the class name and id by adding or
        updating attribute(saves the change ubto the JSON file)"""

        param = param.split()
        if not param:
            print("** class name missing **")
        elif param[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(param) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            key = "{}.{}".format(param[0], param[1])
            if key not in objects:
                print("** no instance found **")
                return
            if len(param) < 3:
                print("** attribute name missing **")
                return
            if len(param) < 4:
                print("** value missing **")
                return
            attribute_name = param[2]
            attribute_value = param[3]

            try:
                attribute_value = eval(attribute_value)
            except (NameError, SyntaxError):
                pass
            setattr(objects[key], attribute_name, attribute_value)
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
