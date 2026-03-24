import cmd
import sys

class LunMoonShell(cmd.Cmd):
    intro = 'Welcome to the LunMoon interactive shell. Type ajuda for help.'
    prompt = '(LunMoon) '

    def do_ajuda(self, arg):
        """
        Display help information for available commands.
        """
        print('Available commands: ajuda, limpar, historico, sair')

    def do_limpar(self, arg):
        """
        Clear the terminal screen.
        """
        print('\033[H\033[J')

    def do_historico(self, arg):
        """
        Display command history.
        """
        print('Command history feature not implemented yet.')

    def do_sair(self, arg):
        """
        Exit the LunMoon shell.
        """
        print('Exiting LunMoon shell.')
        sys.exit()

    def default(self, line):
        """
        Execute LunMoon commands as typed by the user.
        """
        try:
            exec(line)
        except Exception as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    LunMoonShell().cmdloop()