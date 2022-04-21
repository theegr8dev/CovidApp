import sys 
import uuid
import pyodbc
import json
import pandas as pd
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget
from data import Country
from data import History
from data import Global


# connecting to my database
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-DLCPHPP\SQLEXPRESS;'
                      'Database=PythonProject;'
                     'Trusted_Connection=yes;')
cursor = conn.cursor()



# create a welcome class.
class welcomeScreen(QDialog):
    def __init__(self):
        super(welcomeScreen, self).__init__()
        loadUi("C:\\Python310\\CovidApp-Project\\UI\\welcomeScreen.ui", self) # loading the ui of the page
            
        self.welcomeLogin.clicked.connect(self.gotoLogin) # when the login button is clicked it will redirect to login page
        self.welcomeSignup.clicked.connect(self.gotoSignup) # when the create account button is clicked it will redirect to sign up age
        

    # slot that  allow login screen to be open from welcome screen
    def gotoLogin(self):
        login = LoginScreen() # creating and object of the login screen
        widget.addWidget(login) # adding the screen to stack
        widget.setCurrentIndex(widget.currentIndex()+1) # chaning the index once the screen is change to login screen
        
    # slot allow signup screen to be open from welcome screen    
    def gotoSignup(self):
        Signup = SignupScreen() # creating and object of the signup screen
        widget.addWidget(Signup) # adding the screen to stack
        widget.setCurrentIndex(widget.currentIndex()+1) # chaning the index once the screen is change to signup screen
        
# create a Signup class..
class SignupScreen(QDialog):
    def __init__(self):
        super(SignupScreen, self).__init__()
        loadUi("C:\\Python310\\CovidApp-Project\\UI\\signup2.ui", self) # loading the signup ui
        self.signup.clicked.connect(self.successSignup) # a click signal that successfully sign user up 
        self.backtoLogin.clicked.connect(self.goBackToLoginFromSignup) # a click signal that takes user to login when done signing up..
        self.signPasswordField.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password) # hashing the password inputed by user
        self.signConPasswordField.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password) # hashing the Confirm password inputed by user
    
    # validing user inputs
    def successSignup(self):
        id = uuid.uuid4() # generating random id for by database..
        firstname = self.fnameField.text().strip() # saving my user firstname input in a variable and removing the whitespaces 
        lastname = self.lnameField.text().strip() # saving my user lastbname input in a variable and removing the whitespaces 
        email = self.signEmailField.text().strip() # saving my user email input in a variable and removing the whitespaces 
        country = self.countryField.text().strip() # saving my user country input in a variable and removing the whitespaces 
        password = self.signPasswordField.text().strip() # saving my user password input in a variable and removing the whitespaces 
        confirmPassword = self.signConPasswordField.text().strip() # saving my user confirm password input in a variable and removing the whitespaces 

         
        if len(firstname) == 0 or len(lastname) == 0 or len(email) == 0 or len(country) == 0 or len(password) == 0 or len(confirmPassword) == 0: # checking if the user input are not empty
            self.signupErrorMessage.setText("Please input all fields") # displaying an error messsage if they are empty..
        else:
            self.signupErrorMessage.setText("") 
            
            if (password ==  confirmPassword): # checking if the password is same as the confirm password
                # catching this error shoudld in case the user enter an existing email in my database... 
                try: 
                    # saving my user data in a database..
                    InsertQuery = ("INSERT INTO CovidAuthentication (ID, Firstname, Lastname, Email, Country, Password) VALUES(?, ?, ?, ?, ?, ?)")
                    InsertValues = (id,firstname, lastname, email,country, password)                                      
                    cursor.execute(InsertQuery, InsertValues)
                    conn.commit()
                    print(cursor.rowcount, "record inserted.")
                    self.duplicateEmail.setText("")
                except:
                    self.duplicateEmail.setText("Email is already in use")
                    

            else:
                self.signupErrorMessage.setText("incorrect password")
                self.duplicateEmail.setText("")
                    
    # allow login screen to be open from Signup screen            
    def goBackToLoginFromSignup(self):
        backToLogin = LoginScreen() # creating and object of the login screen
        widget.addWidget(backToLogin)  # adding the screen to stack
        widget.setCurrentIndex(widget.currentIndex()+1) # chaning the index once the screen is change to login screen
    
