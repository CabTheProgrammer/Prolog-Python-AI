import tkinter     # this is a gui library for python
from tkinter import *

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



# function here to display % of persons who have covid based on symptons
# Should break-down to show percentage with mild,percentage with severe
#percentage with Delta and percentage with Mu

lbl_Temp = tkinter.Label(window,text="Temperature(C)")
ent_Tvalue = tkinter.Entry(window,width=3)
lbl_dizzy = tkinter.Label(window,text="Dizziness")
lbl_faint = tkinter.Label(window,text="Fainting")
lbl_BV = tkinter.Label(window,text="Blurred Vision")

#Checkboxes for the last three
chb_dizzy = tkinter.Checkbutton(window, text="Dizzy",variable=isDizzy,onvalue=1, offvalue=0)
chb_faint= tkinter.Checkbutton(window, text="Faint",variable=isFaint,onvalue=1, offvalue=0)
chb_bv = tkinter.Checkbutton(window, text="Blurred Vision",variable=isBV,onvalue=1, offvalue=0)

#For Blood Pressure, ONLY ask if patient is dizzy, faint or BV






#Grid Section
lbl_Temp.grid(row=0,column=0)
ent_Tvalue.grid(row=0,column=1)
#lbl_dizzy.grid(row=1,column=0)
chb_dizzy.grid(row=1,column=0)
chb_faint.grid(row=2,column=0)
chb_bv.grid(row=3,column=0)
#lbl_faint.grid(row=2,column=0)
#lbl_BV.grid(row=3,column=0)


window.mainloop()