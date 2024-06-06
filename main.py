from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Keep Chrome Browser open after program ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3937718084&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

sign_in = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()

user_name = driver.find_element(By.CSS_SELECTOR, value="#username")
user_name.send_keys("contactarmaanhasib@gmail.com")

password = driver.find_element(By.CSS_SELECTOR, value="#password")
password.send_keys("Leogsd@666")

submit = driver.find_element(By.XPATH, value='/html/body/div/main/div[2]/div[1]/form/div[3]/button')
submit.click()

# job_list = driver.find_element(By.CLASS_NAME, value="scaffold-layout__list-container")
# job_list.click()

job_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
job_listings[0].click()





# next_button = driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button/span')
# next_button.click()
#
# upload_cv = driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span')
# upload_cv.click()