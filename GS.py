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
    def __init__(self, name, male):
        self.pref = []
        self.name = name  # string
        self.male = male  # boolean, not really used
        self.fiance = None
        self.ugly = None  # the person this person finds the least attractive

    def generateRandPref(self, listOfOtherGender):
        self.pref = list(listOfOtherGender)
        random.shuffle(self.pref)  # does inline, returns nothing!
        self.ugly = self.pref[len(self.pref)-1]  # get the least attractive person
        print("     TEST: " + self.name + "DOESN'T LIKE: " + self.ugly.name + "\n\n")

    def getPref(self, spacing=8):
        """Utility function, Prints out preference list"""
        for person in self.pref:
            print(person.name.ljust(spacing), end=" ")  # no newline

def main(numberOfCouples, verbose): 
    num = numberOfCouples
    men = []
    women = []
    proposals = 0  # when man approaches woman
    rejections = 0  # when man is rejected upton approach
    breakups = 0  # when woman breaks up the engagement, to be with a "better man"
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
    if(verbose): print("========Start Engagements=========")
    while len(lonelyMen) > 0:  # while there is a man that hasn't proposed
        proposals += 1
        readyMan = lonelyMen.pop(0)  # get man at top of "stack"
        if(verbose): print(readyMan.name + " is looking for a fiance...") 
        crush = readyMan.pref.pop(0)  # pop top woman in "stack"
        if(verbose): print(" " + readyMan.name + " is proposing to: " + crush.name)
        # and see if woman is engaged
        if (crush.fiance is None) :  # if woman isn't engaged
            if(verbose): print("  " + readyMan.name + " and " + crush.name + " got engaged")
            crush.fiance = readyMan  # set the man as the fiance!s
            readyMan.fiance = crush  # set the woman as the fiance
        #elif (crush.pref.index(readyMan) > crush.pref.index(crush.fiance)): 
        else: # w is currently engaged with someone else
            otherMan = crush.fiance
            if (crush.pref.index(readyMan) > crush.pref.index(otherMan)):
                if(verbose): print(" " + readyMan.name + " got rejected by " + crush.name)
                lonelyMen.append(readyMan)  # no longer ready, push to top of stack
                rejections += 1
            else:  # our readyMan is liked BETTER
                if(verbose): print("  " + readyMan.name + " is liked better than " + otherMan.name + " ")
                breakups += 1
                otherMan.fiance = None
                lonelyMen.append(otherMan)  # no longer ready, add back to list
                crush.fiance = readyMan
                readyMan.fiance = crush
        if(verbose): print("")
    if(verbose): print("==========End Engagements=========")
    for man in men:
        print(("Couple: " + man.name + " <---> " + man.fiance.name), end="") 
        if(man.ugly is man.fiance):
            print(" | " + man.name + " got their least desirable match! " + man.ugly.name ,end="")
        print("")
    print("\n------------------------")
    print("Couples(n) = " + str(numberOfCouples))
    print("Total proposals: " + str(proposals))
    print("Rejections: " + str(rejections))
    print("Breakups: " + str(breakups))
    print("")
    print("Big O:")
    n2 = numberOfCouples * numberOfCouples
    print(" n^2 = " + str(n2))
    print("Full Algorithm analysis:")
    print("  n^2-n+1 where n = " + str(numberOfCouples))
    fullAlgo = (numberOfCouples * numberOfCouples)-numberOfCouples+1
    print("  Algorithm gives max worstcase:(" + str(fullAlgo) + ")")

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
