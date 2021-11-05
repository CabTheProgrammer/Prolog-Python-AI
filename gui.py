import tkinter     # this is a gui library for python
from tkinter import *

#Sample run is to go in System Design.



#Initial Stuff
name = "Python Expert System"
window = tkinter.Tk()
window.title(name)
window.geometry("500x350")# Sets window size
window.minsize(width=500,height=250)

#boolean values for symptons
isDizzy = IntVar()
isFaint = IntVar()
isBV = IntVar()

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
#tired easily
#shortness of breath
#say something if pressure too high or too low 

# function here to display % of persons who have covid based on symptons
# Should break-down to show percentage with mild,percentage with severe
#percentage with Delta and percentage with Mu

#Basic Information
lbl_name = tkinter.Label(window,pady=10,text="Patient Name: ")
ent_name = tkinter.Entry(window)
lbl_age = tkinter.Label(window,pady=10,text="Patient Age: ")
ent_age = tkinter.Entry(window,width=3)


lbl_Temp = tkinter.Label(window,text="Temperature(C)")
ent_Tvalue = tkinter.Entry(window,width=3)
lbl_dizzy = tkinter.Label(window,text="Dizziness")
lbl_faint = tkinter.Label(window,text="Fainting")
lbl_BV = tkinter.Label(window,text="Blurred Vision")

def displayBP(): #Displays options to capture blood pressure should the user click any of the options
    if(isDizzy.get()==1 or isBV.get()==1 or isFaint.get()==1):
        lbl_dbv.grid(row=6,column=0)
        ent_dbv.grid(row=6,column=1)
        lbl_sbv.grid(row=7,column=0)
        ent_sbv.grid(row=7,column=1)
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


#Checkboxes for the last three
chb_dizzy = tkinter.Checkbutton(window, text="",variable=isDizzy,onvalue=1, offvalue=0,command=displayBP)
chb_faint= tkinter.Checkbutton(window, text="",variable=isFaint,onvalue=1, offvalue=0,command=displayBP)
chb_bv = tkinter.Checkbutton(window, text="",variable=isBV,onvalue=1, offvalue=0, command=displayBP)


btn_submit = tkinter.Button(window,text="Analyze!")
#For Blood Pressure, ONLY ask if patient is dizzy, faint or BV
lbl_dbv = tkinter.Label(window,text="Blood Pressure (diastolic)")
ent_dbv = tkinter.Entry(window,width=3)
lbl_sbv = tkinter.Label(window,text="Blood Pressure (systolic)")
ent_sbv = tkinter.Entry(window,width=3)





#Grid Section
lbl_name.grid(row =0,column = 0)
ent_name.grid(row=0,column = 1)

lbl_age.grid(row =1,column = 0)
ent_age.grid(row=1,column = 1)



lbl_Temp.grid(row=2,column=0)
ent_Tvalue.grid(row=2,column=1)

lbl_dizzy.grid(row=3,column=0)
chb_dizzy.grid(row=3,column=1)

lbl_faint.grid(row=4,column=0)
chb_faint.grid(row=4,column=1)

lbl_BV.grid(row=5,column=0)
chb_bv.grid(row=5,column=1)

btn_submit.grid(row=8,column=0)



window.bind()
window.mainloop()