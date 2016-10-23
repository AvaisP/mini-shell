from cmd2 import Cmd 
import os


class Shell(Cmd):
	
	def preloop(self):
		print 'A Simple python Shell created by Avais and Swapneel.\nUse help or "?" to see list of commands.\nUse help (command name) to for help realted to the command'
		print 'Version 0.1'
		print '==============================================\n\n\t\tStay in the shell\n\n=============================================='

	def do_lf(self, arg):
		'Lists Files in the present directory'
		for f in os.listdir('.'):
			print f

	def do_exit(self, arg):
		'Exits the shell'
		print 'Thanks for using this amazingly simple shell.'
		return True


shell = Shell()
shell.cmdloop()