#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 22:19:16 2021

@author: kiyisi.24
"""

def panama():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pydirectinput
    import datetime
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.youtube.com/watch?v=gkcrD1_DcbY');
    #pydirectinput.moveTo(100, 100)
    #pydirectinput.click()
    #date_stamp = str(datetime.datetime.now()).split('.')[0]
    #date_stamp = date_stamp.replace(" ","_")
    #file_name = date_stamp + ".png"
    driver.save_screenshot("y1.png");

def texas():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pydirectinput
    import time
    import datetime
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.earthcam.com/usa/texas/elpaso/?cam=elpaso');
    #pydirectinput.moveTo(100, 100)
    #pydirectinput.click()
    #t_end = time.time() + 25
    #while time.time() < t_end:
    #    date_stamp = str(datetime.datetime.now()).split('.')[0]
    #    date_stamp = date_stamp.replace(" ","_")
    #    file_name = date_stamp + ".png"
    driver.save_screenshot("eltx.png");


def LA():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pydirectinput
    import datetime
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://myearthcam.com/starlinetours');
    #pydirectinput.moveTo(100, 100)
    #pydirectinput.click()
    #date_stamp = str(datetime.datetime.now()).split('.')[0]
    #date_stamp = date_stamp.replace(" ","_")
    #file_name = date_stamp + ".png"
    driver.save_screenshot("elsl.png");

def tz():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pydirectinput
    import datetime
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://g0.ipcamlive.com/player/player.php?alias=zkpcam&timelapseplayerenabled=0');
    #pydirectinput.moveTo(100, 100)
    #pydirectinput.click()
    #date_stamp = str(datetime.datetime.now()).split('.')[0]
    #date_stamp = date_stamp.replace(" ","_")
    #file_name = date_stamp + ".png"
    driver.save_screenshot("ip.png");
    
def rome():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pydirectinput
    import datetime
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.skylinewebcams.com/en/webcam/italia/lazio/roma/fontana-di-trevi.html');
    #pydirectinput.moveTo(100, 100)
    #pydirectinput.click()
    #date_stamp = str(datetime.datetime.now()).split('.')[0]
    #date_stamp = date_stamp.replace(" ","_")
    #file_name = date_stamp + ".png"
    driver.save_screenshot("rome.png");


import schedule
import time

def job():
    print("I'm working...")
    panama()
    texas()
    LA()
    tz()
    rome()

#schedule.every().day.at("01:00").do(job,'It is 01:00')

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(30) 
