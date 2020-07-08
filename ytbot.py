from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pyvirtualdisplay import Display

from time import sleep
display = Display(visible=0, size=(800, 600))
display.start()
options = Options()
options.headless = False
_browser_profile = webdriver.FirefoxProfile()
_browser_profile.set_preference("dom.webnotifications.enabled", False)
driver = webdriver.Firefox(options=options,firefox_profile=_browser_profile,executable_path=r'/root/ytbot/geckodriver')
try:
	print("loaded")
	driver.get("https://www.ytmonster.net/campaigns/views")
	user_name = driver.find_element_by_id('inputUsername')
	user_name.send_keys('vinay221097')
	password =driver.find_element_by_id('inputPassword')
	password.send_keys('Musha22@')
	login = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div/form/button')
	login.click()
	print("logged in successfully")
	sleep(3)
	driver.get("https://www.ytmonster.net/exchange/views")
	sleep(4)
except Exception as e:
	print("error occured",e)


def open_new_client():
	try:
		sleep(4)		
		driver.switch_to_window(driver.window_handles[0])
		client = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div[2]/a[3]')
		client.click()
		print("opened new client successfully")
	except Exception as e:
		print("error in opening new client",e)

def start_watching():
	try:
		sleep(5)
		window_number = len(driver.window_handles)
		print("window number",window_number)
		if window_number%2==0:
			window_number= window_number-1
		driver.switch_to_window(driver.window_handles[window_number])
		driver.set_window_size(300,300)
		sleep(2)
		startBtn= driver.find_element_by_id('startBtn')
		startBtn.click()
		print("started watching on window {}".format(window_number))
		sleep(3)
	except Exception as e:
		print("error ocuured in starting video",e)

for i in range(0,3):
	open_new_client()
	start_watching()
