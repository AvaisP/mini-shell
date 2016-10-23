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
	prompt = ">$"

	def preloop(self):
		print 'A Simple python Shell created by Avais and Swapneel.\nUse help or "?" to see list of commands.\nUse help (command name) for help realted to the command'
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
		print bcolors.BOLD + 'Directory named {0} created'.format(arg) + bcolors.ENDC

	def do_rmdr(self, arg):
		'Removes a Directory'
		os.rmdir(arg)
		print bcolors.FAIL +'Directory named {0} deleted'.format(arg) + bcolors.ENDC

	def do_rnm(self, arg):
		'Renames a directory or file'
		params = arg.split(' ')
		#print params
		os.rename(params[0], params[1])
		print bcolors.OKGREEN + '{0} changed to {1}'.format(params[0],params[1]) + bcolors.ENDC

	def do_cd(self, arg):
		'Changes the current working directory'
		params = arg.split(' ')
		os.chdir(os.path.abspath(os.getcwd()) + '/' + params[0])
		print "Changed the current working directory to " + bcolors.BOLD + os.getcwd() + bcolors.ENDC 

	def do_cwd(self, arg):
		'Shows the current working directory'
		print os.getcwd()

	def do_touch(self, arg):
		'Creates a new file'
		os.mknod(arg)
		print bcolors.BOLD + "Created a file named {0}".format(arg) + bcolors.ENDC

	def do_rem(self, arg):
		'Removes file'
		os.remove(arg)
		print bcolors.FAIL + "Deleted {0}".format(arg) + bcolors.ENDC

	def do_append(self, arg):
		'Appends to a file\nappend file_name text_to_append'
		params = arg.split(' ')
		print params[0]
		stri = ""
		for x in params[1:]:
			stri += x + " "
		with open(params[0],"a") as file:
			file.write(stri)

shell = Shell()
shell.cmdloop()