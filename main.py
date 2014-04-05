import sys
import os

from analizer import *

current_directory = ""
if (len(sys.argv) == 1):
    print "No arguments found!"
    current_directory = os.path.realpath(os.curdir)
else:
    current_directory = os.path.realpath(sys.argv[1])

print ("Program will try to analyze \"" +
       current_directory + "\" directory")
analize_dir(current_directory)
print "End of program"
quit()
