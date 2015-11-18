# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class add_remove_film(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://localhost:8081/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_remove_film(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
	driver.find_element_by_id("username").clear()
        
	driver.find_element_by_id("username").send_keys("admin")
       
	driver.find_element_by_name("password").clear()
     
	driver.find_element_by_name("password").send_keys("admin")
 
	driver.find_element_by_name("submit").click()


  	driver.find_element_by_link_text("Add movie").click()
        driver.find_element_by_xpath("//*[@id='updateform']/table/tbody/tr[2]/td[2]/input").send_keys("my film")
	driver.find_element_by_xpath("//*[@id='submit']").click()
	driver.find_element_by_xpath(".//*[@id='updateform']/table/tbody/tr[4]/td[2]/label")
	driver.find_element_by_xpath("//*[@id='updateform']/table/tbody/tr[4]/td[2]/input").send_keys("1989")
	driver.find_element_by_xpath("//*[@id='submit']").click()
	driver.find_element_by_xpath("//*[@id='wrapper']/header/div/a/h1").click()
	driver.find_element_by_css_selector(".title").click()
	driver.find_element_by_xpath(".//*[@id='content']/section/nav/ul/li[4]/div/div/a/img").click()
	driver.switch_to_alert().accept()	
	driver.quit()