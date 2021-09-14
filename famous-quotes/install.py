#! /usr/bin/python3

import os

class Setup():
    """A class to represent setup."""
    def __init__(self):
        """Initialize setup attributes."""
        PATH_values = ["/usr/local/bin", "/usr/bin", "/bin", "/usr/sbin", "/sbin"]
        try:
            self.PATH = os.environ.get("PATH") # get $PATH variable
        except:
            print("Access to PATH variable is denied.")
        else:
            # Assigning one of $PATH value to our self.PATH
            for value in PATH_values:
                if value in self.PATH:
                    self.PATH = value
                    break
                else:
                    print("PATH variable is not defined.")
                    exit()

        # Assigning the PATH in main.py.
        with open("main.py", 'r+') as main_py: # r+ does the work of rw
            lines = main_py.readlines()
            for i, line in enumerate(lines):
                if line.startswith('PATH'):
                    lines[i] = lines[i].strip() + ' ' + f"\"{self.PATH}\"\n"
            main_py.seek(0)
            for line in lines:
                main_py.write(line)
        main_py.close()

        # Assigning the PATH in fq.
        with open("fq", 'r+') as fq: # r+ does the work of rw
            lines = fq.readlines()
            for i, line in enumerate(lines):
                if line.startswith('path'):
                    lines[i] = lines[i].strip() + f"\"{self.PATH}\"\n"
            fq.seek(0)
            for line in lines:
                fq.write(line)
        fq.close()

    def copy_to_PATH(self):
        """Copy the files to $PATH in order to freely run the fq command."""
        # Setup the permissions.
        os.system("chmod 744 -R $(pwd)")
        # Copy famous-quotes folder.
        os.system(f"cp -r $(pwd) {self.PATH}")
        # Copy fq file.
        os.system(f"cp fq {self.PATH}")

if __name__ == "__main__":
    Setup().copy_to_PATH()
    print("\n\nThe proramme is successfully installed.\n\n")
    # Display the usage.
    os.system("fq -h")
