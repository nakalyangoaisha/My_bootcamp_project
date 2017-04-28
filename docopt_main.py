#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    docopt_main.py create_room <room_type> <room_name>...
    docopt_main.py add_person <name> <position> <accommodate>...
    docopt_main.py print_room <room_name>...
    docopt_main.py print_staff_office_allocations 
    docopt_main.py print_fellow_office_allocations
    docopt_main.py print_fellow_livingspace_allocations
    docopt_main.py (-i | --interactive)
    docopt_main.py (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""

import sys
import cmd
from docopt import docopt, DocoptExit

from app.dojo import Dojo

dojo_instance = Dojo()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class Aisha(cmd.Cmd):
    intro = 'Welcome to my interactive program!' \
            + ' (type help for a list of commands.)'
    prompt = '(my_program) '
    file = None

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_type> <room_name>..."""
        room_type = arg['<room_type>']
        room_name = arg['<room_name>']
        for room_name in room_name:
            dojo_instance.create_room(room_name, room_type)
            if room_type == 'office':
                print('An office called '+ room_name + ' has been created')
            elif room_type == 'livingspace':
                print('A livingspace called ' + room_name + ' has been created')
        print(arg)
    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <name> <position> <accommodate>..."""
        name = arg['<name>']
        position = arg['<position>']
        accommodate = arg['<accommodate>']
        for name in name:
            dojo_instance.add_person(name, position, accommodate)
            if position == 'staff':
                if accommodate == 'Yes':
                    return 'Staff cannot be accommodated'
                elif accommodate == 'No':
                    dojo_instance.allocate_room(name, 'office')
                    print('Staff ' + name + 'has been successfully added')
                    print(name + 'has been allocated office ' + dojo_instance.staff_office_allocations[name])
    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name>..."""


    @docopt_cmd
    def do_print_staff_office_allocations(self, arg):
        """Usage: print_staff_office_allocations"""
        print('These are the staff allocated the respective offices')
        print(dojo_instance.staff_office_allocations)

    @docopt_cmd
    def do_print_fellow_office_allocations(self, arg):
        """Usage: print_fellow_office_allocations"""
        print('These are the names of fellows that have been allocated the respective offices')
        print(dojo_instance.fellow_office_allocations)

    @docopt_cmd
    def do_print_fellow_livingspace_allocations(self, arg):
        """Usage: print_fellow_livingspace_allocations"""
        print('These fellows have allocated the respective livingspaces')
        print(dojo_instance.fellow_livingspace_allocations)

    @docopt_cmd
    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    Aisha().cmdloop()

print(opt)
