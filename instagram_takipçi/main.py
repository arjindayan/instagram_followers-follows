
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")


driver = webdriver.Chrome(service=Service(".\\chromedriver-win64\\chromedriver.exe"), options=chrome_options)


user_id=input("Please enter your instagram user_id")
password=input("Please enter your password")




# Open Instagram
driver.get("https://www.instagram.com/")

wait = WebDriverWait(driver, 10)

# Log in process
user_id_section = wait.until(EC.presence_of_element_located((By.NAME, "username")))
user_id_section.send_keys(user_id)
password_section = driver.find_element(By.NAME, "password")
password_section.send_keys(password)

enter_section = driver.find_element(By.CSS_SELECTOR, "._acan._acap._acas._aj1-._ap30")
enter_section.send_keys(Keys.ENTER)

time.sleep(10)

# Handle pop-ups and notifications
şimdi_değil_section = driver.find_element(By.CSS_SELECTOR, ".x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37")
şimdi_değil_section.send_keys(Keys.ENTER)

time.sleep(10)



time.sleep(10)


profile_gir_section = driver.find_element(By.CSS_SELECTOR, "a[href='/aarjiinn/']")
profile_gir_section.send_keys(Keys.ENTER)

time.sleep(6)

# Open the followers list
takipçi_section = driver.find_element(By.CSS_SELECTOR, ".x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x5n08af.x9n4tj2._a6hd")
takipçi_section.send_keys(Keys.ENTER)
time.sleep(6)



followers_pop_up=driver.find_element(By.CSS_SELECTOR,".xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6")
last_height = driver.execute_script("return arguments[0].scrollHeight", followers_pop_up)


while True:
    driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", followers_pop_up)
    time.sleep(3)  # Adjust sleep as necessary
    new_height = driver.execute_script("return arguments[0].scrollHeight", followers_pop_up)
    
    if new_height == last_height:
        break
    last_height = new_height

followers=driver.find_elements(By.CSS_SELECTOR,"._ap3a._aaco._aacw._aacx._aad7._aade")
follower_names = [follower.text for follower in followers]

driver.back()
time.sleep(5)

takip_section=driver.find_elements(By.CSS_SELECTOR,".x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x5n08af.x9n4tj2._a6hd")[0]

takip_section.send_keys(Keys.ENTER)


time.sleep(5)

follows_pop_up=driver.find_element(By.CSS_SELECTOR,".xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6")
last_height = driver.execute_script("return arguments[0].scrollHeight", follows_pop_up)

while True:
    driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", follows_pop_up)
    time.sleep(2)  # Adjust sleep as necessary
    new_height = driver.execute_script("return arguments[0].scrollHeight", follows_pop_up)
    
    if new_height == last_height:
        break
    last_height = new_height


follows=driver.find_elements(By.CSS_SELECTOR,"._ap3a._aaco._aacw._aacx._aad7._aade")

follows_names=[followss.text for followss in follows]




with open('follows.txt', 'w') as f:
    for name in follows_names:
        f.write(name + '\n')

print(f"Saved {len(follows_names)} followers to file.")


time.sleep(4)

with open("followers.txt") as f:
    followers=[line for line in f]
    
with open("follows.txt") as f:
    follows=[line for line in f]


for follow in follows:
    if follow not  in followers:
        print(follow)
        print("\n")