#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd()):
    """ class definition which creates an interactive session with the
    console """

    prompt = "(hbnb) "

    def do_quit(self, param):
        """quits the program anf exits """
        return True

    def do_EOF(self, param):
        """also quits the program"""
        print("Exiting the program")
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
