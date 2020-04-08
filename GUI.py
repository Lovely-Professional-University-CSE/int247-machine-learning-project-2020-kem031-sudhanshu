#Tk class is used to create a root window
root = Tk()
root.configure(background='Ivory')

Symptom1 = StringVar()
Symptom1.set("Select Here")

Symptom2 = StringVar()
Symptom2.set("Select Here")

Symptom3 = StringVar()
Symptom3.set("Select Here")

Symptom4 = StringVar()
Symptom4.set("Select Here")

Symptom5 = StringVar()
Symptom5.set("Select Here")
Name = StringVar()

prev_win=None
def Reset():
    global prev_win

    Symptom1.set("Select Here")
    Symptom2.set("Select Here")
    Symptom3.set("Select Here")
    Symptom4.set("Select Here")
    Symptom5.set("Select Here")
    try:
        prev_win.destroy()
        prev_win=None
    except AttributeError:
        pass

from tkinter import messagebox
def Exit():
    qExit=messagebox.askyesno("System","Do you want to exit the system")
    
    if qExit:
        root.destroy()
        exit()

#Headings for the GUI written at the top of GUI
w2 = Label(root, justify=LEFT, text="Disease Predictor using Machine Learning", fg="Red", bg="White")
w2.config(font=("Times",30,"bold italic"))
w2.grid(row=1, column=0, columnspan=2, padx=100)
w2 = Label(root, justify=LEFT, text="Contributors: Sudhanshu,Rohan,Aditya", fg="Pink", bg="Blue")
w2.config(font=("Times",30,"bold italic"))
w2.grid(row=2, column=0, columnspan=2, padx=100)

#Label for the name
NameLb = Label(root, text="Name of the Patient", fg="Red", bg="Sky Blue")
NameLb.config(font=("Times",15,"bold italic"))
NameLb.grid(row=6, column=0, pady=15, sticky=W)

#Creating Labels for the symtoms
S1Lb = Label(root, text="Symptom 1", fg="Blue", bg="Pink")
S1Lb.config(font=("Times",15,"bold italic"))
S1Lb.grid(row=7, column=0, pady=10, sticky=W)

S2Lb = Label(root, text="Symptom 2", fg="Sky Blue", bg="Purple")
S2Lb.config(font=("Times",15,"bold italic"))
S2Lb.grid(row=8, column=0, pady=10, sticky=W)

S3Lb = Label(root, text="Symptom 3", fg="Green",bg="red")
S3Lb.config(font=("Times",15,"bold italic"))
S3Lb.grid(row=9, column=0, pady=10, sticky=W)

S4Lb = Label(root, text="Symptom 4", fg="blue", bg="Yellow")
S4Lb.config(font=("Times",15,"bold italic"))
S4Lb.grid(row=10, column=0, pady=10, sticky=W)

S5Lb = Label(root, text="Symptom 5", fg="purple", bg="light green")
S5Lb.config(font=("Times",15,"bold italic"))
S5Lb.grid(row=11, column=0, pady=10, sticky=W)

#Labels for the different algorithms
lrLb = Label(root, text="DecisionTree", fg="white", bg="red")
lrLb.config(font=("Times",15,"bold italic"))
lrLb.grid(row=15, column=0, pady=10,sticky=W)

destreeLb = Label(root, text="RandomForest", fg="Red", bg="Orange")
destreeLb.config(font=("Times",15,"bold italic"))
destreeLb.grid(row=17, column=0, pady=10, sticky=W)

ranfLb = Label(root, text="NaiveBayes", fg="White", bg="green")
ranfLb.config(font=("Times",15,"bold italic"))
ranfLb.grid(row=19, column=0, pady=10, sticky=W)

knnLb = Label(root, text="kNearestNeighbour", fg="Red", bg="Sky Blue")
knnLb.config(font=("Times",15,"bold italic"))
knnLb.grid(row=21, column=0, pady=10, sticky=W)
OPTIONS = sorted(l1)

#Taking name as input from user
NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1)

#Taking Symptoms as input from the dropdown from the user
S1 = OptionMenu(root, Symptom1,*OPTIONS)
S1.grid(row=7, column=1)

S2 = OptionMenu(root, Symptom2,*OPTIONS)
S2.grid(row=8, column=1)

S3 = OptionMenu(root, Symptom3,*OPTIONS)
S3.grid(row=9, column=1)

S4 = OptionMenu(root, Symptom4,*OPTIONS)
S4.grid(row=10, column=1)

S5 = OptionMenu(root, Symptom5,*OPTIONS)
S5.grid(row=11, column=1)

#Buttons for predicting the disease using different algorithms
dst = Button(root, text="Prediction 1", command=DecisionTree,bg="Red",fg="yellow")
dst.config(font=("Times",15,"bold italic"))
dst.grid(row=8, column=3,padx=10)

rnf = Button(root, text="Prediction 2", command=randomforest,bg="Purple",fg="green")
rnf.config(font=("Times",15,"bold italic"))
rnf.grid(row=9, column=3,padx=10)

lr = Button(root, text="Prediction 3", command=NaiveBayes,bg="Blue",fg="white")
lr.config(font=("Times",15,"bold italic"))
lr.grid(row=10, column=3,padx=10)

kn = Button(root, text="Prediction 4", command=KNN,bg="sky blue",fg="red")
kn.config(font=("Times",15,"bold italic"))
kn.grid(row=11, column=3,padx=10)

rs = Button(root,text="Reset Inputs", command=Reset,bg="Yellow",fg="purple")
rs.config(font=("Times",15,"bold italic"))
rs.grid(row=12,column=3,padx=10)

ex = Button(root,text="Exit System", command=Exit,bg="pink",fg="purple")
ex.config(font=("Times",15,"bold italic"))
ex.grid(row=13,column=3,padx=10)

#Showing the output of different aldorithms
t1 = Text(root, height=1, width=40,bg="Light green",fg="red")
t1.config(font=("Times",15,"bold italic"))
t1.grid(row=15, column=1, padx=10)

t2 = Text(root, height=1, width=40,bg="Purple",fg="Blue")
t2.config(font=("Times",15,"bold italic"))
t2.grid(row=17, column=1 , padx=10)

t3 = Text(root, height=1, width=40,bg="red",fg="orange")
t3.config(font=("Times",15,"bold italic"))
t3.grid(row=19, column=1 , padx=10)

t4 = Text(root, height=1, width=40,bg="Blue",fg="yellow")
t4.config(font=("Times",15,"bold italic"))
t4.grid(row=21, column=1 , padx=10)

#calling this function because the application is ready to run
root.mainloop()