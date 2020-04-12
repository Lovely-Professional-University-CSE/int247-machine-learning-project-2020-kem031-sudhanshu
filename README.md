# Machine Learning Project on Disease Predictions using Symptoms
# Problem Statement 
Health information needs are also changing the information seeking behavior and can be 
observed around the globe. Challenges faced by many people are looking online for health 
information regarding diseases, diagnoses and different treatments. If a recommendation system 
can be made for doctors and medicine while using review mining will save a lot of time. In this 
type of system, the user face problem in understanding the heterogeneous medical vocabulary as 
the users are laymen. User is confused because a large amount of medical information on 
different mediums are available.The idea behind recommender system is to adapt to cope with the special requirements of the health domain related with users.

# Registration Number
* 11716071-Sudhanshu Agrawal
* 11716106-Rohan Agrawal
* 11716665-Aditya Arya

# Visit Website
https://sites.google.com/view/mlprojectdiseaseprediction/documentation
![](https://github.com/Lovely-Professional-University-CSE/int247-machine-learning-project-2020-kem031-sudhanshu/blob/master/WebsiteLink/Capture.PNG)

# Explanation of Files
## training.csv
* This is the main dataset which has been used in this project. This dataset consist of mainly two columns "Disease" and "Symptoms" but this dataset is preprocessed so it helps in easily clasifying the data. This dataset is used to train our model.

## testing.csv
* This is the dataset which has been used to test our model so that we can know the accuracy of our model. this dataset is predefined with output.

## Compiled_Report.pdf
* This is the complete explaination of Each and every module implemented in software. You can refer to the pdf for the detailed explaination of every part.

## PythonCodeOfAlgorithm.py
This is the file which consist of dataset and there are various differnt algorithms used for training of our model which are as follows:
* Decision Tree 
* Random Forest
* KNearestNeighbour
* Naive Bayes
These four algorithms is used to train our model and all gives an accuracy of over 90

## Database
The database used in this project is "sqlite" whose name is database.db which consist of four tables in which we have shown the results of four different algorithms.we are saving the results of users with their names for future preferences.
![](https://github.com/Lovely-Professional-University-CSE/int247-machine-learning-project-2020-kem031-sudhanshu/blob/master/Database/db1.jpeg)

## GUI.py
This is the file which is used to create the interface of our system.GUI stands for Graphical User Interface and to create it we have used Tkinter which gives a software kind of view to our project where user can directly interact with the system by entering the symptoms of dieases and he/she will get the disease through various algorithms.

## Project_ML.ipynb
This is the jupyter notebook which consist of complete code. This is used to explain the working of each and every module used in the project.

## GUI.jpeg
This file contains the screenshot of the built GUI which shows the working of the system

# Working with GUI
## Step 1:
Enter the name in the provided space infront of the label as "Name of the Patient". It is the mandatory field which user have to enter in order to get result.
## Step 2:
Select 5 Symptoms from the dropdown menu which are labelled as Symptom 1, Symptom 2, Symptom 3, Symptom 4, Symptom 5 respectively. If user is not aware of 5 symptoms then it is mandatory for him to enter atleast 2 starting systems, otherwise the result will not come and a message box will pop up for the same
## Step 3:
As per user interest,he/she can predict the disease using different algorithms such as Decision tree algorithm, Random forest algorithm, Naive bayes algorithm and K-Nearest neighbour. According to algorithm click on buttons:</br>
Press Prediction 1 for Decision tree algorithm</br>
Press Prediction 2 for Random forest algorithm</br>
Press Prediction 3 for Naive bayes algorithm</br>
Press Prediction 4 for K-Nearest neighbour</br>
(User can predict the disease using  more than one algorithm at a time)
## Step 4:
Disease Recommendation will be available infront of the  labels of algorithm of user's choice.
## Step 5:
Click on "Reset" button to predict the disease for any other patient or Press "Exit System" button to come out of the GUI.

# A picture of GUI Interface
![](https://github.com/Lovely-Professional-University-CSE/int247-machine-learning-project-2020-kem031-sudhanshu/blob/master/GUI/GUI.PNG)
