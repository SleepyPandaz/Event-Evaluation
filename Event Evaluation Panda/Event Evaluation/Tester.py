'''
Created on Oct 4, 2018

@author: ZakLuetmer
'''

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="zvluetmer@csbsju.edu",
  passwd="Legend34"
)

print(mydb)
