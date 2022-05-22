#importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_URL ="https://twitter.com/i/flow/login"
TWITTER_PASSWORD ="Hiruka123@"
URL ="https://www.speedtest.net/result/13184536583"

USER_NAME ="Hiruka1299"
driver_service = Service(executable_path="C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

#Getting internet speed
driver.get(URL)
time.sleep(2)
down_speed = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/span')
print(f"down: {down_speed.text}")
time.sleep(2)
up_speed = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/span')
print(f"up:{up_speed.text}")
time.sleep(3)

#Twitter bot
driver.get(TWITTER_URL)
time.sleep(3)
#Username
user_name = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
user_name.send_keys(USER_NAME)
time.sleep(2)
user_name.send_keys(Keys.ENTER)
time.sleep(2)

#Password
password = driver.find_element(By.NAME,'password')
time.sleep(2)
password.send_keys(TWITTER_PASSWORD)
password.send_keys(Keys.ENTER)

#tweet message
time.sleep(2)
tweet_message = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
time.sleep(2)
tweet = f"Hey! Why is my internet speed 19.46 down/4.47 up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
time.sleep(1)
tweet_message.send_keys(tweet)
time.sleep(3)

#tweet button
tweet_button = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
tweet_button.click()
