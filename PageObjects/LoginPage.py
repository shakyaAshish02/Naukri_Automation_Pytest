import time
from selenium.webdriver.support import expected_conditions as con
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from utilities.customLogger import logclass



class functions():

    profile = "//a[normalize-space()='View profile']"
    headerbox="//div[@class='card mt15']//div//span[@class='edit icon'][normalize-space()='editOneTheme']"
    headerboxselect="resumeHeadlineTxt"
    comments="SAP MM, Six Sigma Green Belt,S-2-P Procurement, Buyer, SQL, Tableau, Python, Selenium, Automation, Analytics, MBA"
    resumebutton="//div[@class='uploadBtn']//input[@type='file']"
    resumelink="C:\\Users\\ashis\\Downloads\\Ashishshakya_resume1.pdf"
    Headerok="//button[normalize-space()='Save']"
    log=logclass.getthelogs()

    def __init__(self, driver,wait,a):
        self.driver = driver
        self.wait = wait
        self.a=a
    def profil(self):
        self.log.info("clicked on profile")
        try:
            self.wait.until(con.presence_of_element_located((By.XPATH,self.profile))).click()
        except:
            self.errors()


    def headertext(self):
        self.wait.until(con.presence_of_element_located((By.XPATH,self.headerbox))).click()
        self.wait.until(con.presence_of_element_located((By.ID,self.headerboxselect))).click()
        self.a.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        self.a.key_down(Keys.BACKSPACE).send_keys(self.comments).key_up(Keys.BACKSPACE).perform()
        self.wait.until(con.presence_of_element_located((By.XPATH,self.Headerok ))).click()
        self.log.info("headertext cleared")
    def resume(self):
        time.sleep(3)
        self.wait.until(con.presence_of_element_located((By.XPATH,self.resumebutton))).send_keys(self.resumelink)
        self.log.info("all functions cleared")

    def errors(self):
        self.log.info("error occured snapshot taken")
        self.driver.save_screenshot("C:\\Users\\ashis\PycharmProjects\\pythonProject9\\Screenshots\\"+"2.png")
        self.driver.get("https://www.naukri.com/mnjuser/homepage")
        self.profil()

    def checksanity(self):
        self.log.info("sanity running")

