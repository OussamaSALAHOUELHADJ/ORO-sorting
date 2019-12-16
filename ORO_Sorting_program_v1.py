# -*- coding: UTF-8 -*-
print """
Hello My friend! I'm ORO🦉 The Sorting Bot... Nice to meet you!
I'm here to help you ordering as many numbers as you want in Ascending or Descending way! with some other adds.
>>> How to use:
- the app is asking you to enter a number, so enter it then hit "Enter" and so on...
- if you are finished enter the word "end" in any type you want (END/End...) even we accept einde if you are speaking "Dutch" 🍺🇩🇪
- Then you'll understand every thing that i'll ask you
Enjoy! and don't forget to send us your oppinion. """

Test2 = True

Ends = ["End", "END", "end", "einde"]
Nos = ["n", "N", "no", "No", "NO"]
Yess = ["y", "Y", "yes", "Yes", "YES"]


def ordering(List, newList):
    for i in range(0,len(List)):
        firstInList = List[0]
        compVar = firstInList

        for j in List:
            if compVar < j:
                compVar = j

        List.remove(compVar)
        newList.append(compVar)
    #return newList, inputList


while Test2 == True:
    inputList = []
    newList = []
    Test1 = True
    Test3 = True
    Test4 = True
    rep = True
    print "Please enter a Number: "

    while rep == True:
        inputNum = raw_input("> ")
        if inputNum in Ends:

            print "\nAlright, Your numbers list is: "
            print inputList
            print "\nYour list have %i numbers" % len(inputList)
            rep = False

        else:
            if float(inputNum) in inputList:
                print "You Already Entred %f" % float(inputNum)
            else:
                inputList.append(float(inputNum))
                print "Number %f was stored!" % float(inputNum)

    ordering(inputList, newList)
    w = newList[::-1]

    while Test1 == True:
        Test1 = False
        print """\nPlease! Choose the type of sorting, Enter a number:
        \t1. for Ascending.
        \t2. for Descending.
        \t3. for Top N numbers (Ascending).
        \t4. for Top N numbers (Descending).
        """
        chosenType = raw_input("> ")

        if chosenType == "1":

            print newList

        elif chosenType == "2":

            print newList[::-1]

        elif chosenType == "3":

            print "Please enter the first N number you want to see"
            q = int(raw_input("> "))
            print newList[0: q: 1]

        elif chosenType == "4":

            print "Please enter the Last N number you want to see"
            q = int(raw_input("> "))
            print w[0: q: 1]

        else:
            print "Error: Enter a valid Order"
            Test1 = True

    while Test3 == True:
        print "Do you want to do another ordering? y/n"
        answer = raw_input("> ")
        if answer in Nos:
            Test2 = False
            Test3 = False
        elif answer in Yess:
            Test3 = False
        else:
            print "Error: put a valid answer"

print """\tThanks For Using ORO🦉, GoodBye!
ORO - Version 1.0.1
All Rights Reserved Oussama SALAHOUELHADJ December 2019 © """
