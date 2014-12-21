class CommandParser():

    def __init__(self):
        self.__commands = {}

    def add_command(self, name, function):
        self.__commands[name] = function

    def parse_arguments(self, arguments):
        parsed_arguments = []
        for arg in arguments:
            if arg.isdigit():
                parsed_arguments.append(float(arg) if '.' in arg else int(arg))
            else:
                parsed_arguments.append(arg)
        return parsed_arguments

    def execute(self, user_input):
        userinput = user_input.replace('(', '; ').replace(')', '; ').replace(', ', '; ').split('; ')
        userinput = list(filter(None, userinput))

        command = userinput[0]
        arguments = self.parse_arguments(userinput[1:])
        try:
            return self.__commands[command](*arguments)
        except KeyError:
            return "No such command"
