import time

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from selenium.webdriver.chrome.options import Options


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

driver = webdriver.Chrome(chrome_options=opt)
#open instagram and going to create new user
driver.get("https://www.instagram.com/")
time.sleep(10)
signup=driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/div/p/a/span")
signup.click()
time.sleep(5)
#here selecting the fields and giving email, name, username, password
email=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[3]/div/label/input")
email.send_keys("<<--your email-->>")
fullname=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[4]/div/label/input")
fullname.send_keys("<<--your name-->>")
username=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[5]/div/label/input")
username.send_keys("<<--your username-->>")
password=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[6]/div/label/input")
password.send_keys("<<--your password-->>")
time.sleep(5)
signupbutton=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button")
signupbutton.click()
time.sleep(5)
#here we will be selecting a birthdate from the dropdown
selectmonth=Select(driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select"))
selectmonth.select_by_visible_text("January")
selectdate=Select(driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select"))
selectdate.select_by_visible_text("25")
selectyear=Select(driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select"))
selectyear.select_by_visible_text("2001")
time.sleep(5)
nextbutton=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button")
nextbutton.click()
time.sleep(60)

#now an otp must be sent to your email id, so we open a new tab and take otp

driver.execute_script("window.open('');")

driver.switch_to.window(driver.window_handles[1])

#go to gmail
driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")

username=driver.find_element_by_name("identifier")
username.send_keys("<<--your username-->>")
nextbutton=driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]")
nextbutton.click()
time.sleep(4)
password=driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
password.send_keys("<<--your password-->>")
sub=driver.find_element_by_xpath("//*[@id='passwordNext']/div/button/div[2]")
sub.click()
time.sleep(4)
driver.get("https://www.gmail.com")
time.sleep(4)

#accessing the top email and taking out the otp 

otp=driver.find_element_by_xpath("//*[@id=':2n']/span").text
# print(otp)
mainotp=otp[0:6]

driver.switch_to.window(driver.window_handles[0])

#switching back to instagram and entering otp

enterotp=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div[2]/form/div/div[1]/input")

enterotp.send_keys(mainotp)

time.sleep(4)

laststep=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div[2]/form/div/div[2]/button")
laststep.click()

