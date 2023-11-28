import os
import datetime

# Pathway to folder I want to look through.

rootdir = os.getcwd()

# Pathway to file that is collecting the TODO list.
text_file_location = rootdir + "/README.md"

# Opens and writes the TODO.txt file.
README_file = open(text_file_location, "w")

print("working")

print(text_file_location)


for file in sorted(os.listdir()):
    slug = False
    print(file)
    if str(file).endswith(".md") and str(file) != "README.md":
        print(file)
        print("working in files with .md extension")
        open_file = open(rootdir + "/" + file, "r")
        print(file)
        for line in open_file:
            if line.startswith("---"):
                if slug == False:
                    slug = True
                    continue
                else:
                    slug = False
            if not slug:
                README_file.write(line)
        # Closes open_file
        open_file.close()


# end of all for loops
# Prints the last date modified for convenience.
# README_file.write("Last modified: " + str(datetime.datetime.now()))
# Closes the TODO_file
README_file.close()
