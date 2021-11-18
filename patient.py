#from ast import Str
import os 
import pickle
import pyswip
import statsmanager

from ctypes import string_at 
from pyswip import Prolog
from pathlib import Path

prolog = Prolog()
prolog.consult("CovidKnowledgeBase.pl")

PatientList = []
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

        self.numSymptoms = len(self.symptom_set) # number of symptoms of the patient, is this needed tho?
        self.diagnosis = ""
        self.severity = ""
        self.bpstat = ""
        self.recommend = ""

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
        string+=("Temperature: "+ str(self.temp)+ " C\n")

        if(self.systolic!=0 or self.diastolic !=0):
                string+=("Systolic Pressure: "+ str(self.systolic)+ " mm Hg\n")
                string+=("Diastolic Pressure: "+ str(self.diastolic)+ " mm Hg\n")
        string+="Symptoms:\n"
        for x in  self.symptom_set:
            string+="\t"+str(x)+"\n"
        string+=("===============================\n")

        analysis = "Analysis\n"
        analysis += "Diagnosis: "+self.prologanlyze()+"\n"
        analysis += "Severity: "+self.SeverityAnalyze()+"\n"
        analysis += "Blood Pressure Analysis: "+self.PressureAnalyze()+"\n"
        
        self.recommendation()
        self.PatientSave()
        print("Patient Data has been saved")
        return string+analysis+self.recommend

    def prologanlyze(self): # Analyzes which strain the patient has
        results = list(prolog.query("covid_diag("+self.temp+","+stringStripper(self.symptom_set)+",X)"))
        for stuff in results:
            result = stuff["X"]
            break

        if(result == 1):
            self.diagnosis = "Mu Variant"
        elif(result == 2):
           self.diagnosis = "Delta Variant"
        elif(result == 3):
            self.diagnosis = "Original Strain(Covid-19)"
        else:
             self.diagnosis = "Covid-19 Negative"
        return self.diagnosis
        
    def PressureAnalyze(self): # Analyzes the blood pressure of the patient
        results = list(prolog.query("blood_pressure_warn("+str(self.systolic)+","+str(self.diastolic)+",X)"))
        for stuff in results:
            result = stuff["X"]
            break

        if(result == 1):
            self.bpstat = "Low"
        elif(result == 2):
           self.bpstat = "Normal"
        else:
            self.bpstat = "High"
        if(self.systolic == 0 and self.diastolic == 0):
            return "UNKNOWN"
        else:
            return self.bpstat
        
    def SeverityAnalyze(self): # Analyzes severity of the patient
        results = list(prolog.query("severity("+str(self.temp)+","+str(len(self.symptom_set))+",X)"))
        for stuff in results:
            result = stuff["X"]
            break
        if (result == 1):
            self.severity = "Severe"
        else:
            self.severity = "Non-Severe" 
        return self.severity

    def recommendation(self):
        self.recommend = "Recommendation\n"
        self.recommend+=("===============================\n")
        #section for covid variant and severity
        if(self.diagnosis == "Mu Variant" or  self.diagnosis == "Delta Variant" or self.diagnosis == "Original Strain(Covid-19)" and self.serverity == "Severe"):
            self.recommend += """Patient may have a possible strain of corona virus \n based on symptoms, is in a severe condition
                              \n Short Term Recommendations: Patient should be tested for covid\n and seek medical attention urgently 
                              \n Long Term Recommendations:  Patient should prepare for a hospital stay\n"""
        elif(self.diagnosis == "Mu Variant" or  self.diagnosis == "Delta Variant" or self.diagnosis == "Original Strain(Covid-19)" and self.serverity == "Non-Severe" ):
            self.recommend += """Patient may have a possible strain of corona virus \n  based on symptoms, is in a non-severe condition
                              \n Short Term Recommendations: Patient should be tested for covid and seek to stay at home as much as possible while recovering
                              \n Long Term Recommendations:  If conditions worsens, patient should seek medical attention urgently\n"""
        else:
            self.recommend+= """Patient does not display any symptoms of covid-19,\n please monitor to be sure"""
        #section for persons with high, low or normal blood pressure
        if(self.bpstat == "Low"):
            self.recommend += "\nWARNING! PATIENT HAS LOW BLOOD PRESSURE!\n"
        elif(self.bpstat == "High"):
            self.recommend += "\nWARNING! PATIENT HAS HIGH BLOOD PRESSURE!\n"
        elif(self.bpstat == "Normal"):
            self.recommend+= "\nBlood Pressure appears to be normal\n"
        else:
            self.recommend+="\nBlood Pressure was not taken\n"

    def PatientSave(self): # saves patient object to file   
        if not(os.path.exists('./patient.db')):
            statsmanager.dbinit()
        statsmanager.insertdata(self.name,self.age,self.temp,self.vax_status,str(self.symptom_set),self.diagnosis,self.severity,self.bpstat,self.recommend)
        
       

def toFarenheit(celcius):  # converts from celcius to farenheit
    Farenheit = ((float(celcius) * 9)/5) +32 
    return Farenheit

def stringStripper(astring):
    strip = str(astring)[1:-1]
    strip = "["+strip+"]"
    return strip