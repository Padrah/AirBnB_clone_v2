#!/usr/bin/python3

"""An interactive shell?"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)  '

    def do_EOF(self, line):
        print("")
        return True

    def do_quit(self, line):
        print("Good Bye!")
        return True

    def help_quit(self):
        print('\n'.join(["Quit command to exit the program"]))

    def emptyline(self):
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
