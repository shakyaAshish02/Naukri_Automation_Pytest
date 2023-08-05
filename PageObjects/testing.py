import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
import pandas as pd
import time

#import wait as wait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as con
#from time import sleep
#import undetected_chromedriver as UC
#from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
#from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import pytest
#from utilities.readProperties import ReadConfig
#from utilities.customLogger import LogGen
import time

opt = Options()

opt.add_experimental_option("debuggerAddress", "localhost:9988")

d=webdriver.Chrome(executable_path="C:\\Users\\ashis\\PycharmProjects\\pythonProject4\\chromedriver.exe",chrome_options=opt)
a = ActionChains(d)

profile = "//a[normalize-space()='View profile']"
d.find_element(By.XPATH,profile).click()

