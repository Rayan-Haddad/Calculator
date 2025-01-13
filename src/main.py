import cmd
import os
import argparse
from argparse import Namespace
import rich
from rich import print
import datetime

from algebra.factorial import factorial
from algebra.prime import prime
from algebra.sprime import sprime
from algebra.friendsNumbers import friends
from algebra.pgcd import pgcd
from algebra.perfect import perfect

from Source.utilities.YamlUtils import editYaml
from utilities.SQLiteUtils import deleteDefinition
from utilities.SQLiteUtils import addDefinition
from utilities.SQLiteUtils import recreate
from utilities.SQLiteUtils import ChangeDefinition
from utilities.SQLiteUtils import showDefinition

config = "config.yaml"

class MathTerminal(cmd.Cmd):
    intro = 'Hello and welcom to the math calculator project project!'
    prompt = '(MC)>> '  

    def do_calc(self, args):
        ...

    def do_is(self, args):
        parser = argparse.ArgumentParser(prog="Is", description="Funcs that reuturn boolean")
        parser.add_argument("Type")
        parser.add_argument("Number", type=int)
        if args.startswith('Friends') or args.startswith('friends'):
            parser.add_argument("Argument1", type=int, help="First argument for friends")
        arg: Namespace = parser.parse_args(args.split())
        if arg.Type == "prime":
            print(prime(arg.Number))
        elif arg.Type in ["sprime", "semi-prime","semi_prime"]:
            print(sprime(arg.Number))
        elif arg.Type in ["Friends", "friends"]:
            if hasattr(arg, 'Argument1'):
                print(friends(arg.Number, arg.Argument1))
        elif arg.Type in ["perfect", "Perfect"]:
            print(perfect(arg.Number))

    def do_set(self, args):
        parser = argparse.ArgumentParser(
            prog="set settings",
            description="Change settings in the config.yaml file"
        )
        parser.add_argument("head")
        parser.add_argument("key")
        parser.add_argument("value")
        arg: Namespace = parser.parse_args(args.split())
        editYaml(config,arg.head, arg.key, arg.value)

    def do_pgcd(self, args):
        parser = argparse.ArgumentParser(prog="Pgcd", description="nothing for now")
        parser.add_argument("FirstNumber", type=int)
        parser.add_argument("SecondNumber", type=int)
        arg: Namespace = parser.parse_args(args.split())
        print(pgcd(arg.FirstNumber, arg.SecondNumber))

    def do_define(self, args):
        ...

    def do_factorial(self, args):
        parser = argparse.ArgumentParser(
            prog="Factorial calculation",
            description="Factorial calculator",
        )
        parser.add_argument("Number",type=int)
        arg: Namespace = parser.parse_args(args.split())
        print(factorial(arg.Number))

    def do_exit(self, args):
            exit()

    def do_hello(self, args):
        os.system("echo Hello and welcome to the math tool, type help for more!")

    def cmdloop(self, intro=None):
        try:
            super().cmdloop(intro)
        except KeyboardInterrupt:
            print("\nGoodbye")

if __name__ == '__main__':
    terminal = MathTerminal()
    terminal.cmdloop('Starting...')