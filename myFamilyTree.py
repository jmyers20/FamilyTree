#Programming Assignment #2
#$> python3 myFamilyTree.py test1.txt output1.txt

import sys

people = {}

#this method can be used to iterate through a nested dictionary and print its contents
def myprint( d ):
  for k, v in d.items():
    if isinstance(v, dict):
      myprint(v)
    else:
      print("{0} : {1}".format(k, v))

def addPeople( names ):
    #add logic for E name1 name2 or E name1 name2 name3 here

    #check to see if name already exists, if not, add it to the dictionary
    for x in range (1,len(names)):
        if not names[x] in people.keys():
            people[names[x]] = {}
            people[names[x]]['name'] = names[x]
            people[names[x]]['parents'] = []
            people[names[x]]['siblings'] = []
            people[names[x]]['spouse'] = []
            people[names[x]]['children'] = []

    if len(names) == 3:
        #add each person to each other's spouses
        if not names[2] in people[names[1]]['spouse']:
            people[names[1]]['spouse'].append(names[2])
            people[names[2]]['spouse'].append(names[1])

    if len(names) == 4:
        #add each person to each other's spouses
        if not names[2] in people[names[1]]['spouse']:
            people[names[1]]['spouse'].append(names[2])
            people[names[2]]['spouse'].append(names[1])

        #add kid to names[1] and names[2]
        people[names[1]]['children'].append(names[3])
        people[names[2]]['children'].append(names[3])

        #add parents to names[3]
        people[names[3]]['parents'].append(names[1])
        people[names[3]]['parents'].append(names[2])

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

        #begin processing what is input
        if(len(contents) == 0):
            output.write('File is Empty!')
            sys.exit()
        else:
            #separate the test case line by line
            for line in contents:
                line = line.split(' ')
                if(line[0] == 'E'):
                    addPeople(line)
                elif(line[0] == 'W'):
                    print(line)                     #replace with method calls
                elif(line[0] == 'X'):
                    print(line)                     #replace with method calls

                #output.write(line + '\n')

        myprint( people )
        output.close()
