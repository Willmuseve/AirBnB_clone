#!/usr/bin/python3
"""Custom airbnb console."""
import json
import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class that creates an interactive session with the prompt."""

    prompt = "(hbnb) "

    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review}

    def do_quit(self, param):
        """Quit the program."""
        return True

    def do_EOF(self, param):
        """Exit the program with an exit message."""
        print("Exiting the session ...bye")
        return True

    def emptyline(self):
        """Handle emptyline input."""
        pass

    def do_create(self, param):
        """Create a new instance of the BaseModel.

        Saves it to the json file
        and prints the id
        """
        param = param.split()
        if not param:
            print("** class name missing **")
        elif param[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_inst = self.classes[param[0]]()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, param):
        """Print the string representation of an instance.

        The representation is based on the class name and id
        """
        param = param.split()
        if not param:
            print("** class name missing **")
        elif param[0] not in self.classes:
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
        """Delete an instance.

        Deletion is based on the class name and id
        and saves the changes into the JSON file
        """
        param = param.split()
        if not param:
            print("** class name missing **")
        elif param[0] not in self.classes:
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
        """Print all string representation of all instances.
        The representation is based or not on the class name
        """
        param = param.split()
        objects = models.storage.all()
        if not param:
            print([str(obj) for obj in objects.values()])
        elif param[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            class_name = param[0]
            for key, obj in objects.items():
                if obj.__class__.__name__ == class_name:
                    print(str(obj))

    def do_update(self, param):
        """Update an instance.

        The update process is based on the class name and id by adding or
        updating attribute(saves the change ubto the JSON file)
        """
        param = param.split()
        if not param:
            print("** class name missing **")
        elif param[0] not in self.classes:
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
            attribute_value = param[3].strip('""')

            try:
                attribute_value = eval(attribute_value)
            except (NameError, SyntaxError):
                pass
            setattr(objects[key], attribute_name, attribute_value)
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
