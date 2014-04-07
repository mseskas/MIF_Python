import sys
import os

from analizer import analizer

current_directory = ""
if (len(sys.argv) == 1):
    print "No arguments found!"
    # set current directory as work directory
    current_directory = os.path.realpath(os.curdir)
else:
    current_directory = os.path.realpath(sys.argv[1])

print ("Program will try to analyze \"" +
       current_directory + "\" directory")
analize_tool = analizer(current_directory)
analize_tool.analize_dir()
print "End of program"
quit()
