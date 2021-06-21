#! /usr/bin/python3

import os

class Setup():
    """A class to represent setup."""
    def __init__(self):
        """Initialize setup attributes."""
        # Getting the path where the programme will stay.
        filename_1 = "setup.txt"
        with open(filename_1, 'r') as path:
            path = str(path.read()).strip()

        self.path = path

        # Assigning the path in main.py.
        filename_2 = 'main.py'
        with open(filename_2, 'r+') as main_py: # r+ does the work of rw
            lines = main_py.readlines()
            for i, line in enumerate(lines):
                if line.startswith('PATH'):
                    lines[i] = lines[i].strip() + ' ' + f"\"{path}\"\n"
            main_py.seek(0)
            for line in lines:
                main_py.write(line)
        main_py.close()

        # Assigning the path in fq.
        filename_3 = 'fq'
        with open(filename_3, 'r+') as fq: # r+ does the work of rw
            lines = fq.readlines()
            for i, line in enumerate(lines):
                if line.startswith('path'):
                    lines[i] = lines[i].strip() + f"\"{path}\"\n"
            fq.seek(0)
            for line in lines:
                fq.write(line)
        fq.close()

    def copy_to_path(self):
        """Copy the files in order to freely run the fq command."""
        path = self.path
        # Copy famous-quotes folder.
        cmd_1 = f"cp -r $(pwd) {path}"
        os.system(cmd_1)

        # Copy fq file.
        cmd_2 = f"cp fq {path}"
        os.system(cmd_2)

if __name__ == '__main__':
    Setup().copy_to_path()
    print("\n\nThe proramme is successfully installed.\n\n")
    # Display the usage.
    os.system("fq -h")
