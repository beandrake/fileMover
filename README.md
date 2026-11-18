# fileMover
A simple Python utility to copy, move, and rename any number of files on demand.

## Windows Instructions ##:
1. You'll need [git](https://git-scm.com/), which will allow you to make a local clone of this repository via your [preferred method](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

2. You'll also need [Python](https://www.python.org/downloads/).

3. Create a command file that contains the instructions for which files to copy and move. There's an example command file in the `example` directory named `exampleCommands.txt`, so use that as a reference. You can also read more detailed instructions about how command files need to be structured at the top of `fileMover.py`.

3. Once you have a command file, you can run the program on the command line by passing the command file as an argument:

       python apiPaginate.py MY_COMMAND_FILE.txt

If you end up using this program frequently, it might be convenient to make a batch file; that way you can run the program with a single click without needing to type any of that command line stuff. There's an example of such a batch in the `example` directory named `exampleBatch.bat`.
