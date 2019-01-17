'''import tkinter as tk 
r = tk.Tk() 
r.title('XGBBoost')
 







def wait(): 
	main= Tk() 
	ourMessage ='This is our Message'
	messageVar = Message(main, text = ourMessage) 
	messageVar.config(bg='lightgreen') 
	messageVar.pack( ) 

button = tk.Button(r, text='Stop', width=25, command=wait()) 
button.pack() 
r.mainloop() 

'''

# -*- coding: utf-8 -*-

# Python program to  create a simple GUI  
# calculator using Tkinter 
  
# import everything from tkinter module 
from tkinter import *
  
# globally declare the expression variable 
expression = "" 
  
  
# Function to update expressiom 
# in the text entry box 
def press(num): 
    # point out the global expression variable 
    global expression 
  
    # concatenation of string 
    expression = expression + str(num) 
  
    # update the expression by using set method 
    equation.set(expression) 
  
  
# Function to evaluate the final expression 
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
  
    # Put that code inside the try block 
    # which may generate the error 
    try: 
  
        global expression 
  
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression)) 
  
        equation.set(total) 
  
        # initialze the expression variable 
        # by empty string 
        expression = "" 
  
    # if error is generate then handle 
    # by the except block 
    except: 
  
        equation.set(" error ") 
        expression = "" 
  


def start():
#	try:
		equation.set("Please Wait.......")


		import numpy as np
		import pandas as pd
		from xgboost import XGBClassifier
		from sklearn.model_selection import train_test_split
		from sklearn.metrics import accuracy_score
		data = pd.read_csv("assignment/train.csv")
		testdata = pd.read_csv("assignment/test.csv")
		
		testdata.FeaB = testdata.FeaB.fillna("0")
		testdata["FeaB"] = testdata.FeaB.astype(float)
		testdatacopy = testdata
		testdata = testdata.drop("Timestamp",axis=1)
		
		#print(testdata.FeaA)
		Y_train = data.Label
		X_train = data.drop("Timestamp",axis=1)
		X_train = X_train.drop("Label",axis=1)
	
		X_train, X_test, y_train, y_test = train_test_split(X_train, Y_train, test_size=0.01, random_state=10)
		# fit model no training data
		model = XGBClassifier()
		model.fit(X_train, y_train)
		# make predictions for test data
		y_pred = model.predict(testdata)
		predictions = [round(value) for value in y_pred]
	
		predc = predictions
		testc = testdatacopy
	
		testc['Label'] = predc
	
		testc.to_csv("Predicted.csv", sep='\t', encoding='utf-8')
		equation.set("Prediction Completed  Filename:- Prediced.csv")
	
	# if error is generate then handle 
        # by the except block 
#        except:
#	       	equation.set(" error ") 	  
	
  
# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 
  
    # set the background colour of GUI window 
    gui.configure(background="light green") 
  
    # set the title of GUI window 
    gui.title("XGBoost") 
  
    # set the configuration of GUI window 
    gui.geometry("500x200") 
  
    # StringVar() is the variable class 
    # we create an instance of this class 
    equation = StringVar() 
  
    # create the text entry box for 
    # showing the expression . 
    padding = Message(gui)
    padding.config(background="light green")
    padding.grid(columnspan = 20,ipadx = 10)


    expression_field = Message(gui, textvariable = equation) 
    expression_field.config(width=500)
    expression_field.grid(rowspan=5)
  



    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    expression_field.grid(columnspan=20, ipadx=200) 
  
    equation.set('Start Prediction ') 
  
    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed . 
    button1 = Button(gui, text='Start', fg='black', bg='red',command=start, height=1, width=20) 
    button1.grid(row=10, column=0,rowspan=10,columnspan=200) 

  
    stop = Button(gui, text='Stop', fg='black', bg='red',command=gui.destroy, height=1, width=20) 
    stop.grid(row=20, column=0,rowspan=10,columnspan=20) 
    #padding.grid(row=5,column=10)
    # start the GUI 
    gui.mainloop()


