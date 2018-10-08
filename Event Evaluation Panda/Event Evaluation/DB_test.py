'''
Created on Oct 4, 2018

@author: ZakLuetmer
'''
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        database = "CSCI330.db"
        conn= sqlite3.connect(database)
        cur = conn.cursor() 
        


    def tearDown(self):
        conn.close()


    def test_add_Students(self):
        with open('test.csv','a') as fd:
            fd.write("00000, Fake, Student, None, 0")
        string = add_data_Students("test.csv",cur)
        self.assertEqual("Addition Successful",string)
        delete_Student(cur,"00000")
        
    def test_add_Events(self):
        with open('TestEvents.csv','a') as fd:
            fd.write("TestEvent")
        string = add_data_Events("testEvent.csv",cur)
        self.assertEqual("Addition Successful",string)
        delete_Event(cur,"TestEvent")
        
    def test_delete_Student(self):
        cur.execute("INSERT INTO Students VALUES (00000, Fake, Student, None, 0)")
        string = delete_Student(cur,"00000")
        self.assertEqual(string, "Delete Successful")
        
    def test_delete_Event(self):
        cur.execute("INSERT INTO Events VALUES (TestEvent)")
        string = delete_Student(cur,"TestEvent")
        self.assertEqual(string, "Delete Successful")
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()