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
            
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# Function to do Quick sort 
def quickSort(arr,low=0,high=-1):
    if high==-1:
        high=len(arr)-1
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)
        
def checkindividual(name):
    if not name in people.keys():
        people[name] = {}
        people[name]['name'] = name
        people[name]['parents'] = []
        people[name]['spouse'] = []
        people[name]['children'] = []
        people[name]['ancestors']=[]

def addPeople( names ):
    #add logic for E name1 name2 or E name1 name2 name3 here

    #check to see if name already exists, if not, add it to the dictionary
    for x in range (1,len(names)):
        if not names[x] in people.keys():
            people[names[x]] = {}
            people[names[x]]['name'] = names[x]
            people[names[x]]['parents'] = []
            people[names[x]]['spouse'] = []
            people[names[x]]['children'] = []
            people[names[x]]['ancestors']=[]

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
    result = 'No \n'
    checkindividual(names[1])
    checkindividual(names[3])

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
        

def returnSiblings( names ):
    checkindividual(names[2])
    # W sibling name1
    l = []

    result = ''
    if not names[2] in people.keys():
        result += '\n'

    personOneParents = people[names[2]]['parents']

    siblings = []
    for i in range(0,len(personOneParents)):
        siblings += people[personOneParents[i]]['children']

    #remove duplicates and names[2] from siblings
    siblings = list(set(siblings))
    if names[2] in siblings:
        siblings.remove(names[2])
    quickSort(siblings)
    if len(siblings)==0:
        result += 'Nobody' + '\n'
    else:
        for value in siblings:
            result += value + '\n'
    
    output.write(result + '\n')



def isunrelated(line):
    name1=line[1]
    name2=line[3]
    checkindividual(name1)
    checkindividual(name2)
    if name1==name2:
        return True
    if (name1 in findancestors(name2)) or (name2 in findancestors(name1)):
        return False
    else:
        for name3 in findancestors(name1):
            if name3 in findancestors(name2):
                return False
    return True
    
def returnunrelated(line):
    name1=line[2]
    checkindividual(name1)
    unrelated=[]
    for name2 in list(people.keys()):
        if isunrelated([0,name2,0,name1]):
            unrelated.append(name2)
    quickSort(unrelated)
    result=''
    if len(unrelated)==0:
        result='Nobody' + '\n'
    else:
        for value in unrelated:
            result += value + '\n'

    output.write(result + '\n')

def ischild(line):
    name1=line[1]
    name2=line[3]
    checkindividual(name1)
    checkindividual(name2)
    if name1 in people[name2]['children']:
        output.write('Yes\n\n')
    else:
        output.write('No\n\n')

def returnchild(line):
    name1=line[2]
    checkindividual(name1)
    children=people[name1]['children']
    quickSort(children)
    result=''
    if len(children)==0:
        result='Nobody' + '\n'
    else:
        for value in children:
            result += value + '\n'

    output.write(result + '\n')


def iscousin(line):
    name1=line[1]
    name2=line[4]
    checkindividual(name1)
    checkindividual(name2)
    cousinnum=int(line[3])
    stack=[]
    stack.append(name1)
    l=[]
    l.append(stack)
    while l!=[] and len(l[0])<cousinnum+2:
        for parent in people[l[0][len(l[0])-1]]['parents']:
            t=l[0].copy()
            t.append(parent)
            l.append(t)
        l.pop(0)
    while l!=[] and len(l[0])<cousinnum*2+3:
        for child in people[l[0][len(l[0])-1]]['children']:
            if child not in l[0]:
                t=l[0].copy()
                t.append(child)
                l.append(t)
        l.pop(0)
    for i in l:
        if (i[len(i)-1]==name2) or (i[len(i)-1] in findancestor(name2)):
            output.write('Yes\n')
            return
    name1=line[4]
    name2=line[1]
    stack=[]
    stack.append(name1)
    l=[]
    l.append(stack)
    while l!=[] and len(l[0])<cousinnum+2:
        for parent in people[l[0][len(l[0])-1]]['parents']:
            t=l[0].copy()
            t.append(parent)
            l.append(t)
        l.pop(0)
    while l!=[] and len(l[0])<cousinnum*2+3:
        for child in people[l[0][len(l[0])-1]]['children']:
            if child not in l[0]:
                t=l[0].copy()
                t.append(child)
                l.append(t)
        l.pop(0)
    for i in l:
        if (i[len(i)-1]==name2) or (i[len(i)-1] in findancestor(name2)):
            output.write('Yes\n')
            return
    output.write('No\n')
    
