#!/usr/bin/env python3
import os
import sys
import argparse
from subprocess import check_call, check_output

application = 'autonomouse'
jslibs_dir = os.path.join(application, "static")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument('extra', nargs='*')
    args = parser.parse_args()
    args_dict = {key: value for key, value in
                 [arg.split('=') for arg in args.extra]}
    private_methods = TaskBase().getAvailableMethods()
    tasks = Tasks()
    public_methods = tasks.getAvailableMethods()
    available_methods = [
        method for method in public_methods if method not in private_methods]
    try:
        return getattr(tasks, args.command)(**args_dict)
    except AttributeError:
        print("There is no '" + args.command + "' command.")
        print("Available commands: \n * " + "\n * ".join(available_methods))


class TaskBase():
    """Helper methods, not meant to be called from the cli. """

    def getAvailableMethods(self):
        return [func for func in dir(self) if callable(getattr(self, func))
                and not func.startswith("__")]

    def sudo(self, cmd):
        sudo_cmd = ["sudo"]
        sudo_cmd.extend(cmd)
        return check_output(sudo_cmd)


class Tasks(TaskBase):
    """Tasks meant to be callable from the cli. """

    # Add your methods here, e.g.:
    def noop(self):
        """ Example method"""
        pass

if __name__ == "__main__":
    sys.exit(main())
