#from ast import Str
from ctypes import string_at
import pyswip 
from pyswip import Prolog
from pathlib import Path
prolog = Prolog()
prolog.consult("CovidKnowledgeBase.pl")

class Patient:
    def __init__(self,name,age,sex,temp,vax_status,symptom_set,systolic,diastolic):
        self.name=name
        self.age=age
        self.sex=sex
        self.temp = temp
        self.vax_status=vax_status
        self.symptom_set=symptom_set # This is a set to hold all checked symbols, the rest are strings
        self.diastolic = diastolic
        self.systolic = systolic
        self.numSymptoms = len(self.symptom_set) # number of symptoms of the patient

    def pinfo(self):
        
        print("Name: "+ self.name+'\n')
        print("Age: "+ self.age+'\n')
        print("Sex: "+ str(self.sex)+'\n')
        print("Vaccination Status: "+ str(self.vax_status) +'\n')
        print("Temperature: "+ str(self.temp)+ " C || "+str(toFarenheit(self.temp))+" F")
        if(self.systolic!=0 or self.diastolic !=0):
            print("Systolic Pressure: "+ str(self.systolic)+ " mm Hg")
            print("Diastolic Pressure: "+ str(self.diastolic)+ " mm Hg")
            #TODO: Add to the string here
        print("Symptoms:\n")
        for x in  self.symptom_set:#range(len(self.symptom_set)):
            #print("Symptom # "+str(x)+" "+ str(self.symptom_set[x])+ "\n");
            print(str(x))
        
        print("===============================\n")

    def pstring(self):
        string = ("\nName: "+ self.name+'\n')
        string+=("Age: "+ self.age+'\n')
        string+=("Sex: "+ str(self.sex)+'\n')
        string+=("Vaccination Status: "+ str(self.vax_status) +'\n')
        string+=("Temperature: "+ str(self.temp)+ " C || "+str(toFarenheit(self.temp))+" F\n")

        if(self.systolic!=0 or self.diastolic !=0):
                string+=("Systolic Pressure: "+ str(self.systolic)+ " mm Hg\n")
                string+=("Diastolic Pressure: "+ str(self.diastolic)+ " mm Hg\n")
        string+="Symptoms:\n"
        for x in  self.symptom_set:
            string+="\t"+str(x)+"\n"
        string+=("===============================\n")
        return string

    # list(prolog.query("father(michael,X)")) == [{'X': 'john'}, {'X': 'gina'}]
    # for soln in prolog.query("father(X,Y)"):
    #     print(soln["X"], "is the father of", soln["Y"])



    def prologanlyze(self): # Analyzes which strain the patient has
     #bool(list(prolog.query("covid_diag("+self.temp+","+stringStripper(self.symptom_set)+")")))) == True:
        results = list(prolog.query("covid_diag("+self.temp+","+stringStripper(self.symptom_set)+",X)"))
        for stuff in results:
            result = stuff["X"]
            break

        if(result == 1):
            print("You have mu")
        elif(result == 2):
            print("You have Delta")
        elif(result == 3):
            print("You have regular covid")
        else:
            print("You do not have covid :)")

        
        

    def PressureAnalyze(self): # Analyzes the blood pressure of the patient
        pass
    def SeverityAnalyze(self): # Analyzes severity of the patient
        pass
    def PatientSave(self,str_analysis): # Saves all patient data to a file
        pass

def StatsCalc(): # Reads patient data and recalculates the statistics; returns results in a string
    string = 'blank'
    return  string

def toFarenheit(celcius):  # converts from celcius to farenheit
    Farenheit = ((int(celcius) * 9)/5) +32 
    return Farenheit

def stringStripper(astring):
    strip = str(astring)[1:-1]
    strip = "["+strip+"]"
    return strip