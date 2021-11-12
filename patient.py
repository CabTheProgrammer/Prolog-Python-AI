from ast import Str
import pyswip

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



def toFarenheit(celcius):  # converts from celcius to farenheit
    Farenheit = ((int(celcius) * 9)/5) +32 
    return Farenheit

