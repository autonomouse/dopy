#!/usr/bin/env python3
import os
import sys
import argparse
from subprocess import check_call, check_output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument('extra', nargs='*')
    args = parser.parse_args()

    args_list = []
    args_dict = {}
    for arg in args.extra:
        if '=' in arg:
            key, value = arg.split('=')
            args_dict[key] = value
        else:
            args_list.append(arg)
    private_methods = TaskBase().getAvailableMethods()
    tasks = Tasks()
    public_methods = tasks.getAvailableMethods()
    available_methods = [
        method for method in public_methods if method not in private_methods]
    try:
        method = getattr(tasks, args.command)
    except AttributeError:
        print("There is no '" + args.command + "' command.")
        print("Available commands: \n * " + "\n * ".join(available_methods))
    method(*args_list, **args_dict)


class TaskBase():
    """Helper methods, not meant to be called from the cli. """

    def getAvailableMethods(self):
        return [func for func in dir(self) if callable(getattr(self, func))
                and not func.startswith("__")]

    def sudo(self, cmd):
        sudo_cmd = ["sudo"]
        sudo_cmd.extend(cmd)
        return check_output(sudo_cmd)

    def mkdir_p(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)


class Tasks(TaskBase):
    """Tasks meant to be callable from the cli. """

    # Add your methods here, e.g.:
    def noop(self):
        """ Example method"""
        pass

    '''
    def db(self, action):
        """ Example of a task with sub-tasks ("actions"). """

        switch = {
            "do_thing_1": self.method1,
            "do_thing_2": self.method2,
            "do_thing_3": self.method3,
        }
        if action not in switch.keys():
            msg = "'{}' is not a recognised db action. Actions are: {}"
            raise Exception(msg.format(action, ", ".join(switch.keys())))
        switch.get(action)()
    '''


if __name__ == "__main__":
    sys.exit(main())
