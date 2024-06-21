import os
import sys
if len(sys.argv) > 1:
    if os.path.isfile(sys.argv[1]):
       print ("It's file")
    elif os.path.isdir(sys.argv[1]):
        print ("It's dir")
    else:
        print ("Not exist") 
else:
    print("There is nothing to check")