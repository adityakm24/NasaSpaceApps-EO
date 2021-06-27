def panama():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pyautogui
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.youtube.com/watch?v=gkcrD1_DcbY');
    pyautogui.click(100, 100)
    driver.save_screenshot("screenshot-panama.png");

def texas():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pyautogui
    import time
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.earthcam.com/usa/texas/elpaso/?cam=elpaso');
    pyautogui.click(100, 100)
    t_end = time.time() + 25
    while time.time() < t_end:
        driver.save_screenshot("screenshot-texas.png");

    
def LA():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pyautogui
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://myearthcam.com/starlinetours');
    pyautogui.click(100, 100)
    driver.save_screenshot("screenshot-LA.png");

def tz():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import pyautogui
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://g0.ipcamlive.com/player/player.php?alias=zkpcam&timelapseplayerenabled=0');
    pyautogui.click(100, 100)
    driver.save_screenshot("screenshot-tz.png");



import schedule
import time

def job(t):
    panama()
    texas()
    LA()
    tz()

schedule.every().day.at("01:00").do(job,'It is 01:00')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute