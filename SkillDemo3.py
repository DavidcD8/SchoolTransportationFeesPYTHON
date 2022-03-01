
#Author: David Cuevas Diaz
#Date:   3/14/2021


#this function is used to process the calculations of the transportation for students.
def processtransportcost( ):
    loopForFirstLevelStudentKm = True
    loopForSecondLevelStudentKm = True
    loopForFirstLevelStudents = True
    loopForSecondLevelStudents = True
    firstlevelstudentsnumber = 0
    secondlevelstudentsnumber = 0
    totaltransportcost = 0
    firstLevelfamilyAllowance = 390
    secondLevelfamilyAllowance = 940
    firstLevelMinKm = 3.2
    secondLevelMinkm = 4.8

    #this loop will read in the number of students for first level
    while loopForFirstLevelStudents == True:
        try:
            firstlevelstudentsnumber = int(input("Enter Number of First Level Students "))

            if firstlevelstudentsnumber >= 0:
                loopForFirstLevelStudents = False
            elif (firstlevelstudentsnumber < 0):
                print("You must enter a Valid Number")
        except ValueError:
            print("You must enter a Valid Number")
    # this loop will read in the km for first level students
    while loopForFirstLevelStudentKm:
        try:
            firstLevelstudentsKm = float(input("Enter First Level students Km or -1 to finish "))
            if firstLevelstudentsKm < firstLevelMinKm and firstLevelstudentsKm > 0:
                firstlevelstudentsnumber -= 1
                print("Student do not Qualify for subsidised Transport ")
            if firstLevelstudentsKm < -1:
                print("You must enter a Valid Number ")
            elif firstLevelstudentsKm == -1:
                loopForFirstLevelStudentKm = False
        except ValueError:
            print("You must enter a Valid Number ")
            break
    # this loop will read in the number of students for second level
    while loopForSecondLevelStudents == True:
        try:
            secondlevelstudentsnumber = int(input("Enter Number of Second Level Students "))
            if secondlevelstudentsnumber >= 0:
                loopForSecondLevelStudents = False
            elif (secondlevelstudentsnumber < 0):
                print("You must enter a Valid Number ")
        except ValueError:
            print("You must enter a Valid Number ")
        # this loop will read in the km for second level students
        while loopForSecondLevelStudentKm:
            try:
                secondLevelstudentsKm = float(input("Enter Second Level students Km or -1 to finish "))
                if secondLevelstudentsKm < secondLevelMinkm and secondLevelstudentsKm > 0:
                    secondlevelstudentsnumber -= 1
                    print("Student do not Qualify for subsidised Transport ")
                if secondLevelstudentsKm < -1:
                    print("You must enter a Valid Number ")
                elif secondLevelstudentsKm == -1:
                    loopForSecondLevelStudentKm = False
            except ValueError:
                print("You must enter a Valid Number ")

        #thi block of code will calculate the total owed and display it together with the savings if there is any
        if firstlevelstudentsnumber <= 2 and secondlevelstudentsnumber <= 2:
              totaltransportcost = firstlevelstudentsnumber * 100 + secondlevelstudentsnumber * 350
              print("The Amount Due is ",totaltransportcost)
              return

        elif firstlevelstudentsnumber >=3 and secondlevelstudentsnumber >=3:
            firstlevelstudentsnumber -= 2
            secondlevelstudentsnumber -= 2
            totaltransportcost = firstlevelstudentsnumber * 80 + 200 + secondlevelstudentsnumber * 300 + 700
            savings = totaltransportcost - secondLevelfamilyAllowance
            print("The Amount Due is ", secondLevelfamilyAllowance, "You are saving", savings)
            return

        elif firstlevelstudentsnumber >0 and secondlevelstudentsnumber >=3:
            firstlevelstudentsnumber -= 2
            secondlevelstudentsnumber -= 2
            totaltransportcost = firstlevelstudentsnumber * 80 + 200 + secondlevelstudentsnumber * 300 + 700
            savings = totaltransportcost - secondLevelfamilyAllowance
            print("The Amount Due is ", secondLevelfamilyAllowance, "You are saving", savings)
            return

        if firstlevelstudentsnumber > 2 and firstlevelstudentsnumber <= 4:
            firstlevelstudentsnumber -= 2
            totaltransportcost = firstlevelstudentsnumber * 80 + 200
            print("The Amount Due is ",totaltransportcost)
            return

        elif firstlevelstudentsnumber >= 5:
               firstlevelstudentsnumber -= 2
               totaltransportcost = firstlevelstudentsnumber * 80 + 200
               savings = totaltransportcost - firstLevelfamilyAllowance
               print("The Amount Due is ", firstLevelfamilyAllowance, "You are saving", savings)
               return

        if secondlevelstudentsnumber <= 2:
            totaltransportcost += secondlevelstudentsnumber * 350
            print("The Amount Due is ",totaltransportcost)

        elif secondlevelstudentsnumber >= 3:
             secondlevelstudentsnumber -= 2
             totaltransportcost = secondlevelstudentsnumber * 300 + 700
             savings = totaltransportcost - secondLevelfamilyAllowance
             print("The Amount Due is ", secondLevelfamilyAllowance, "You are saving", savings)

        elif firstlevelstudentsnumber <= 2:
                    totaltransportcost += firstlevelstudentsnumber * 100
                    print("The Amount Due is ",totaltransportcost)




#calling the Function
def main():



    processtransportcost()

main()





