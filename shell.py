from cmd import Cmd 
import os


class Shell(Cmd):
	
	def do_lf(self, arg):
		'Lists Files in the present directory'
		for f in os.listdir('.'):
			print f

shell = Shell()
shell.cmdloop()