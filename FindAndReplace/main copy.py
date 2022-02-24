#Find & Replace Project
#Code: 0839175
#Name: Jessica Alvarez

#Import tkinter class to use it
from tkinter import *
from tkinter import ttk

#Create GUI window with a title
jess175 = Tk(className="Find & Replace - Created By Jessica Alvarez")
#Set Width and Height
jess175.geometry("400x200")

#Create Form - Step 1
myLabelFind175 = Label(jess175, text="Find:")
myInputFind175 = Entry(jess175)
myLabelReplace175 = Label(jess175,text="Replace:")
myInputReplace175 = Entry(jess175)

#Add buttons Find and Find All - Step 2
myButtonFind175 = Button(jess175,text="Find", width="7")
myButtonFindAll175 = Button(jess175,text="Find All", width="7")

#Add buttons Replace and Replace All - Step 3
myButtonReplace175 = Button(jess175,text="Replace", width="7")
myButtonReplaceAll175 = Button(jess175,text="Replace All", width="7")

#Add Checkboxes - Step 4
myCheckMatchWhole175 = ttk.Checkbutton(jess175, text="Match whole word only")


#Add elements to the Window
myLabelFind175.grid(column=0, row=0)
myInputFind175.grid(column=1, row=0)
myLabelReplace175.grid(column=0, row=1)
myInputReplace175.grid(column=1, row=1)
myButtonFind175.grid(column=2,row=0)
myButtonFindAll175.grid(column=2, row=1)
myButtonReplace175.grid(column=2,row=2)
myButtonReplaceAll175.grid(column=2, row=3)
myCheckMatchWhole175.grid(column=1, row=2)


#Run the interface
jess175.mainloop()