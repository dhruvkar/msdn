from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import getpass

# Open chrome and navigate to site
#driver = webdriver.Ie()
#driver = webdriver.Chrome()
driver = webdriver.PhantomJS()
driver.get("https://www.microsoft.com/Licensing/servicecenter/default.aspx")

# Click sign in and then sign-in on live.com
driver.find_element_by_xpath("//input[@type='submit']").click()


# put in email and password
email = driver.find_element_by_xpath("//input[@type='email']")
pw = driver.find_element_by_xpath("//input[@type='password']")
email.send_keys("dkar@osisoft.com")
pw.send_keys(getpass.getpass())
#pw.send_keys("")

# Hit Submit
driver.find_element_by_xpath("//input[@type='submit']").click()


if "Help us protect your account" in driver.title:
	# Use email as the verification option
	p_email = driver.find_element_by_xpath("//input[@type='email']")
	p_email.send_keys("dkar")
	driver.find_element_by_xpath("//input[@type='submit']").click()
	
	# Prompt for Two Factor Authentication code sent to email
	enter_code = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "otc")))	
	enter_code.send_keys(raw_input("Enter numeric code from email: "))

	# Click 'I sign in frequently on this device. Don't ask me for a code'.
	driver.find_element_by_xpath("//*[@id='idChkBx_SAOTCC_TD']").click()
	
	# Click submit
	driver.find_element_by_xpath("//input[@type='submit']").click()
	
	
# navigate to page to assign user
driver.find_element_by_id("topnavitem5").click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "MSDN Search"))).click()
driver.find_element_by_xpath("//*[@id='tblAgrmntSrchRst']/tbody/tr/td[1]/a").click()
driver.find_element_by_link_text("Assign Subscription").click()
select = Select(driver.find_element_by_id("lbBenefitLevels"))

while True:
    msdn = raw_input("Enter type of subscription - Pro or Enterprise: ")
    if msdn.lower() == 'pro' or 'enterprise':
	break
    else:
	continue

if msdn.lower() == 'enterprise':
    select.select_by_visible_text("Visual Studio Enterprise w/MSDN")
else:
    select.select_by_visible_text("Visual Studio Pro w/MSDN")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Step1Next"))).click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "usrFirstName")))
firstname = driver.find_element_by_id("usrFirstName")
lastname = driver.find_element_by_id("usrLastName")
email = driver.find_element_by_id("usrEmailAddress")
country = Select(driver.find_element_by_id("ursInfoCountries"))
language = Select(driver.find_element_by_id("ursInfoLanguages"))
reference1 = driver.find_element_by_id("usrReference1")
reference2 = driver.find_element_by_id("usrReference2")






#driver.find_element_by_id("Step1Next").click()
#driver.find_element_by_xpath("//*[@id='tblAgrmntSrchRst']/tbody/tr/td[1]/a").click()
#driver.find_element_by_xpath("//*[@id='tabmenu']/li[2]/a").click()

