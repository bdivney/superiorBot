#!/usr/bin/env python3

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.supremenewyork.com/shop/jackets/fzfe0125o/wyqd5x4vm?alt=1")

driver.find_element_by_xpath('//input[@type="submit" and @value="add to cart"]').click()

driver.find_element_by_xpath('/html/body/div/div/div[1]/div/a[2]').click()

driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys("Brendan Divney")


driver.find_element_by_xpath('//*[@id="order_email"]').send_keys("brendandivney@gmail.com")

driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys("3035940427")

driver.find_element_by_xpath('//*[@id="bo"]').send_keys("1031 Duchess Dr")

driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys("22102")


