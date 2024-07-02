#!/usr/bin/python3
""" A simple command line robo game!"""
import cmd


class RobotGame(cmd.Cmd):
    intro = "Welcome to the Robot Game! Type help or ? to list commands.\n"
    prompt = "(robot) "

    def do_greet(self, line):
        print("Hello! I am your friendly robot.")

    def do_quit(self, line):
        print("Goodbye!")
        return True # this will exit the cmdloop

    def do_track(self, line):
        if not line:
            print("Please provide the product name. Example: track apples")
        else:
            # a simple simulation of tracking info
            print(f"Tracking info for {line}:")
            print("Your product is on the way n' will be delivered in 2 days.")
    
    def default(self, line):
        print(f"Sorry, I don't understand the command: {line}")

    def emptyline(self):
        print("You need to type a command")

    def completedefault(self, text, line, begidx, endidx):
        commands = ['greet', 'quit']
        return [cmd for cmd in commands if cmd.startswith(text)]


if __name__ == '__main__':
    RobotGame().cmdloop()
