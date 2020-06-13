# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 12:24:30 2020

@author: Etheking

THE CHORE WHEEL ORGANIZER!

"""

from datetime import date
from itertools import cycle

today = date.today()
year = today.year
month = today.month

chores = {
        "Sweeping/Vacuum Floors": "weekly",
        "Vacuum Stairs": "weekly",
        "Vacuum cat tower":"weekly",
        "Common bathroom: Toilet bowl, counters, floor, and mirror":"weekly",
        "Kitchen: Wipe counters, table, oven and microwave surfaces":"weekly",
        "Vacuum and tidy office.":"weekly",
        "Wash living room blankets":"biweekly",
        "Declutter and wipe down living room": "biweekly",
        "Rinse and dry trash/recycle bins":"biweekly",
        "Clean the fridge":"monthly",
        "Dusting: fans, windows, baseboards and surfaces":"monthly",
        "Mow the lawns":"monthly"
        }

def getMonthlyAssignment(month=month, year=year, specificPerson = ""):
    """month and year are both ints
    specific person is a str containing the name of a housemate, empty otherwise
    takes in the current month and year to return a tuple of lists 
    for the breakdown of chore assignments in a given month"""
    eli, sam, bob = ["ELI'S LIST:"], ["SAM'S LIST:"] , ["BOBBY'S LIST:"]
    groupMetaList = [eli, sam, bob]
    infiniteList = cycle(groupMetaList)
    weeklyChores, biweeklyChores, monthlyChores = [], [], []
    
    def personSelector():
        """shuffles through the list of housemates infinitely"""
        for subList in infiniteList:
            yield subList
            
    def shiftRight(aList, shifts=1):
        """takes aList as a list, and shifts as an int
        shifts aList to the right #shifts times"""
        try:
            newList = [aList[-1]] + aList[:-1]
            for x in range(shifts-1):
                newList = [newList[-1]] + newList[:-1]
            return newList
        except IndexError:
            return aList

    for chore in chores:
            if chores.get(chore) == "weekly":
                weeklyChores.append(chore)
            elif chores.get(chore) == "biweekly":
                biweeklyChores.append(chore)
            else:
                monthlyChores.append(chore)
    for week in range(1,5):
      person = personSelector()
      tempChoreList = []
      for chore in weeklyChores:
          tempChoreList.append(chore)
      if week == 1:
          for chore in monthlyChores:
              tempChoreList.append(chore)
      elif week == 2 or week == 4:
          for chore in biweeklyChores:     
              tempChoreList.append(chore)
      shiftedList = shiftRight(tempChoreList, (month+year+week))
      for chore in shiftedList:  
          temp = person.__next__()
          weekLabel = ("Week " + str(week)+":")
          if weekLabel not in temp:
              temp.append(weekLabel)
          temp.append(chore)
    if specificPerson != "":
        finalList = []
        for y in groupMetaList:
            if specificPerson in y[0]:
                finalList.append(y)
    else:
        finalList = groupMetaList
    for x in finalList:
        print(x[0])
        for y in x:
            if "LIST" in y:
                pass
            elif "Week" in y:
                print()
                print(y)
            else:
                print(y)
        print('-------------------------------------------------')
            
check = False
while check == False:
    specific = ""
    option = input("Do you want to see a specific month? Y/N:  ").upper()
    if option != "Y" and option != "N":
        check = True
    elif option == "N":
        getMonthlyAssignment()
    else:
        monthChoice = input("What month? Please use numbers 1-12:  ")
        yearChoice = input("What year? Please use the full year:  ")
        personChoice = input("Just one person's list? Y/N:  ").upper()
        if personChoice == "Y":
            specific = input("Type the name: Eli, Sam, or Bobby:   ").upper()
        try:
            print()
            print('-------------------------------------------------')
            getMonthlyAssignment(int(monthChoice), int(yearChoice),specific)
        except ValueError:
            print("You input bad values, you bad person!")