# Login Class        
class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("C:\\Python310\\CovidApp-Project\\UI\\Login2.ui", self) # laoding my login ui..
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password) # hashing my login details
        self.login.clicked.connect(self.successLogin) # a click signal that successfully log user in
        self.backtoSignup.clicked.connect(self.goBackToSignupFromLogin) # a click signal that successfully take user back to sign up 
        self.forgotPassword.clicked.connect(self.gotoUpdatePassword)  # a click signal that successfully take user back to update password if forgotten       
        
    # loginning user into the app..
    def successLogin(self):
        email = self.emailField.text().strip() # saving my user email input in a variable and removing the whitespaces 
        password = self.passwordField.text().strip() # saving my user password input in a variable and removing the whitespaces 
        
        
        # checking if the user is valid..
        if len(email) == 0 or len(password) == 0:
            self.errorMessage.setText("Please input all fields") # checking if the user input are not empty
        else:
           # query the data with the user email
           self.errorMessage.setText("")
           SelectQuery = ("SELECT Email, Password, country FROM CovidAuthentication WHERE (Email = ?)")
           cursor.execute(SelectQuery, email)
           row = cursor.fetchall()
           
           # if row as values check if the user is the owner of the input password 
           if (row):
            self.emailErrorMessage.setText("")
            for i in row:
                #print(i)           
                if (password in i):
                    self.gotoMainScreen()
                else:
                    self.errorMessage.setText("Incorrect Password")
           else:
            self.emailErrorMessage.setText("Invalid Email") # rows is false that is  the email is not seen in the database
            


    # allow signup screen to be open from updatePassword             
    def goBackToSignupFromLogin(self):
        backToSignup = SignupScreen()  # creating and object of the signup screen
        widget.addWidget(backToSignup) # adding the screen to stack
        widget.setCurrentIndex(widget.currentIndex()+1) # chaning the index once the screen is change to signup screen
    
    # allow upadtePassword screen to be open from updatePassword     
    def gotoUpdatePassword(self):
        updatePassword = UpdatePassword()  # creating and object of the updatePassword screen
        widget.addWidget(updatePassword) # adding the screen to stack
        widget.setCurrentIndex(widget.currentIndex()+1) # chaning the index once the screen is change to updatePassword screen
        

    def gotoMainScreen(self):
        self.mainScreen = MainScreen()
        widget.addWidget(self.mainScreen)
        widget.setCurrentIndex(widget.currentIndex()+1)


       
class MainScreen(QDialog):
    def __init__(self):
        super(MainScreen, self).__init__()
        loadUi("C:\\Python310\\CovidApp-Project\\UI\\main.ui", self)
        self.searchBtn.clicked.connect(self.search)
        
        globals = Global()
        globalData = json.loads(globals)
        population = str(globalData['data']['population'])
        
        
        self.poulationLabel.setText(str(globalData['data']['population']))
        self.confirmedLabel.setText(str(globalData['data']['cases']))
        self.deathLabel.setText(str(globalData['data']['deaths']))
        self.recoveryLabel.setText(str(globalData['data']['recovered']))
        self.activeLabel.setText(str(globalData['data']['active']))
        self.sampleLabel.setText(str(globalData['data']['tests']))
        
      
        getCountry = Country()
        countryData = json.loads(getCountry)
        self.countryBox.addItems(countryData['response'])
        
    def search(self):
        date = self.dateEdit.text().strip()
        country = str(self.countryBox.currentText())   
        
        h = History(country, date)
        data = json.loads(h) 
    
        try:
            self.dateError.setText('')
            print('yes')
            print(data['response'][-1]['population'])
            print(data['response'][-1]['cases']['total'])
            
            self.poulationLabel.setText(str(data['response'][-1]['population']))
            self.confirmedLabel.setText(str(data['response'][-1]['cases']['total']))
            self.deathLabel.setText(str(data['response'][-1]['deaths']['total']))
            self.recoveryLabel.setText(str(data['response'][-1]['cases']['recovered']))
            self.activeLabel.setText(str(data['response'][-1]['cases']['active']))
            self.sampleLabel.setText(str(data['response'][-1]['tests']['total']))
        except:
            self.dateError.setText('No Covid for this date check for another date')
        

        
