import time

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException



#this code here gives yes to all permissions allowing smooth functioning of code later

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")

opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })

#open instagram and enter login details
driver = webdriver.Chrome(chrome_options=opt)
driver.get("https://www.instagram.com/")
time.sleep(5)


username=driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
username.send_keys("<<--your instagram username-->>")

password=driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
password.send_keys("<<--your instagram password-->>")

button=driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div")
button.click()

time.sleep(5)

#go to search and find the person whose pictures you want to like or comment
search=driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div/div/span[2]")
search.click()
time.sleep(4)
searchbox=driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")

searchbox.send_keys("<<--instagram handle of the person you want to like or comment-->>")
time.sleep(10)
searchbox.send_keys(Keys.RETURN)
searchbox.send_keys(Keys.RETURN)

time.sleep(10)
# open account
# follow=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button")
# follow.click()

# private account
# follow=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div/button")
# follow.click()
# time.sleep(20)


#following code is for liking and commenting on the first post
firstpost=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div/div/div[1]/div[1]/a")
firstpost.click()
time.sleep(12)
like=driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button")
like.click()
time.sleep(10)
comment = driver.find_element_by_class_name('Ypffh')
comment.click()
time.sleep(5)
commentbox = driver.find_element_by_class_name('focus-visible')
commentbox.send_keys('<<--comment you want to make-->>')
commentbox.send_keys(Keys.ENTER)
# comment=driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea")
# comment.send_keys("good content")
time.sleep(5)
nextpost=driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a")
nextpost.click()
time.sleep(7)
# now here is a loop for liking and commenting on all his posts
while(1):
    like=driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button")
    like.click()
    time.sleep(3)
    comment = driver.find_element_by_class_name('Ypffh')
    comment.click()
    time.sleep(5)
    commentbox = driver.find_element_by_class_name('focus-visible')
    commentbox.send_keys('<<--comment you want to make-->>')
    commentbox.send_keys(Keys.ENTER)
    nextpost=driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]")
    if not nextpost:
        print("No element found") 
        break 
    else:
        nextpost.click()
        time.sleep(20) 

#you can always make a comment array if you want to enter a different comment on each post