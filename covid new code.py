# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 09:36:20 2022

@author: ANUJ KADU
"""
import matplotlib.pyplot as plt
import sys
import pandas as pd
#from csv import writer
tbl = pd.read_csv("C:\\Users\\ANUJ KADU\\Documents\\residents.csv", usecols=[
                  0, 1, 2, 3], index_col='Flat No.')
tbl2 = pd.read_csv("C:\\Users\\ANUJ KADU\\Documents\\Visitors.csv", usecols=[
                   0, 1, 2, 3, 4], index_col='Flat No.')
tbl3 = pd.read_csv(
    "C:\\Users\\ANUJ KADU\\Documents\\list_res.csv", index_col='index')
tbl4 = pd.read_csv(
    "C:\\Users\\ANUJ KADU\\Documents\\list_vis.csv", index_col='index')
lst1 = tbl3['Flat No.'].to_list()
lst2 = tbl4['Flat No.'].to_list()


def main4():
    k = int(input(" ENTER FLAT NUMBER:"))
    if k in lst1:
        print(tbl.loc[k:k, :])
        main()
    else:
        print(" FLAT NO. INCORRECT. TRY AGAIN")
        main4()


def main5():
    k = int(input(" ENTER FLAT NUMBER:"))
    if k in lst2:
        print(tbl2.loc[k:k, :])
        main()
    else:
        print(" FLAT NO. INCORRECT. TRY AGAIN")
        main5()


def main2():
    f = int(input(" ENTER FLAT NO.: "))
    n = str(input(" ENTER RESIDENT NAME: "))
    t = str(input(" ENTER LAST RECORDED TEMPERATURE: "))
    v = str(input(" ENTER VACCINATION RECORD (COMPLETE/INCOMPLETE): "))
    print()
    if f not in lst1:
        tbl.at[f, :] = [n, t, v]
        tbl.to_csv("C:\\Users\\ANUJ KADU\\Documents\\residents.csv")
        len1 = len(lst1)
        tbl3.at[len1, :] = [f]
        tbl3.to_csv("C:\\Users\\ANUJ KADU\\Documents\\list_res.csv")
        lst1.append(f)
        print(tbl)
        print()
        main()

    else:
        print(" INVALID FLAT NO.")
        print()
        print(" RESIDENT OF THIS FLAT ALREADY EXISTS")
        print()
        print(" TO ENTER AGAIN PRESS Y")
        print()
        print(" TO CANCEL PRESS N")
        yn = str(input(" ENTER CHOICE: "))
        if yn == 'Y':
            main2()
        elif yn == 'N':
            main()


def main3():
    fn = int(input(" ENTER FLAT NO.: "))
    vi = str(input(" ENTER VISITOR NAME: "))
    te = str(input(" ENTER RECORDED TEMPERATURE: "))
    vs = str(input(" ENTER VACCINATION STATUS: "))
    en = str(input(" ENTER ENTRY MONTH: "))
    len2 = len(lst2)
    inx = int(len2+1)
    if fn in lst1:
        tbl2.loc[inx] = [vi, te, vs, en]
        tbl2.rename(index={inx: fn}, inplace=True)
        tbl4.at[len2, :] = [fn]
        tbl4.to_csv("C:\\Users\\ANUJ KADU\\Documents\\list_vis.csv")
        lst2.append(fn)
        print(tbl2)
        main()
    else:
        print(" INVALID FLAT NO.")
        print()
        print(" FLAT IS UNOCCUPIED")
        print()
        print(" TO TRY AGAIN PRESS Y")
        print()
        print(" TO CANCEL ACTION PRESS N")
        print()
        yon = str(input(" ENTER CHOICE: "))
        if yon == 'Y':
            main3()
        elif yon == 'N':
            main()


def main():
    print("---------------VIRKAR HOUSING SOCIETY---------------")
    print()
    print(" TO GET REQUIRED INFORMATION ENTER RESPECTIVE NUMBER")
    print()
    print(" TO KNOW MORE ABOUT COVID PRESS 1")
    print()
    print(" TO GET ALL RESIDENT INFORMATION PRESS 2")
    print()
    print(" TO GET ALL VISITOR INFORMATION PRESS 3")
    print()
    print(" TO GET INFORMATION ABOUT RESIDENT AND VISITOR BY FLAT NUMBER PRESS 4")
    print()
    print(" TO ADD NEW RESIDENT INFORMATION PRESS 5")
    print()
    print(" TO ADD NEW VISITOR INFORMATION PRESS 6")
    print()
    print(" TO VIEW ANALYSIS OF INFORMATION PRESS 7")
    print()
    print(" TO EXIT PROGRAM PRESS 8")

    x = int(input(" ENTER NO: "))

    if x == 1:
        print()
        print("Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus.\n"
              "Most people infected with the virus will experience mild to moderate respiratory illness \nand recover without requiring special treatment.\n"
              "However, some will become seriously ill and require medical attention.\n"
              "Due to this it is recommended to follow the guidelines given below:\n"
              "\n"
              "Use masks when outside.\n"
              "\n"
              "Follow social distancing norms when outside and go only if needed. \n"
              "\n"
              "Get the Covid vaccine if not taken already.")
        print()
        print("INCASE OF EMERGENCY: CALL 020-26127394 (covid maharashtra helpline)")
        print()
        main()
    elif x == 2:
        print()
        print(tbl)
        print()
        main()
    elif x == 3:
        print()
        print(tbl2)
        print()
        main()
    elif x == 4:
        print()
        print(" TO GET VISITOR INFORMATION PRESS V")
        print()
        print(" TO GET RESIDENT INFORMATION PRESS R")
        print()
        r = str(input(" ENTER HERE: "))
        print()
        if r == 'R':
            k = int(input(" ENTER FLAT NUMBER:"))
            print()
            if k in lst1:
                print(tbl.loc[k:k, :])
                main()
            else:
                print(" FLAT NO. INCORRECT. TRY AGAIN")
                main4()
        elif r == 'V':
            k = int(input(" ENTER FLAT NUMBER:"))
            print()
            if k in lst2:
                print(tbl2.loc[k:k, :])
                main()
            else:
                print(" VISITOR TO THIS FLAT DOES NOT EXIST. ENTER AGAIN")
                main5()
    elif x == 5:
        print()
        main2()
    elif x == 6:
        print()
        main3()

    elif x == 7:
        vis = tbl2['Entry month'].to_list()
        vis2 = tbl2['Vaccination status'].to_list()
        countJ = 0
        countF = 0
        countM = 0
        countA = 0
        countMay = 0
        countJune = 0
        countJuly = 0
        countAug = 0
        countS = 0
        countO = 0
        countN = 0
        countD = 0
        countC = 0
        countIC = 0
        mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
               'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
        for x in vis:
            if x == "January":
                countJ += 1
            elif x == "February":
                countF += 1
            elif x == "March":
                countM += 1
            elif x == "April":
                countA += 1
            elif x == "May":
                countMay += 1
            elif x == "June":
                countJune += 1
            elif x == "July":
                countJuly += 1
            elif x == "August":
                countAug += 1
            elif x == "September":
                countS += 1
            elif x == "October":
                countO += 1
            elif x == "November":
                countN += 1
            elif x == "December":
                countD += 1
        for y in vis2:
            if y == 'COMPLETE':
                countC += 1
            elif y == 'INCOMPLETE':
                countIC += 1
        pie1 = [countC, countIC]
        lab = ['VACCINATED', 'NOT VACCINATED']
        entry = [countJ, countF, countM, countA, countMay, countJune,
                 countJuly, countAug, countS, countO, countN, countD]
        print()
        print(" TO GET VACCINATION GRAPH FOR VISITORS PRESS P")
        print()
        print(" TO GET VISITOR ANALYSIS BY MONTH PRESS Q")
        print()
        pq = str(input("ENTER CHOICE: "))

        if pq == 'Q':
            plt.bar(mon, entry)
            plt.yticks([1, 2, 3, 4], [1, 2, 3, 4])
            plt.xlabel("Months")
            plt.ylabel("No. of Visitors")
            plt.show()
            main()

        elif pq == 'P':
            plt.pie(pie1, labels=lab, autopct='%1.1f%%')
            plt.show()
            main()

    elif x == 8:
        print()
        print("-----------THANK YOU FOR USING THIS PROGRAM----------")
        sys.exit()


main()
