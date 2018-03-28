"""
Created on Fri Mar 16 03:11:53 2018

@author: ameypawar
"""# -*- coding: utf-8 -*-


'''

Parse Downloaded Cricket Data

'''

import os
import csv
import pandas as pd
import matplotlib.pyplot as plt

##################################Creating file's list of lists of all formats for all teams######################################### 
 
total_teams = 9
INPUT_FOLDER = []
INPUT_FOLDER_list = []
BATSMEN_OUTPUT_FILE = []
BATSMEN_OUTPUT_FILE_list = []
BOWLERS_OUTPUT_FILE = []
BOWLERS_OUTPUT_FILE_list = []

for i in range(1, total_teams+1):
    INPUT_FOLDER = ["espncricinfo-test_batsmen"+str(i),"espncricinfo-odi_batsmen"+str(i),"espncricinfo-t20i_batsmen"+str(i)]
    INPUT_FOLDER_list.append((INPUT_FOLDER))
#FINAL_OUTPUT_FILE1 = "test_batsmen.csv"
#FINAL_OUTPUT_FILE2 = "odi_batsmen.csv"
#FINAL_OUTPUT_FILE3 = "t20i_batsmen.csv"

    BATSMEN_OUTPUT_FILE = ["test_batsmen"+str(i)+".csv", "odi_batsmen"+str(i)+".csv", "t20i_batsmen"+str(i)+".csv"]
    BATSMEN_OUTPUT_FILE_list.append((BATSMEN_OUTPUT_FILE))
    BOWLERS_OUTPUT_FILE = ["test_bowlers"+str(i)+".csv", "odi_bowlers"+str(i)+".csv", "t20i_bowlers"+str(i)+".csv"]
    BOWLERS_OUTPUT_FILE_list.append((BOWLERS_OUTPUT_FILE))
    
BATSMEN_HEADER = "Player Name,Batting Average,Batting Strike rate,Batting Rating Points"
BOWLERS_HEADER = "Player Name,Bowling Average,Bowling Economy rate,Bowling Strike rate,Bowling Rating Points"

# removes end line characters to recover appropriate strings from data
def removeEndLineCharacter(mystr):
    return mystr.replace("\n"," ")
    
## finding strings which starts from startPattern and ends with endPattern 
def findWithPattern(mystr, startPattern, endPattern):
    """
    Find the string that starts with <startPattern> and ends with <endPattern> in the orginal string <mystr>.
    Args:
        + mystr: orginal string.
        + startPattern: 
        + endPattern: 
    Returns:
        + The found string,
        + and the remained part of the orginal string.
    """
    x = mystr.find(startPattern)
    if x==-1:
        return "",mystr
    mystr = mystr[x + len(startPattern):]
    y = mystr.find(endPattern)
    if y==-1:
        return "",mystr
    return mystr[:y], mystr[y+len(endPattern):]


# extracting useful information from data of test batsmen
def extracttestbatsmenDataFrom(data):
    outcome,tmp = findWithPattern(data, '<title>', 'ESPNcricinfo</title>' )
    Player_name = outcome.split("|")[0]
    data1 = removeEndLineCharacter(data)
    outcome1,tmp = findWithPattern(data1, 'batting\'><span><b>Tests', '</tr>')
    try:
        Batting_Average = outcome1.split("</td>")[6].split(">")[1]
    except:
        Batting_Average =  None
    try:
        Batting_Strike_rate = outcome1.split("</td>")[8].split(">")[1]
    except:
        Batting_Strike_rate = None
    try:
        Batting_Rating_points = (float(Batting_Average)*.87) + (float(Batting_Strike_rate)*float(Batting_Average)*.01*.13)
    except: 
        Batting_Rating_points = None
    return Player_name, Batting_Average, Batting_Strike_rate, Batting_Rating_points

# extracting useful information from data of test bowlers
def extracttestbowlersDataFrom(data):     
    outcome,tmp = findWithPattern(data, '<title>', 'ESPNcricinfo</title>' )
    Player_name = outcome.split("|")[0]
    data1 = removeEndLineCharacter(data)
    outcome2,tmp = findWithPattern(data1, 'bowling\'><span><b>Tests', '</tr>')
    try:
        Bowling_Average = outcome2.split("</td>")[8].split(">")[1]
    except: 
        Bowling_Average = None
    try:
        Bowling_Economy_rate = outcome2.split("</td>")[9].split(">")[1]
    except:
        Bowling_Economy_rate = None
    try:
        Bowling_Strike_rate = outcome2.split("</td>")[10].split(">")[1]
    except:
        Bowling_Strike_rate = None
    try:
        Bowling_Rating_points = (float(Bowling_Average)*.55) + (float(Bowling_Strike_rate)*float(Bowling_Average)*.01*.25) + (float(Bowling_Average)*((float(Bowling_Economy_rate)*.20)/6.00))
    except: 
        Bowling_Rating_points = None
    
    return Player_name, Bowling_Average, Bowling_Economy_rate, Bowling_Strike_rate, Bowling_Rating_points

