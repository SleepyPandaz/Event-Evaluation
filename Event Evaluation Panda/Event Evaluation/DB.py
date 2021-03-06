'''
Created on Sep 26, 2018

@author: ZakLuetmer
'''
import sqlite3
import csv
from sqlite3 import Error
import psycopg2
import tkinter as tk
from tkinter import filedialog
from tkinter import *
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        cursor=conn.cursor()
        return conn, cursor
    except Error as e:
        print(e)
 
    return None
 
def close(conn):
    """ Commit changes and close connection to the database """
    # conn.commit()
    conn.close()
    
def total_rows(cursor, table_name, print_out=False):
    """ Returns the total number of rows in the database """
    cursor.execute('SELECT COUNT(*) FROM {}'.format(table_name))
    count = cursor.fetchall()
    if print_out:
        print('\nTotal rows: {}'.format(count[0][0]))
    return count[0][0]
 
 

def add_data_Students(dataFileName, cur):
     """ Add data to database by reading .txt file
    :param dataFileName: .txt file with data to be imported
     """           
     with open(dataFileName) as csv_file:
         csv_reader = csv.reader(csv_file, delimiter=',')
         for row in csv_reader:
             cur.execute("""SELECT ID
             FROM Students
             WHERE ID=?""",(row[0],))
             
             result = cur.fetchone()
             if result:
                 print("Student " + row[0] + " Already in Database")
             else:
                 cur.execute("INSERT INTO STUDENTS VALUES (?, ?, ?, ?, ?)", row)
         
         print("Addition Successful") 
         csv_file.close()       
def add_data_Events(dataFileName, cur):
     """ Add data to database by reading .txt file
    :param dataFileName: .txt file with data to be imported
     """           
     with open(dataFileName) as csv_file:
         csv_reader = csv.reader(csv_file, delimiter=',')
         for row in csv_reader:
             cur.execute("""SELECT Name
             FROM Events
             WHERE Name=?""",(row[0],))
             
             result = cur.fetchone()
             if result:
                 raise ValueError("Event Already in Database")
             else:
                 cur.execute("INSERT INTO Events VALUES (?,?,?,?)", row)
         
         print("Addition Successful") 
         csv_file.close()                 

def delete_Student(cur,id):
    """
    Delete a task by task id
    :param cur:  Cursor to the database
    :param id: id of the student to delete
    :return:
    """
    sql = 'DELETE FROM Students WHERE id=?'
    cur.execute(sql, (id,)) 
    print("Delete Successful")
    
def delete_Event(cur,name):
    """
    Delete a task by task id
    :param cur:  Cursor to the database
    :param name: name of the event to delete
    :return:
    """
    sql = 'DELETE FROM Events WHERE Name=?'
    cur.execute(sql, (name,)) 
    print("Delete Successful")
        
def get_Students(cur):
    cur.execute("SELECT * FROM Students")
    print(cur.fetchall())                
 
def get_Events(cur):
    cur.execute("SELECT * FROM Events")
    print(cur.fetchall()) 
    
def getSpecificYear(cur,year): 
    cur.execute("SELECT * FROM Students WHERE Year=?")
    print(cur.fetchall())
    
def exportDB(cur):
    student_data = cur.execute("SELECT * FROM Students")
    with open('studentData.csv', 'w') as f:
        writer = csv.writer(f)
        #writer.writerow(['Column 1', 'Column 2', ...])
        writer.writerows(student_data)
    f.close()
    
    event_data = cur.execute("SELECT * FROM Events")
    with open('eventData.csv', 'w') as g:
        writer = csv.writer(g)
        writer.writerows(event_data)
    g.close()  
    
def importDB(cur):
    root = Tk()
    file_path_students = filedialog.askopenfilename("Select Student Information")
    f=open(file_path_students,'r') # open the Student csv data file
    reader = csv.reader(f)
    for row in reader:
        cur.execute("INSERT INTO STUDENTS VALUES (?, ?, ?, ?, ?)", row)
    
    f.close()
    file_path_events = filedialog.askopenfilename("Select Event Information")
    g=open(file_path_events,'r') #open the Events csv data file
    event_reader = csv.reader(g)
    for row in event_reader:
        cur.execute("INSERT INTO EVENTS VALUES (?, ?, ?, ?)", row)
    g.close()

             
def main():
    database = "CSCI330.db"
    tableName = "Students"
    csvFile = "Test.csv"

    conn,cur = create_connection(database)
    
    #add_data_Students(csvFile, cur)
    
    #add_data_Events(events, cur)
    
    #delete_Student(cur,"12345")
    
    #get_Students(cur)
    
    #get_Events(cur)
    exportDB(cur)
    
    conn.commit()
    conn.close()
if __name__ == '__main__':
    main()