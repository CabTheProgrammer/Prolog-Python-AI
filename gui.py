import tkinter     # this is a gui library for python
import patient
import statsmanager
from tkinter import *


#Initial Stuff
name = "Python Expert System(PES)"
window = tkinter.Tk()
window.title(name)
window.geometry("600x500")# Sets window size
window.minsize(width=650,height=350)

#Section for various frames
basicinfo = Frame(window,borderwidth=2,relief=RIDGE)
basicinfo.grid(row=0,column=0)
symptoms = Frame(window,borderwidth=2,relief=RIDGE)
symptoms.grid(row=0,column=1,padx=5)
display = Frame(window,borderwidth=2,relief=RIDGE)
display.grid(row=2,columnspan = 2)


#boolean values for symptons
isDizzy = IntVar()
isFaint = IntVar()
isBV = IntVar()
sex=StringVar(value='male')
vax = StringVar(value='Unvaccinated') #1 if the person is vaccinated; 0 if they are not
isNausea = IntVar()
isshortofbreath = IntVar()
iseasilytired = IntVar()

#string variables

#TODO:
# Add a textbox to collect symptoms that are not there... 
#Normal Human Temperature: 37 Celcius or 98.6 Farenheit
#Sample run is to go in System Design.
#Write a reccomendation based on severity and strain.
#Analyze should display likelihood patient has covid and add them to the knowledge base.
#View Statistics to show overall statistics.

#like if temp over 120, then they have mu for example(mu is the most serious one)
#nausea is a symptom of mu variant and not regular covid
#loss of speech or mobility, or confusion is a symptom of regular covid.[IGNORE?]
#set it so that you can only pick one or the other in terms of symptoms.
# Ask if person is vaccinated
#if temperature is lower with symptoms then it is probably delta(treat delta as the wimp one)

#General covid symptoms
#Over five symptoms checked or if they have a really high temperature then they are severe, otherwise they are mild

#other things to check for
#tired easily[x]
#shortness of breath[x]
#say something if pressure too high or too low [x]

# function here to display % of persons who have covid based on symptons
# Should break-down to show percentage with mild,percentage with severe
#percentage with Delta and percentage with Mu

#Basic Information
lbl_name = tkinter.Label(basicinfo,pady=10,text="Patient Name: ")
ent_name = tkinter.Entry(basicinfo)
lbl_age = tkinter.Label(basicinfo,pady=10,text="Patient Age: ")
ent_age = tkinter.Entry(basicinfo,width=5)
#Sex of Person
lbl_sex = tkinter.Label(basicinfo,pady=10,text="Sex: ")
rad_male = tkinter.Radiobutton(basicinfo, text="Male",variable=sex,value='male')
rad_female = tkinter.Radiobutton(basicinfo, text="Female",variable=sex,value='female')
#Vaccination Status
lbl_vax = tkinter.Label(basicinfo,pady=10,text="Vaccination Status")
rad_vax = tkinter.Radiobutton(basicinfo, text="Vaccinated",variable=vax,value="Vaccinated")
rad_novax = tkinter.Radiobutton(basicinfo, text="Unvaccinated",variable=vax,value="Unvaccinated")


lbl_Temp = tkinter.Label(basicinfo,text="Temperature(C)")
ent_Tvalue = tkinter.Entry(basicinfo,width=5)

#Symptoms
lbl_dizzy = tkinter.Label(symptoms,text="Dizziness")
lbl_faint = tkinter.Label(symptoms,text="Fainting")
lbl_BV = tkinter.Label(symptoms,text="Blurred Vision")


#for output
txt_display = tkinter.Text(display,height=18,width=70)
txt_display.insert('1.35','===Analysis Output===')
txt_display['state']= 'disabled' #prevents user from editing text
# txt_display['state'] = 'normal' how to display text
txt_display.grid(row =0,column = 0)

def DisplayString(astring,flag): # Function to display stuff in the text box
    txt_display['state'] = 'normal'
    txt_display.delete('1.0', END) #clears display  
    if(flag == 1):
        txt_display.insert('1.35','===Analysis Output===')
    elif (flag == 2):
        txt_display.insert('1.35','===Recorded Patients===')
    else:
        txt_display.insert('1.35','===Patient Statistics===')


    txt_display.insert('2.0',astring)
    txt_display['state']= 'disabled'

def displayBP(): #Displays options to capture blood pressure should the user click any of the options
    if(isDizzy.get()==1 or isBV.get()==1 or isFaint.get()==1):
        lbl_dbv.grid(row=8,column=0)
        ent_dbv.grid(row=8,column=1)
        lbl_sbv.grid(row=9,column=0)
        ent_sbv.grid(row=9,column=1)
    else:
        lbl_dbv.grid_forget()
        ent_dbv.grid_forget()
        lbl_sbv.grid_forget()
        ent_sbv.grid_forget()

