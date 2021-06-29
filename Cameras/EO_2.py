#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
    driver.save_screenshot("US/Panama/y1.png");

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
    driver.save_screenshot("US/LA/elsl.png");

def rome_antheon():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pydirectinput
    import datetime
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://www.albergodelsenato.it/webcam.php');
    #pydirectinput.moveTo(100, 100)
    #pydirectinput.click()
    #date_stamp = str(datetime.datetime.now()).split('.')[0]
    #date_stamp = date_stamp.replace(" ","_")
    #file_name = date_stamp + ".png"
    driver.save_screenshot("Italy/Rome/Rome_Piazza_Del_Pantheon.png");

def rome_trevi():
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
    driver.save_screenshot("Italy/Rome/Rome_Trevi_Fountain.png");
    
def rome_Spagna():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pydirectinput
    import datetime
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.skylinewebcams.com/webcam/italia/lazio/roma/piazza-di-spagna.html');
    #pydirectinput.moveTo(100, 100)
    #pydirectinput.click()
    #date_stamp = str(datetime.datetime.now()).split('.')[0]
    #date_stamp = date_stamp.replace(" ","_")
    #file_name = date_stamp + ".png"
    driver.save_screenshot("Italy/Rome/Rome_Piazza_di_Spagna.png");

def rome_il_palazzetto():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pydirectinput
    import datetime
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.hotelhasslerroma.com/en/il-palazzetto-footer-pages/webcam');
    #pydirectinput.moveTo(100, 100)
    #pydirectinput.click()
    #date_stamp = str(datetime.datetime.now()).split('.')[0]
    #date_stamp = date_stamp.replace(" ","_")
    #file_name = date_stamp + ".png"
    driver.save_screenshot("Italy/Rome/Rome_Il_Palazzetto.png");
    
def rome_colosseum():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pydirectinput
    import datetime
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.facebook.com/197761626911992/videos/230567388684465');
    #pydirectinput.moveTo(100, 100)
    #pydirectinput.click()
    #date_stamp = str(datetime.datetime.now()).split('.')[0]
    #date_stamp = date_stamp.replace(" ","_")
    #file_name = date_stamp + ".png"
    driver.save_screenshot("Italy/Rome/Rome_Colosseum.png");

def houston():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pydirectinput
    import datetime
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.webcamtaxi.com/en/usa/texas/houston-downtown.html');
    #pydirectinput.moveTo(100, 100)
    #pydirectinput.click()
    #date_stamp = str(datetime.datetime.now()).split('.')[0]
    #date_stamp = date_stamp.replace(" ","_")
    #file_name = date_stamp + ".png"
    driver.save_screenshot("US/Houston/Houston.png");
    
def LA2():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pydirectinput
    import datetime
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.earthcam.com/usa/california/losangeles/hollywoodandvine/?cam=hollywoodandvine');
    #pydirectinput.moveTo(100, 100)
    #pydirectinput.click()
    #date_stamp = str(datetime.datetime.now()).split('.')[0]
    #date_stamp = date_stamp.replace(" ","_")
    #file_name = date_stamp + ".png"
    driver.save_screenshot("US/LA/LA.png");
    
def hollywood_blvd():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pydirectinput
    import datetime
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.earthcam.com/usa/california/losangeles/hollywoodblvd/?cam=hollywoodblvd');
    #pydirectinput.moveTo(100, 100)
    #pydirectinput.click()
    #date_stamp = str(datetime.datetime.now()).split('.')[0]
    #date_stamp = date_stamp.replace(" ","_")
    #file_name = date_stamp + ".png"
    driver.save_screenshot("US/LA/hollywood_blvd.png");

def venice_beach():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pydirectinput
    import datetime
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.westland.net/beachcam/');
    #pydirectinput.moveTo(100, 100)
    #pydirectinput.click()
    #date_stamp = str(datetime.datetime.now()).split('.')[0]
    #date_stamp = date_stamp.replace(" ","_")
    #file_name = date_stamp + ".png"
    driver.save_screenshot("US/LA/venice_beach.png");
    
import schedule
import time

def job():
    print("I'm working...")
    panama()
    LA()
    tz()
    rome_antheon()
    rome_trevi()
    rome_Spagna()
    rome_il_palazzetto()
    rome_colosseum()
    houston()
    LA2()
    hollywood_blvd()
    venice_beach()

#schedule.every().day.at("06:00").do(job,'It is 06:00')

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(30) 
