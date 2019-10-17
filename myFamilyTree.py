#Programming Assignment #2
#$> python3 myFamilyTree.py test1.txt output1.txt

import re
import sys

if __name__ == '__main__':
    if(len(sys.argv) != 3):
        print('\nPlease follow the execution format:')
        print('$> python3 myFamilyTree.py test1.txt output1.txt')
    else:
        #read from test.txt from commandline
        with open(sys.argv[1], 'r') as test:
            contents = test.read()
            test.close()

        #write into output.txt from commandline
        with open(sys.argv[2], 'w') as output:
            output.write(contents)
            output.close()
