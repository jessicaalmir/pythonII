#Find & Replace Project
#Code: 0839175
#Name: Jessica Alvarez

#Import tkinter class to use it
import tkinter
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
myButtonFind175 = ttk.Button(jess175,text="Find", width="7")
myButtonFindAll175 = ttk.Button(jess175,text="Find All", width="7")

#Add buttons Replace and Replace All - Step 3
myButtonReplace175 = ttk.Button(jess175,text="Replace", width="7")
myButtonReplaceAll175 = ttk.Button(jess175,text="Replace All", width="7")

#Add Checkboxes - Step 4
myCheckMatchWhole175 = ttk.Checkbutton(jess175, text="Match whole word only")
myCheckMatchCase175 = ttk.Checkbutton(jess175, text="Match Case")
myCheckWrapAround175 = ttk.Checkbutton(jess175, text="Wrap Around")

#Add Radiobuttons - Step 5
myLabelDirection175 = Label(jess175,text="Direction:")
myRadioUp175 = ttk.Radiobutton(jess175, text="Up")
myRadioDown175 = ttk.Radiobutton(jess175, text="Down")

#Add elements to the Window
myLabelFind175.grid(column=0, row=0, sticky=tkinter.E) #Align rigth/est
myInputFind175.grid(column=1, row=0, columnspan=3, sticky='WE') #fill the colunm width
myLabelReplace175.grid(column=0, row=1, sticky=tkinter.E) #Align rigth/est
myInputReplace175.grid(column=1, row=1, columnspan=3, sticky='WE')#fill the colunm width
myButtonFind175.grid(column=4,row=0, sticky=tkinter.W) #Align letf/west
myButtonFindAll175.grid(column=4, row=1, sticky=tkinter.W) #Align letf/west
myButtonReplace175.grid(column=4,row=2, sticky=tkinter.W) #Align letf/west
myButtonReplaceAll175.grid(column=4, row=3, sticky=tkinter.W) #Align letf/west
myCheckMatchWhole175.grid(column=1, row=2, sticky=tkinter.W) #Align letf/west
myCheckMatchCase175.grid(column=1, row=3, sticky=tkinter.W) #Align letf/west
myCheckWrapAround175.grid(column=1, row=4, sticky=tkinter.W) #Align letf/west
myLabelDirection175.grid(column=2, row=2)
myRadioUp175.grid(column=2, row=3)
myRadioDown175.grid(column=3, row=3)

#Run the interface
jess175.mainloop()