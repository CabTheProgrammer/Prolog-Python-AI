# I want to use this file to calculate and store the statistics of the data collected by the system
from ctypes import create_string_buffer
import patient,pickle
import sqlite3
from sqlite3 import Error
import os

masterconn = None

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect("patient.db")
        print("Using "+sqlite3.version)
    except Error as e:
        print(e)
        
    return conn

def create_table(conn):
    createstatement ="""CREATE TABLE IF NOT EXISTS PatientData(
                        id integer PRIMARY KEY,
                        name text NOT NULL,
                        age integer,
                        temp real,
                        vaxstat text,
                        symptomset text,
                        diagnosis text,
                        severity text,
                        bpstat text,
                        recommend text);                                               
                        """
    try:
        c = conn.cursor()
        c.execute(createstatement)
        print("Table has been created")
    except Error as e:
        print(e)


def dbinit():
    masterconn = create_connection()
    create_table(masterconn)

def insertdata(name,age,temp,vaxstat,symptomset,diagnosis,severity,bpstat,recommend):
        sqliteConnection = sqlite3.connect('patient.db')
        cursor = sqliteConnection.cursor()
         
        dbstring = """INSERT INTO PatientData 
                        (name,age,temp,vaxstat,symptomset,diagnosis,severity,bpstat,recommend)
                        VALUES(?,?,?,?,?,?,?,?,?);"""
        data_tuple = (name,age,temp,vaxstat,symptomset,diagnosis,severity,bpstat,recommend) 
        
        cursor.execute(dbstring,data_tuple)
        sqliteConnection.commit()
        cursor.close()
        print("Record has been saved!")


#dbinit()
def symptomslicer(astring):
    astring = astring[1:-1]
    return astring.split(",")


def printall():
    masterstring = ""
    sqliteConnection = sqlite3.connect('patient.db')
    cursor = sqliteConnection.cursor()
    dbstring = """SELECT * FROM PatientData;"""
    
    cursor.execute(dbstring)
    records = cursor.fetchall()
    for row in records:
        masterstring+=("\nRecord#: "+str(row[0])+"\n")
        masterstring+=("Name: "+row[1]+"\n")
        masterstring+=("Age: "+str(row[2])+"\n")
        masterstring+=("Temperature: "+str(row[3])+" C \n")
        masterstring+=("Vaccination Status: "+row[4]+"\n")
        masterstring+=("Symptoms: \n")
        for symptom in symptomslicer(row[5]):
            masterstring+="\t "+symptom[1:-1]+"\n"
        masterstring+="\n"
        masterstring+="===============================\n"
        masterstring+="Analysis\n"
        masterstring+=("Diagnosis: "+row[6]+"\n")
        masterstring+=("Severity: "+row[7]+"\n")
        masterstring+=("Blood Pressure Analysis:: "+row[8]+"\n")
        masterstring+="===============================\n\n"


    sqliteConnection.commit()
    cursor.close()
    return masterstring

def statistic():
    masterstring = ""
    sqliteConnection = sqlite3.connect('patient.db')
    cursor = sqliteConnection.cursor()
    dbstring = """SELECT severity,COUNT(*),COUNT(*)*100/SUM(COUNT(*)) OVER () AS Percentage
                  FROM PatientData
                  GROUP BY severity
                ;"""

    cursor.execute(dbstring)
    records = cursor.fetchall()
    for row in records:
        masterstring+=("\nSeverity: "+ str(row[0])+" Count: "+ str(row[1])+" Percentage Cover "+str(row[2])+"%\n")


    sqliteConnection.commit()
    cursor.close()
    return masterstring    

def statistic2():
    masterstring = "\n\n===============================\n"
    masterstring += "COVID INFECTION VARIANCE\n"
    sqliteConnection = sqlite3.connect('patient.db')
    cursor = sqliteConnection.cursor()
    dbstring = """SELECT diagnosis,COUNT(*),COUNT(*)*100/SUM(COUNT(*)) OVER () AS Percentage
                  FROM PatientData
                  GROUP BY diagnosis
                ;"""

    cursor.execute(dbstring)
    records = cursor.fetchall()
    for row in records:
        masterstring+=("\nDiagnosis: "+ str(row[0])+" Count: "+ str(row[1])+" Percentage Cover "+str(row[2])+"%\n")


    sqliteConnection.commit()
    cursor.close()
    return masterstring    

  