# extracting useful information from data of ODI batsmen
def extractodibatsmenDataFrom(data):
    outcome,tmp = findWithPattern(data, '<title>', 'ESPNcricinfo</title>' )
    Player_name = outcome.split("|")[0]
    data1 = removeEndLineCharacter(data)
    outcome1,tmp = findWithPattern(data1, 'batting\'><span><b>ODIs', '</tr>')
    try:
        Batting_Average = outcome1.split("</td>")[6].split(">")[1]
    except:
        Batting_Average =  None
    try:
        Batting_Strike_rate = outcome1.split("</td>")[8].split(">")[1]
    except:
        Batting_Strike_rate = None
    try:
        Batting_Rating_points = (float(Batting_Average)*.7) + (float(Batting_Strike_rate)*float(Batting_Average)*.01*.3)
    except: 
        Batting_Rating_points = None
    return Player_name, Batting_Average, Batting_Strike_rate, Batting_Rating_points

# extracting useful information from data of ODI bowlers
def extractodibowlersDataFrom(data): 
    outcome,tmp = findWithPattern(data, '<title>', 'ESPNcricinfo</title>' )
    Player_name = outcome.split("|")[0]
    data1 = removeEndLineCharacter(data)       
    outcome2,tmp = findWithPattern(data1, 'bowling\'><span><b>Tests', '</tr>')
    try:
        Bowling_Average = outcome2.split("</td>")[8].split(">")[1]
    except: 
        Bowling_Average = None
    try:
        Bowling_Economy_rate = outcome2.split("</td>")[9].split(">")[1]
    except:
        Bowling_Economy_rate = None
    try:
        Bowling_Strike_rate = outcome2.split("</td>")[10].split(">")[1]
    except:
        Bowling_Strike_rate = None
    try:
        Bowling_Rating_points = (float(Bowling_Average)*.50) + (float(Bowling_Strike_rate)*float(Bowling_Average)*.01*.20) + (float(Bowling_Average)*((float(Bowling_Economy_rate)*.30)/6.00))
    except: 
        Bowling_Rating_points = None
    
    return Player_name, Bowling_Average, Bowling_Economy_rate, Bowling_Strike_rate, Bowling_Rating_points
   

# extracting useful information from data of t20i batsmen
def extractt20ibatsmenDataFrom(data):
    outcome,tmp = findWithPattern(data, '<title>', 'ESPNcricinfo</title>' )
    Player_name = outcome.split("|")[0]
    data1 = removeEndLineCharacter(data)
    outcome1,tmp = findWithPattern(data1, 'batting\'><span><b>T20Is', '</tr>')
    try:
        Batting_Average = outcome1.split("</td>")[6].split(">")[1]
    except:
        Batting_Average =  None
    try:
        Batting_Strike_rate = outcome1.split("</td>")[8].split(">")[1]
    except:
        Batting_Strike_rate = None
    try:
        Batting_Rating_points = (float(Batting_Average)*.5) + (float(Batting_Strike_rate)*float(Batting_Average)*.01*.5)
    except: 
        Batting_Rating_points = None
    return Player_name, Batting_Average, Batting_Strike_rate, Batting_Rating_points

# extracting useful information from data of t20i bowlers
def extractt20ibowlersDataFrom(data):
    outcome,tmp = findWithPattern(data, '<title>', 'ESPNcricinfo</title>' )
    Player_name = outcome.split("|")[0]
    data1 = removeEndLineCharacter(data)    
    outcome2,tmp = findWithPattern(data1, 'bowling\'><span><b>Tests', '</tr>')
    try:
        Bowling_Average = outcome2.split("</td>")[8].split(">")[1]
    except: 
        Bowling_Average = None
    try:
        Bowling_Economy_rate = outcome2.split("</td>")[9].split(">")[1]
    except:
        Bowling_Economy_rate = None
    try:
        Bowling_Strike_rate = outcome2.split("</td>")[10].split(">")[1]
    except:
        Bowling_Strike_rate = None
    try:
        Bowling_Rating_points = (float(Bowling_Average)*.45) + (float(Bowling_Strike_rate)*float(Bowling_Average)*.01*.20) + (float(Bowling_Average)*((float(Bowling_Economy_rate)*.35)/6.00))
    except: 
        Bowling_Rating_points = None
    
    return Player_name, Bowling_Average, Bowling_Economy_rate, Bowling_Strike_rate, Bowling_Rating_points
    
##################################START PROCESSING DATA#########################################

for batsmen_file_list in BATSMEN_OUTPUT_FILE_list:
    for batsmen_file in batsmen_file_list:
        outputFile = open(batsmen_file, "w")
        outputFile.write(BATSMEN_HEADER + "\n")
        folder = "espncricinfo-"+ batsmen_file.split(".")[0]
        
        print "---PROCESSING FOLDER {0!s}---".format(folder)
        counter = 0
        
        for url in os.listdir(folder):
        
            print folder+url
            data = open(folder + "/" + url).read()
