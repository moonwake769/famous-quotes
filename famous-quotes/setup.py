#! /usr/bin/python3

import os

class Setup():
    """A class to represent setup."""
    def __init__(self):
        """Initialize setup attributes."""
        # Getting the path where the programme will stay.
        #filename_1 = "path.txt"
        #with open(filename_1, 'r') as path:
        #    path = str(path.read()).strip()
        # Defining list of $PATH values.
        PATH_values = ["/usr/local/bin", "/usr/bin", "/bin", "/usr/sbin", "/sbin"]

        try:
            self.path = os.environ.get("PATH") # get $PATH variable
        except:
            print("Access to PATH variable is denied.")
        else:
            # Assigning one of $PATH value to our self.PATH
            for value in PATH_values:
                if value in self.path:
                    self.path = value
                    break
                else:
                    print("PATH variable is not defined.")
                    exit()
        

        # Assigning the path in main.py.
        filename_2 = 'main.py'
        with open(filename_2, 'r+') as main_py: # r+ does the work of rw
            lines = main_py.readlines()
            for i, line in enumerate(lines):
                if line.startswith('PATH'):
                    lines[i] = lines[i].strip() + ' ' + f"\"{self.path}\"\n"
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
                    lines[i] = lines[i].strip() + f"\"{self.path}\"\n"
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
