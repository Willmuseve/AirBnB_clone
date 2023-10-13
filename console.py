#!/usr/bin/python3
"""Console module."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class definition which creates an interactive session with the.

    console.
    """

    prompt = "(hbnb) "

    def do_quit(self, param):
        """Quit the program anf exits."""
        return True

    def do_EOF(self, param):
        """Also quits the program."""
        print("Exiting the program")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
