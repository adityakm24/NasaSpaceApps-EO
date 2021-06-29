#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 10:01:02 2021

@author: kiyisi.24
"""
import cv2
import matplotlib.pyplot as plt
def job():
    global addrs
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
    return job

def cntryn():
    global job
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
    adqry = job + cntry
    return adqrya
def city():
    addrs=""
    cty=""
    global cntry
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
    addrs = cntry + cty
    return addrs

job = job()
cntry = cntryn()
addrs = city()

