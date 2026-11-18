#	fileMover.py
#
#	A utility that can copy, move, and/or rename files. Reads commands from a
#	file to enable numerous operations with a single run. If a destination
#	directory doesn't exist, this program creates it. Any existing files with
#	the same name as the destination file will be overwritten without any
#	prompting.
#
#	Instructions:
#		To use this program, you'll need a command file. Here's an example of
#		a command:
#			Copy
#			C:\Some\Place\file.jpg
#			to
#			C:\Some\Other\Place\aCopyOfFile.jpg
#
#		As you can see, each command is 4 lines. The 1st line contains the
#		operation to perform, which must be either "copy" or "move". The 3rd
#       line is always "to". Capitalization does not matter for these two
#		lines.

#       The 2nd	line is the file to be moved or copied, and the 4th line is
#       the destination to put the file. Note that you can give the
#		destination file a different name if you want.#
#
#		Lines that are just white space are ignored, so feel free to use them
#		to organize your file into sections that are easier to read.
#		
#		Once your command file has been created, you can run the program by
#		giving it the command file as an argument. For example:
#			python fileMover.py example_commands.txt
#
#	If you want to use this utility to move a variety of different files at
#	different times, consider creating a command file and corresponding batch
#	file for each distinct job; that way you can simply run the specific batch
#	file whenever you want without needing to type in filenames each time.
#	There's a simple Windows batch file in this	repository that serves as an
#	example.
#
#	This program currently uses input commands to allow human users to see the
#	results of each run, but if you use this file in an automated context these
#	commands can be removed.
#
import sys
import os
import shutil

################################ Functions ####################################


# Something has gone wrong, abort the program and provide info to user.
def doError(message, exception=None):
	print("ERROR!  The above command was not completed.")
	print()
	print("ERROR DETAILS:")
	print(message)
	if exception != None:
		print(exception)
	else:
		print("Please review instructions in fileMover.py for more information.")
	print()
	print("Cancelling operations from this point. Press Enter to close.")
	trash = input()
	sys.exit()


# We've enough lines for a command, now parse and execute it.
def executeCommand(command):
	verb = command[0].strip().lower()
	source = command[1].strip()
	theWordTo = command[2].strip().lower()
	destination = command[3].strip()
		
	print("EXECUTING:")
	print(verb)
	print(source)
	print(theWordTo)
	print(destination)
	print()
	
	if verb not in {'copy', 'move'}:
		doError('Commands must begin with either "move" or "copy".')
	if theWordTo != "to":
		doError("3rd line of each command should be: TO.")
	
	# make destination folder if it doesn't already exist
	try:
		directoryPath = os.path.dirname(destination)
		os.makedirs(directoryPath, exist_ok=True)
	except Exception as e:
		doError("Received this error when trying to create destination directory:", e)

	# copy the file
	if verb == 'copy':
		try:
			shutil.copyfile(source, destination)
		except Exception as e:
			doError("Received this error when trying to copy file:", e)
	# move the file
	elif verb == 'move':
		try:
			os.replace(source, destination)
			#os.remove(source)
		except Exception as e:
			doError("Received this error when trying to move file:", e)
				


########################## Execution Starts Here ##############################

# Check for command line arguments, and if none, quit.
if len(sys.argv) < 2:
	print("Needs the name of a file containing commands to run.")
	print("Example:")
	print("python fileMover.py fileWithCommands.txt")
	print("Please review instructions in fileMover.py for more information.")
	print("Press Enter to close.")
	trash = input()
	sys.exit()

# first argument should be the name of a file containing commands
userFilename = sys.argv[1]
print()
currentCommand = []
with open (userFilename, 'r') as commandFile:
	for line in commandFile:
		
		if line.isspace():
			continue
		else:
			currentCommand.append(line)
			
			# commands are 4 lines long
			if len(currentCommand) == 4:
				executeCommand(currentCommand)
				currentCommand = []
				
print("Operations successfully completed!  Press Enter to close program.")
trash = input()