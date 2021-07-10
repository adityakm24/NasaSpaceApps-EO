#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def jobs():
    job =""
    print("1) NASA radar images \n 2) Cameras \n 3) Population location data")
    ch=int(input("Enter choice: "))
    if ch==1:
        job="NASA radar images" 
    elif ch==2:
        job="Cameras"
    elif ch==3:
        job="Population location data"
    else:
        print("Error-Wrong choice entered. Please try again.")
    return str(job)

def cntryn():
    global job
    cty=""
    cntry=""
    adqry=""
    print("1) United States \n2) Italy")
    c=int(input("Select a country"))
    print(c)
    if c == 1:
        cntry="US"
    elif c == 2:
        cntry="Italy"
    else:
        print("Error-Wrong choice entered. Please try again.")
    return cntry

def city():
    addrs=""
    cty=""
    global cntry
    print (cntry)
    if cntry == "US":
        print("1) Los Angeles \n 2)Panama \n 3)Houston")
        c = int(input("Select a a city"))
        if c==1:
            cty="LA"
        elif c==2:
            cty="Panama"
        elif c==3:
            cty="Houston"
        else:
            print("Error-Wrong choice entered. Please try again.")
    elif cntry == "Italy":
        cty="Rome"
    else:
        print("Error-Wrong choice entered. Please try again.")
    print(cty)
    return cty

job = jobs()
cntry = cntryn()
cty = city()

loc = str(job + "\\" + cntry + "\\" + cty)
import subprocess
subprocess.Popen(f'explorer "{loc}"')

