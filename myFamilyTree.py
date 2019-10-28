#Prog;l=ramming Assignment #2
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
   print( names) 
   for x in range (1,len(names)):
         if not names[x] in people.keys():
            people[names[x]] = {}
            people[names[x]]['name'] = names[x]
            people[names[x]]['parents'] = []
            people[names[x]]['spouse'] = []
            people[names[x]]['children'] = []
            people[names[x]]['ancestors'] = []

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

def isSibling( names ):
    # X name1 sibling name2
    output.write('X ' + names[1] + ' sibling ' + names[3] + '\n')
    result = 'No \n'

    if not names[1] in people.keys() or not names[3] in people.keys():
        result = 'No \n'

    else:
        personOneParents = people[names[1]]['parents']
        personTwoParents = people[names[3]]['parents']
     
        for x in personOneParents: 
            for y in personTwoParents:
            	 if x == y:
	             	 result = 'Yes \n'

    output.write(result + '\n')

def isAncestorHelper(names):
     output.write('X ' + names[1] + ' ancestor' + names[3] + '\n')
     ancestor = people[names[1]]
     descendant = people[names[3]]	
     isAncestor(ancestor, descendant)


def isAncestor( ancestor , person ):
    #X name1 ancestor name 3
    result = 'No \n'
    if person['parents'] == []:
 	return False
    else:
	if person['parents'][0] == ancestor:
		return True
	else:
	    ancestorLevelUp = person['parents'][0]
	    resultSideOne = isAncestor(ancestorLevelUp, person)
	    if  resultSideOne == True:
		 result = 'Yes \n'
		 print(ancestor['name'])
		 return True
	    else:
		 if person['parents'][1] == ancestor :
                    result = 'Yes \n' 
		    print(ancestor['name'])   
		    return True
		 else:
		     ancestorLevelUp = person['parents'][1]
                     resultSideTwo = isAncestor(ancestorLevelUp, person)
 		     if  resultSideTwo == True:
                         result = 'Yes \n'
		         return True
		     else:
			 result = 'No \n'
			 return False
# print('here \n')

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
                elif(line[0] == 'X'):
                    if line[2] == 'sibling':
                        isSibling(line)
                    if line[2] == 'ancestor':
                        isAncestorHelper(line)
                elif(line[0] == 'W'):
                    print(line)                     #replace with method calls

        #myprint( people )
        output.close()