#           extracting batting variables from test ODI and t20i        
            if (batsmen_file.find("test")> -1):
                Player_name, Batting_Average, Batting_Strike_rate, Batting_Rating_points = extracttestbatsmenDataFrom(data)
            if (batsmen_file.find("odi")> -1):
                Player_name, Batting_Average, Batting_Strike_rate, Batting_Rating_points = extractodibatsmenDataFrom(data)
            if (batsmen_file.find("t20i")> -1):
                Player_name, Batting_Average, Batting_Strike_rate, Batting_Rating_points = extractt20ibatsmenDataFrom(data)
        
            url_new = folder + "/" + url
#           adding batting varibles to csv files 
            if (Batting_Rating_points != None):
                rowStr = '"{0!s}","{1!s}","{2!s}","{3!s}"\n'.format(Player_name, Batting_Average, Batting_Strike_rate, Batting_Rating_points)
                outputFile.write(rowStr)
            
            counter = counter + 1
            if counter%1000==0:
                print "   + Processing file {0:d}000th".format(counter/1000)
        outputFile.close()
        print "DONE. Wrote output to {0!s}".format(batsmen_file)
        

for bowlers_file_list in BOWLERS_OUTPUT_FILE_list:
    for bowlers_file in bowlers_file_list:
        outputFile = open(bowlers_file, "w")
        outputFile.write(BOWLERS_HEADER + "\n")
        batsmen_file = bowlers_file.replace("bowlers","batsmen")
        folder = "espncricinfo-"+ batsmen_file.split(".")[0]
        
        print "---PROCESSING FOLDER {0!s}---".format(folder)
        counter = 0
     
        for url in os.listdir(folder):
        
            print folder+url
            data = open(folder + "/" + url).read()
#           extracting bowling variables from test ODI and t20i                
            if (bowlers_file.find("test")> -1):
                Player_name, Bowling_Average,  Bowling_Economy_rate, Bowling_Strike_rate, Bowling_Rating_points = extracttestbowlersDataFrom(data)
            if (bowlers_file.find("odi")> -1):
                Player_name, Bowling_Average,  Bowling_Economy_rate, Bowling_Strike_rate, Bowling_Rating_points = extractodibowlersDataFrom(data)
            if (bowlers_file.find("t20i")> -1):
                Player_name, Bowling_Average,  Bowling_Economy_rate, Bowling_Strike_rate, Bowling_Rating_points = extractt20ibowlersDataFrom(data)
            
        
            url_new = folder + "/" + url
#           adding bowling varibles to csv files         
            if (Bowling_Rating_points != None):
                rowStr1 = '"{0!s}","{1!s}","{2!s}","{3!s}","{4!s}"\n'.format(Player_name, Bowling_Average, Bowling_Economy_rate, Bowling_Strike_rate, Bowling_Rating_points)
                outputFile.write(rowStr1)
        
        
      
            counter = counter + 1
            if counter%1000==0:
                print "   + Processing file {0:d}000th".format(counter/1000)
        outputFile.close()
        print "DONE. Wrote output to {0!s}".format(bowlers_file)
    
##################################Plot of Analysed data#########################################

colors = ['red', 'blue', 'lime']
teams = ['England', 'Australia', 'South Africa', 'west Indies', 'New Zealand', 'India', 'Pakistan', 'Sri Lanka', 'Zimbabwe']

##################################Plot of Analysed data for batsmen#########################################
k = 0
for batsmen_file_list in BATSMEN_OUTPUT_FILE_list:
    i=0
    for batsmen_file in batsmen_file_list:
        df = pd.read_csv(batsmen_file)
        ax = df.plot(x="Player Name", y="Batting Rating Points" ,kind='bar', color = colors[i], title ="Ratings or Perfomance Analysis of "+batsmen_file.split(".")[0].split("_")[0]+" batsmen of team "+ teams[k], figsize=(60, 60), legend=True, fontsize=12)
        ax.set_xlabel("Player Name", fontsize=12)
        ax.set_ylabel("Batting Rating Points", fontsize=12)
        i += 1
    k +=1
    
##################################Plot of Analysed data for bowlers#########################################

k = 0
for bowlers_file_list in BOWLERS_OUTPUT_FILE_list:
    i=0
    for bowlers_file in bowlers_file_list:
        df = pd.read_csv(bowlers_file)    
        ax1 = df.plot(x="Player Name", y="Bowling Rating Points" ,kind='bar', color = colors[i], title ="Ratings or Perfomance Analysis of "+bowlers_file.split(".")[0].split("_")[0]+" bowlers of team "+ teams[k], figsize=(80, 80), legend=True, fontsize=12)
        ax1.set_xlabel("Player Name", fontsize=12)
        ax1.set_ylabel("Bowling Rating Points", fontsize=12)
        i += 1
    k +=1

