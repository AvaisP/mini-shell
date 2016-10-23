from cmd2 import Cmd 
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Shell(Cmd):
	
	def preloop(self):
		print 'A Simple python Shell created by Avais and Swapneel.\nUse help or "?" to see list of commands.\nUse help (command name) to for help realted to the command'
		print 'Version 0.1'
		print '==============================================\n\n\t\tStay in the shell\n\n=============================================='

	def do_lf(self, arg):
		'Lists Files in the present directory'
		for f in os.listdir('.'):
			if os.path.isfile(f):
				print f
			else:
				print bcolors.OKBLUE + f + bcolors.ENDC

	def do_exit(self, arg):
		'Exits the shell'
		print 'Thanks for using this amazingly simple shell.'
		return True

	def do_crdr(self, arg):
		'Creates a Directory'
		os.mkdir(arg)
		print 'Directory named {0} created'.format(arg)


shell = Shell()
shell.cmdloop()