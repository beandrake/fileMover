REM Any line that starts with REM is a comment.

REM Change the current working directory to be one level up,
REM since that's where the python file is.
cd..

REM Run the utility while telling it where to find the command file.
python fileMover.py example\exampleCommands.txt