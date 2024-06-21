import os
import sys
print (os.listdir(sys.argv[1]))
print ('Total:',len(os.listdir(sys.argv[1])))