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
            contents = test.readlines()
            contents = [line.strip('\n') for line in contents]
            test.close()

        #write into output.txt from commandline
        output = open(sys.argv[2], "w")

        if(len(contents) == 0):
            output.write('File is Empty!')
            sys.exit()
        else:
            #deal with input
            for line in contents:
                #input = line.split('')
                output.write(line + '\n')

        #program EOF
        output.close()
