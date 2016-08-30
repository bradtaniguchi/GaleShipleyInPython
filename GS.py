#!/usr/bin/python3
import sys  # to get command line arguments
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
        self.name = name  # string
        self.male = male  # boolean, not really used
        self.fiance = None

    def addPref(self, list):
        self.pref = list

    def generateRandPref(self, listOfOtherGender):
        self.pref = listOfOtherGender
        random.shuffle(self.pref)  # does inline, returns nothing!
    
    def getPref(self, spacing=8):
        """Utility function, Prints out preference list"""
        for person in self.pref:
            print(person.name.ljust(spacing), end=" ")  # no newline


def main(numberOfCouples, verbose): 
    num = numberOfCouples
    men = []
    women = []
    proposals = 0
    for i in range(0,num):
        men.append(Person("man" + str(i), True))
        women.append(Person("woman" + str(i), False))
    
    # after generating the list of men and women
    # randomly generate the preferences lists for each
    if(verbose): print("========Defining Preferences======")
    for man in men:
        man.generateRandPref(women)
        if(verbose): print(man.name.ljust(10) + " [ ", end="")
        if(verbose): man.getPref()
        if(verbose): print("]")
    for woman in women:
        woman.generateRandPref(men)
        if(verbose): print(woman.name.ljust(10) + " [ ", end="")
        if(verbose): woman.getPref()
        if(verbose): print("]")

    if(verbose): print("========End Preferences===========")
    # now the preferences are done, start propositions
    lonelyMen = list(men)  # men that haven't propsed
    while len(lonelyMen) > 0:  # while there is a man that hasn't proposed
        proposals += 1
        readyMan = lonelyMen.pop(0)  # get man at top of "stack"
        # check preference list....
        crush = readyMan.pref.pop(0)  # pop top woman in "stack"

        #print("debug: " + str(crush.pref.index(readyMan)) + " > " + str(crush.pref.index(crush.fiance)))
        
        # and see if woman is engaged
        if (crush.fiance is None) :  # if woman isn't engaged
            # BECOME engaged (yay)
            crush.fiance = readyMan  # set the man as the fiance!s
            readyMan.fiance = crush  # set the woman as the fiance
            print("DEBUG: " + str(crush.pref.index(readyMan)))
        #TODO: is this object reference comparison
        elif (crush.pref.index(readyMan) > crush.pref.index(crush.fiance)): 
            # according to crush, the pos of our readyMan, is greater than 
            #NOTE: pop removes the LAST item! 
            print("elif")
            Person(crush.fiance).fiance = None  # set the fiance of the fiance's 
            crush.fiance = readyMan # set the man as the fiance's
            readyMan.fiance = checkWoman # set the woman as the fiance

        # crush prefers her current fiance to readyMan
        else:  # here for clarity
            continue
            
    for man in men:
        print("Couple: " + man.name + " <---> " + man.fiance.name)
    for woman in women:
        print("Couple: " + woman.name + " <---> " + woman.fiance.name)
    print("------------------------")
    print(" n = " + str(numberOfCouples))
    n2 = numberOfCouples * numberOfCouples
    print(" n^2 = " + str(n2))
    print("Proposals: " + str(proposals))

if __name__ == '__main__':
    if len(sys.argv) == 1: 
        print("Not enough arguments given!\n" +
              "GS.py [Options] numberOfCouples\n" + 
              "  -v : Verbose - Provides all extra printouts\n")
        sys.exit(1)  # not enough arguments!
    else:
        verbose = False
        numberOfCouples = 0
        for i in range(1, len(sys.argv)):
            arg = sys.argv[i]
            if arg == '-v' or arg == '-V' or arg == '-Verbose':
                verbose = True
                continue
            if i == len(sys.argv)-1:  # occur on the last argument given
                numberOfCouples = int(arg)
                break
        if numberOfCouples <= 0:
            print("You didn't give a correct value for Number of Couples!")
            sys.exit(1)

        if(verbose): print("Program Arguments: " + str(sys.argv))
        main(numberOfCouples,verbose)
