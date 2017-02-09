# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://amberteam.pl')
title = driver.title 
print(title)
assert title == u'AmberTeam / szkolenia, egzaminy, istqbm, reqb'
driver.close()