def returncousin(line):
    name1=line[3]
    checkindividual(name1)
    cousinnum=int(line[2])
    stack=[]
    stack.append(name1)
    l=[]
    l.append(stack)
    cousins=[]
    while l!=[] and len(l[0])<cousinnum+2:
        for parent in people[l[0][len(l[0])-1]]['parents']:
            t=l[0].copy()
            t.append(parent)
            l.append(t)
        l.pop(0)
    while l!=[] and len(l[0])<cousinnum*2+3:
        for child in people[l[0][len(l[0])-1]]['children']:
            if child not in l[0]:
                t=l[0].copy()
                t.append(child)
                l.append(t)
        l.pop(0)
    for i in l:
        stack2=[]
        stack2.append(i[len(i)-1])
        while stack2!=[]:
            for j in people[stack2[0]]['children']:
                stack2.append(j)
            cousins.append(stack2[0])
            stack2.pop(0)
    for ancestor in findancestors(name1):
        stack=[]
        stack.append(ancestor)
        l=[]
        l.append(stack)

        while l!=[] and len(l[0])<cousinnum+2:
            for parent in people[l[0][len(l[0])-1]]['parents']:
                t=l[0].copy()
                t.append(parent)
                l.append(t)
            l.pop(0)
        while l!=[] and len(l[0])<cousinnum*2+3:
            for child in people[l[0][len(l[0])-1]]['children']:
                if child not in l[0]:
                    t=l[0].copy()
                    t.append(child)
                    l.append(t)
            l.pop(0)
        for i in l:
            cousins.append(i[len(i)-1])
    cousins=list(set(cousins))
    quickSort(cousins)
    result=''
    if len(cousins)==0:
        result='Nobody' + '\n'
    else:
        for value in cousins:
            result += value + '\n'
    output.write(result + '\n')
    
if __name__ == '__main__':
    #read text from standard in
    input_method=sys.stdin
    #no need to write into output.txt from commandline
    output=sys.stdout
    #output = open(sys.argv[2], "w")
    empty=True
    for a in input_method:
        a = a.rstrip()
        #changed output into standard out
        #begin processing what is input
        #empty file is allowed
#        if len(a)==0:
#            break
        empty=False
        #separate the test case line by line

        line = a.split(' ')
        if(line[0] == 'E'):
            addPeople(line)
        elif(line[0] == 'X'):
            output.write(a+'\n')
            if line[2] == 'sibling':
                isSibling(line)
            elif line[2] == 'child':
                ischild(line)
            elif line[2] == 'ancestor':
                isancestor(line)
            elif line[2] == 'cousin':
                iscousin(line)
            elif line[2] == 'unrelated':
                if isunrelated(line):
                    output.write('Yes'+ '\n\n')
                else:
                    output.write('No'+ '\n\n')
                    
        elif(line[0] == 'W'):
            output.write(a+ '\n')
            if line[1] == 'sibling':
                returnSiblings(line)
            elif line[1] == 'child':
                returnchild(line)
            elif line[1] == 'ancestor':
                returnancestor(line)
            elif line[1] == 'cousin':
                returncousin(line)
            elif line[1] == 'unrelated':
                returnunrelated(line)

            #myprint( people )
    #output.close()
    if empty:
        output.write('File is Empty!')
    else:
        output.write('\nEnd of File.')