def gatherinput():
    name =ent_name.get() #pname #ent_name.get("1.0","end-1c") # Captures text from input
    age = ent_age.get()
    temp = ent_Tvalue.get()
    symptoms = set()

    diastolic = 0
    systolic = 0
    
    if(isDizzy.get()==1 or isBV.get()==1 or isFaint.get()==1):
         diastolic = ent_dbv.get()
         systolic = ent_sbv.get()


    if(isDizzy.get() == 1):
        symptoms.add("Dizzy")
    if(isFaint.get() == 1):
        symptoms.add("Faint")
    if(isBV.get() == 1):
        symptoms.add("Blurred Vision")
    if(isNausea.get() == 1):
        symptoms.add("Nausea")
    if(isBV.get() == 1):
        symptoms.add("Blurred Vision")
    if(isshortofbreath.get() == 1):
        symptoms.add("Short of Breath")
    if(iseasilytired.get() == 1):
        symptoms.add("Easily Tired") 
        

    p1 = patient.Patient(name,age,sex.get(),temp,vax.get(),symptoms,systolic,diastolic)
    #p1.pinfo()
    #p1.prologanlyze()
    #p1.PressureAnalyze()
    DisplayString(p1.pstring(),1)
    #p1.PatientSave()
    
 
def printall():
    DisplayString(statsmanager.printall(),1)
def statistic():
     DisplayString(statsmanager.statistic()+statsmanager.statistic2(),3)

#Checkboxes for the rest
chb_dizzy = tkinter.Checkbutton(symptoms, text="",variable=isDizzy,onvalue=1, offvalue=0,command=displayBP)
chb_faint= tkinter.Checkbutton(symptoms, text="",variable=isFaint,onvalue=1, offvalue=0,command=displayBP)
chb_bv = tkinter.Checkbutton(symptoms,variable=isBV,onvalue=1, offvalue=0, command=displayBP)

chb_nausea = tkinter.Checkbutton(symptoms, text="",variable=isNausea,onvalue=1, offvalue=0, command=displayBP)
chb_shortbreath = tkinter.Checkbutton(symptoms, text="",variable=isshortofbreath,onvalue=1, offvalue=0, command=displayBP)
chb_easily = tkinter.Checkbutton(symptoms, text="",variable=iseasilytired,onvalue=1, offvalue=0, command=displayBP)

lbl_nausea = tkinter.Label(symptoms,text="Feelings of Nausea")
lbl_shortbreath = tkinter.Label(symptoms,text="Short of Breath")
lbl_easily = tkinter.Label(symptoms,text="Easily tired")


btn_submit = tkinter.Button(symptoms,text="Analyze",command = gatherinput) #Adds patient's data to file and displays analysis results
btn_statistics = tkinter.Button(symptoms,text="Statistics",command = statistic) # Displays overall statistics on screen
btn_viewpatients = tkinter.Button(symptoms,text="View Patients",command = printall) # Displays overall statistics on screen
#For Blood Pressure, ONLY ask if patient is dizzy, faint or BV
lbl_dbv = tkinter.Label(symptoms,text="Blood Pressure (diastolic)")
ent_dbv = tkinter.Entry(symptoms,width=5)
lbl_sbv = tkinter.Label(symptoms,text="Blood Pressure (systolic)")
ent_sbv = tkinter.Entry(symptoms,width=5)





#Grid Section
lbl_name.grid(row =0,column = 0)
ent_name.grid(row=0,column = 1)

lbl_age.grid(row =1,column = 0)
ent_age.grid(row=1,column = 1)

lbl_sex.grid(row=2,column=0) 
rad_male.grid(row=2,column=1)
rad_female.grid(row=2,column=2)

lbl_vax.grid(row=3,column=0) 
rad_vax.grid(row=3,column=1)
rad_novax.grid(row=3,column=2)

lbl_Temp.grid(row=4,column=0)
ent_Tvalue.grid(row=4,column=1)

lbl_dizzy.grid(row=5,column=0)
chb_dizzy.grid(row=5,column=1)

lbl_faint.grid(row=6,column=0)
chb_faint.grid(row=6,column=1)

lbl_BV.grid(row=7,column=0)
chb_bv.grid(row=7,column=1)

lbl_nausea.grid(row=10,column=0)
chb_nausea.grid(row=10,column=1)

lbl_shortbreath.grid(row=11,column=0)
chb_shortbreath.grid(row=11,column=1)

lbl_easily.grid(row=12,column=0)
chb_easily.grid(row=12,column=1)


btn_submit.grid(row=13,column=0)
btn_statistics.grid(row=13,column=2)
btn_viewpatients.grid(row=13,column=3)


window.bind()
window.mainloop()