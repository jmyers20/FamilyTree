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
            #separate the test case line by line
            for line in contents:
                line = line.split(' ')
                if(line[0] == 'E'):
                    print(line)                     #replace with method calls
                elif(line[0] == 'W'):
                    print(line)                     #replace with method calls
                elif(line[0] == 'X'):
                    print(line)                     #replace with method calls

                #output.write(line + '\n')

        output.close()
