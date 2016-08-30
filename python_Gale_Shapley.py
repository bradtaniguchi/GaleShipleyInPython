#!/usr/bin/python3
import random  # to generate random preferences

class Person():
    '''
    A person class, defined by their prefernce list, boolean if they are male, 
    their name, and if they are engaged
    :param name: string - name of person
    :param man: boolean - if this person is a male
    '''
    def __init__(self, name, male, prefList=[]):
        if len(prefList) != 0:
            _generateRandPref(prefList)
        else:
            self.pref = []
        self.name = name #string
        self.male = male #boolean, not really used
        self.fiance = None

    def addPref(self, list):
        self.pref = list

    def generateRandPref(self, listOfOtherGender):
        self.pref = listOfOtherGender
        random.shuffle(self.pref)  # does inline, returns nothing!
    

def main():
    #generate a list of 5 men and 5 women
    num = 5
    men = []
    women = []
    for i in range(0,num):        
        men.append(Person("man" + str(i), True))
        women.append(Person("woman" + str(i), False))
    
    # after generating the list of men and women
    # randomly generate the preferences lists for each
    for man in men:
        man.generateRandPref(women)
    for woman in women:
        woman.generateRandPref(men)
    
    print("================")
    #TODO: print out the preference lists here!
    print("================")
    # now the preferences are done, start propositions
    lonelyMen = list(men)  # men that haven't propsed
    while len(lonelyMen) > 0:  # while there is a man that hasn't proposed
        readyMan = lonelyMen.pop(0)  # get man at top of "stack"
        # check preference list....
        crush = readyMan.pref.pop()  # pop top woman in "stack"
        # and see if woman is engaged
        if (crush.fiance is None) :  # if woman isn't engaged
            # BECOME engaged (yay)
            crush.fiance = readyMan  # set the man as the fiance!s
            readyMan.fiance = crush# set the woman as the fiance
        #TODO: is this object reference comparison
        elif (crush.pref.index(readyMan) > crush.pref.index(crush.fiance)): 
            # according to crush, the pos of our readyMan, is greater than 
            #NOTE: pop removes the LAST item! 
            Person(crush.fiance).fiance = None  # set the fiance of the fiance's 
            crush.fiance = readyMan # set the man as the fiance's
            readyMan.fiance = checkWoman # set the woman as the fiance
            
            
        # crush prefers her current fiance to readyMan
        else:  # here for clarity
            continue
            
    # return the set of S of engaged pairs.
    print("Men engaged: " + str(len(men)))
    for man in men:
        print("Fiance for: " + man.name + " " + man.fiance.name)
    for woman in women:
        print("Fiance for: " + woman.name + " " + woman.fiance.name)


if __name__ == '__main__':
    main()