'''
        #self.poulationLabel.setText(data[i]['population'])
            
            
       
        # print(currentItem)
        #self.poulationLabel.setText(currentItem['population'])
        #print(data2['response'])
        

        
'''        

        
# class Upadate Password            
class UpdatePassword(QDialog):
    def __init__(self):
        super(UpdatePassword, self).__init__()
        loadUi("C:\\Python310\\CovidApp-Project\\UI\\passwordUpdate.ui", self)
        self.update.clicked.connect(self.successUpdate) # a click signal that successfully change user pasword
        self.updateBackToLogin.clicked.connect(self.gotoLoginFromUpdate) # a click signal that successfully take user to the login page form update password
        self.updateBackToSignup.clicked.connect(self.gotoSignupFromUpdate) # a click signal that successfully take user to the signup page form update password
        self.updatePasswordField.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password) # hashing the  password inputed by user
        self.updateConPasswordField.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password) # hashing the Confirm  password inputed by user
      
    # changing user password
    def successUpdate(self):
        updateEmail = self.updateEmailField.text().strip()
        updatePassword = self.updatePasswordField.text().strip()
        updateConPassword = self.updateConPasswordField.text().strip()
        
        if len(updateEmail) == 0 or len(updatePassword) == 0 or len(updateConPassword) == 0:
            self.updateErrorMessage.setText("Please input all fields")
        else:
            self.updateErrorMessage.setText("")
            self.updateErrorMessage.setText("")
            # selecting from the database to check if the emil is a valid email
            SelectQuery = ("SELECT Email, Password FROM CovidAuthentication WHERE (Email = ?)")
            cursor.execute(SelectQuery, updateEmail)
            row = cursor.fetchall()
            # if email is a valid one then we check the password
            if (row): 
                # confirming the password is valid before passing it inot the database
                if (updatePassword == updateConPassword): 
                    self.updateErrorMessage.setText("Password changed..")
                    # update the datase once the password is confirmed correct
                    UpdateQuery = ("UPDATE CovidAuthentication set Password = ? where Email = ?")
                    UpdateValues = (updatePassword, updateEmail)
                    cursor.execute(UpdateQuery, UpdateValues)
                    conn.commit() # saving datbase
                    print(cursor.rowcount, "records affected")  
                    self.updateEmailErrorMessage.setText("")
               
                else:
                    self.updateEmailErrorMessage.setText("")
                    self.updateErrorMessage.setText("Password not confirmed")
            else:
                self.updateEmailErrorMessage.setText("Invalid Email")
                
    # allow signup screen to be open from updatePassword     
    def gotoSignupFromUpdate(self):
        UpadateBackToSignup = SignupScreen() # creating and object of the signup screen
        widget.addWidget(UpadateBackToSignup) # adding the screen to stack
        widget.setCurrentIndex(widget.currentIndex()+1)# chaning the index once the screen is change to signup screen

    
    # allow login screen to be open from updatePassword
    def gotoLoginFromUpdate(self):
        UpdateBackToLogin = LoginScreen() # creating and object of the login screen 
        widget.addWidget(UpdateBackToLogin) # adding the screen to stack
        widget.setCurrentIndex(widget.currentIndex()+1) # chaning the index once the screen is change to login screen
        
     
        


        
        

app = QApplication(sys.argv) # crearting an instance of our applicatiob
window = welcomeScreen() # creating an object of the main screen
widget = QStackedWidget() #allow widget to stack in each other
widget.addWidget(window) # adding widget to stack this allow widget to stack on each other rather than opening differnt screen
widget.setFixedHeight(800) # setting fixed height
widget.setFixedWidth(1200) # setting fied width
widget.show()  # show the widget
try:
    sys.exit(app.exec())
except:
    print('Exiting')
    
