import tkinter     # this is a gui library for python
from tkinter import *

#Initial Stuff
name = "Python Expert System"
window = tkinter.Tk()
window.title(name)
window.geometry("600x500")# Sets window size
window.minsize(width=600,height=250)

#Section for various frames
basicinfo = Frame(window,borderwidth=2,relief=RIDGE)
basicinfo.grid(row=0,column=0)
symptoms = Frame(window,borderwidth=2,relief=RIDGE)
symptoms.grid(row=0,column=1,padx=5)

#boolean values for symptons
isDizzy = IntVar()
isFaint = IntVar()
isBV = IntVar()
sex=StringVar(value='male')
vax = IntVar() #1 if the person is vaccinated; 0 if they are not
isNausea = IntVar()
isshortofbreath = IntVar()
iseasilytired = IntVar()
#TODO: 
#Sample run is to go in System Design.
#Analyze should display likelihood patient has covid and add them to the knowledge base.
#View Statistics to show overall statistics.

#like if temp over 120, then they have mu for example(mu is the most serious one)
#nausea is a symptom of mu variant and not regular covid
#loss of speech or mobility, or confusion is a symptom of regular covid.
#set it so that you can only pick one or the other in terms of symptoms.
# Ask if person is vaccinated
#if temperature is lower with symptoms then it is probably delta(treat delta as the wimp one)

#General covid symptoms
#Over five symptoms checked or if they have a really high temperature then they are severe, otherwise they are mild

#other things to check for
#tired easily[x]
#shortness of breath[x]
#say something if pressure too high or too low 

# function here to display % of persons who have covid based on symptons
# Should break-down to show percentage with mild,percentage with severe
#percentage with Delta and percentage with Mu

#Basic Information
lbl_name = tkinter.Label(basicinfo,pady=10,text="Patient Name: ")
ent_name = tkinter.Entry(basicinfo)
lbl_age = tkinter.Label(basicinfo,pady=10,text="Patient Age: ")
ent_age = tkinter.Entry(basicinfo,width=3)
#Sex of Person
lbl_sex = tkinter.Label(basicinfo,pady=10,text="Sex: ")
rad_male = tkinter.Radiobutton(basicinfo, text="Male",variable=sex,value='male')
rad_female = tkinter.Radiobutton(basicinfo, text="Female",variable=sex,value='female')
#Vaccination Status
lbl_vax = tkinter.Label(basicinfo,pady=10,text="Vaccination Status")
rad_vax = tkinter.Radiobutton(basicinfo, text="Vaccinated",variable=vax,value=1)
rad_novax = tkinter.Radiobutton(basicinfo, text="Unvaccinated",variable=vax,value=0)


lbl_Temp = tkinter.Label(basicinfo,text="Temperature(C)")
ent_Tvalue = tkinter.Entry(basicinfo,width=3)

#Symptoms
lbl_dizzy = tkinter.Label(symptoms,text="Dizziness")
lbl_faint = tkinter.Label(symptoms,text="Fainting")
lbl_BV = tkinter.Label(symptoms,text="Blurred Vision")

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
    name = ent_name.get("1.0",END) # Captures text from input
    age = ent_age.get("1.0","end-1c")
    temp = ent_Tvalue.get("1.0",END)
    # TODO: Capture other values!


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


btn_submit = tkinter.Button(symptoms,text="Analyze!") #Adds patient's data to file and displays analysis results
btn_statistics = tkinter.Button(symptoms,text="Statistics!") # Displays overall statistics on screen
#For Blood Pressure, ONLY ask if patient is dizzy, faint or BV
lbl_dbv = tkinter.Label(symptoms,text="Blood Pressure (diastolic)")
ent_dbv = tkinter.Entry(symptoms,width=3)
lbl_sbv = tkinter.Label(symptoms,text="Blood Pressure (systolic)")
ent_sbv = tkinter.Entry(symptoms,width=3)





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



window.bind()
window.mainloop()