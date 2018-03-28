# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 23:59:02 2018

@author: ameypawar
"""
# This file will create a folder of each team which will contain url data of each capped player of that team

import urllib2
import sys
import time
import os
import unicodedata
from urlparse import urlparse
from bs4 import BeautifulSoup
import shutil

total_teams=10

BASE_URL = 'http://www.espncricinfo.com'

for i in range(1, total_teams+1):
#     if file is there then delete it and then create a new one for test data
    if os.path.exists('./espncricinfo-test_batsmen'+ str(i)):
        shutil.rmtree('./espncricinfo-test_batsmen'+ str(i))
    
    if not os.path.exists('./espncricinfo-test_batsmen'+ str(i)):
        os.mkdir('./espncricinfo-test_batsmen'+ str(i))

    
    soupy_test_team = BeautifulSoup(urllib2.urlopen('http://www.espncricinfo.com/india/content/player/caps.html?country='+str(i)+';class=1').read())
    
    #time.sleep(1)
    for new_host_test in soupy_test_team.findAll('li', {'class' : 'ciPlayername'}):
        try:
#            print new_host_odi
            
            new_host_test = new_host_test.find('a')['href']
        
        except:
            continue
        testurl = BASE_URL + urlparse(new_host_test).geturl()
        new_host_test = unicodedata.normalize('NFKD', unicode(new_host_test)).encode('ascii','ignore')
        print new_host_test
        #print(type(str.split(new_host)[3]))
        print str.split(new_host_test, "/")[4]
        try:
            html = urllib2.urlopen(testurl).read()
            if html:
                with open('espncricinfo-test_batsmen'+ str(i)+'/{0!s}'.format(str.split(new_host_test, "/")[4]), "wb") as f:
                    f.write(html)
        except:
            continue
    

#     if file is there then delete it and then create a new one for ODI data
    if os.path.exists('./espncricinfo-odi_batsmen'+ str(i)):
        shutil.rmtree('./espncricinfo-odi_batsmen'+ str(i))
    
    if not os.path.exists('./espncricinfo-odi_batsmen'+ str(i)):
        os.mkdir('./espncricinfo-odi_batsmen'+ str(i))



    soupy_odi_team = BeautifulSoup(urllib2.urlopen('http://www.espncricinfo.com/india/content/player/caps.html?country='+str(i)+';class=2').read())
    
    #time.sleep(1)
    for new_host_odi in soupy_odi_team.findAll('li', {'class' : 'ciPlayername'}):
        try:
#            print new_host_odi
            
            new_host_odi = new_host_odi.find('a')['href']
        
        except:
            continue
        odiurl = BASE_URL + urlparse(new_host_odi).geturl()
        new_host_odi = unicodedata.normalize('NFKD', unicode(new_host_odi)).encode('ascii','ignore')
        print new_host_odi
        #print(type(str.split(new_host)[3]))
        print str.split(new_host_odi, "/")[4]
        try:
            html = urllib2.urlopen(odiurl).read()
            if html:
                with open('espncricinfo-odi_batsmen'+ str(i)+'/{0!s}'.format(str.split(new_host_odi, "/")[4]), "wb") as f:
                    f.write(html)
        except:
            continue
    

#     if file is there then delete it and then create a new one for t20i data

    if os.path.exists('./espncricinfo-t20i_batsmen'+ str(i)):
        shutil.rmtree('./espncricinfo-t20i_batsmen'+ str(i))
    
    if not os.path.exists('./espncricinfo-t20i_batsmen'+ str(i)):
        os.mkdir('./espncricinfo-t20i_batsmen'+ str(i))


    soupy_t20i_team = BeautifulSoup(urllib2.urlopen('http://www.espncricinfo.com/india/content/player/caps.html?country='+str(i)+';class=1').read())
    
    #time.sleep(1)
    for new_host_t20i in soupy_t20i_team.findAll('li', {'class' : 'ciPlayername'}):
        try:
#            print new_host_odi
            
            new_host_t20i = new_host_t20i.find('a')['href']
        
        except:
            continue
        t20iurl = BASE_URL + urlparse(new_host_t20i).geturl()
        new_host_t20i = unicodedata.normalize('NFKD', unicode(new_host_t20i)).encode('ascii','ignore')
        print new_host_t20i
        #print(type(str.split(new_host)[3]))
        print str.split(new_host_t20i, "/")[4]
        try:
            html = urllib2.urlopen(t20iurl).read()
            if html:
                with open('espncricinfo-t20i_batsmen'+ str(i)+'/{0!s}'.format(str.split(new_host_t20i, "/")[4]), "wb") as f:
                    f.write(html)
        except:
            continue
    