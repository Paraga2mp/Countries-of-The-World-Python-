"""
Student Name: Ashraf Mamun  
Program Title: Country List Update
Description: This program loads countries information from a file and display
country name, display country flag, population, area, density, population percentage
in ui and also allow users to update population number and save to the txt file.
"""


import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import Ui_FinalProject_1
#      ^^^^^^^^^^^ Change this!

#CHANGE THE SECOND PARAMETER (Ui_ChangeMe) TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, Ui_FinalProject_1.Ui_MainWindow):
#                         ^^^^^^^^^^^   Change this!

    #Declare a global 2d list,a string variable, a boolean variable, file name and access mode
    countriesListInMemory = []
    countryName = ""
    unsave_changes = False
    fileName = "countries.txt"
    accessModeRead = "r"
    accessModeWrite = "w"

    # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
    # END DO NOT MODIFY

        # ADD SLOTS HERE, indented to this level (ie. inside def __init__)
       
        #slot for the Load menu Load Countries, when it is chosen from the menu
        self.actionLoad_Countries.triggered.connect(self.LoadMenu_Triggered)
        #slot to set total area units in ui
        self.actionLoad_Countries.triggered.connect(self.Select_TotalAreaUnit)
        #slot for selecting country name and to display name, flag, population, area
        # and percentage of world population 
        self.listDisplayCountries.currentRowChanged.connect(self.country_selected_from_list)
        # slot function to display population of per square mile
        self.radioButtonSquareMile.clicked.connect(self.Population_DensityMile)
        # slot function to display population of per square KM
        self.radioButtonSquareKM.clicked.connect(self.Population_DensityKM)
        # slot function to display total area in sq mile or sq KM
        self.comboBoxTotalArea.currentIndexChanged.connect(self.TotalArea_Unit)
        # slot function to update population to memory
        self.pushButtonUpdatePopulation.clicked.connect(self.update_population)
        # slot function to update population to file
        self.actionSave_To_File.triggered.connect(self.save_action_clicked)
        # slot function to exit the program
        self.actionExit.triggered.connect(self.exit_program)
        # Hide the frame details from user
        self.frameDisplay.hide()
       

    # ADD SLOT FUNCTIONS HERE
    # These are the functions your slots will point to
    # Indent to this level (ie. inside the class, at same level as def __init__)


    # Function is called when user load countries from File menu
    def LoadMenu_Triggered(self):
        #Open file and read it's data into memory in a 2d list
        self.LoadCountriesFromFile()
        #Load country data from memory into on-screen listwidget
        self.loadCountriesListBox()
        # Hide/Show the frame details from user unless user loads list of countries
        self.lineEditCountryName.setEnabled(False)
        self.lineEditPopulation.setEnabled(False)
        self.frameDisplay.show()
        self.labelDisplayDensity.hide()
        self.labelDisplayTotalArea.hide()
       
    def Select_TotalAreaUnit(self, selected_index):
        # A function is called to set values of Sq Mile/Sq KM of selected country
        self.select_AreaDensity(selected_index)

        
    # Function is called when users select a country from listwidget
    def country_selected_from_list(self, selected_index):
        # store the selected country name into a variable
        countryName = self.get_country_index(selected_index)
        # A function is called to display the flag
        self.display_Flag(countryName)
        # A function is called to show the selected country name
        self.display_CountryName(countryName, selected_index)
        # A function is called to display the population of selected country
        self.display_Population(selected_index)
         # A function is called to display the area in Miles of selected country
        self.display_TotalArea(selected_index)
         # A function is called to display the population of selected country
        self.display_PopulationDensity(selected_index)
         # A function is called to display the percentage of world population of selected country
        self.percentage_Population(selected_index)

    # Calls a function to display population density per sq mile
    def Population_DensityMile(self, selected_index):
        self.display_PopulationDensityMile(selected_index)
    # Calls a function to display population density per sq mile
    def Population_DensityKM(self, selected_index):
        self.display_PopulationDensityKM(selected_index)
     # Calls a function to display total area in miles or KM
    def TotalArea_Unit(self, selected_index):
        self.display_TotalAreaUnit(selected_index)
    # calls a function to update population number into memory
    def update_population(self, selected_index):
        self.save_changes_to_memory(selected_index)
    # calls a function to update population number into file
    def save_action_clicked(self):
        self.save_changes_to_file()
    # calls a function to exit the program
    def exit_program(self):
        self.exit_from_program()

        

    #Example Helper Function
    #    def Save(self):
    #       Implement the save functionality here
    
    # Loads data from file to memory
    def LoadCountriesFromFile(self):
        # opne the file with file name & access mode declared as global 
        myFile = open(self.fileName, self.accessModeRead)
       # declare a 2d list
        self.CountriesListInMemory = [] 
        fileData = True
        # load the file into a 2d list
        while fileData:
            fileData = myFile.readline()
            if(fileData):
                self.countriesListInMemory.append(fileData.split(","))
        # close the file after reading
        myFile.close()

    # Loads data from memory to list widget of ui
    def loadCountriesListBox(self):
        self.listDisplayCountries.clear()
        for row in self.countriesListInMemory:
            countryName = row[0]
            self.listDisplayCountries.addItem(countryName)
    # set the load country menu disable after loading the country to list widget        
        self.actionLoad_Countries.setEnabled(False)
    
    
    # function to return the selected country name
    def get_country_index(self, selected_index): 
        countryName = self.countriesListInMemory[selected_index][0] 
        # function returns country name to its caller
        return countryName
        
    # function to display flag of the selected country
    def display_Flag(self, countryName):
        countryFlag = countryName.replace(" ", "_")
        # set the name of the flag based on selected country
        flag = QPixmap("Flags\\" + countryFlag + ".png")
        self.labelFlag.setPixmap(flag)
 
    # function to display country name and set radio button and combo box with default values
    def display_CountryName(self, countryName, selected_index):
        self.lineEditCountryName.setText(self.countriesListInMemory[selected_index][0])
        # set the display country name not editable
        self.lineEditCountryName.setEnabled(False)
        self.radioButtonSquareMile.setChecked(True)
        self.labelDisplayTotalArea.show()
        self.comboBoxTotalArea.setCurrentText("Sq. Miles")

    # function to display population of the country in ui
    def display_Population(self, selected_index):
        numOfPopulation = int(self.countriesListInMemory[selected_index][1])
        self.lineEditPopulation.setText(f"{numOfPopulation:,.0f}")
        # make the population field editable
        self.lineEditPopulation.setEnabled(True)

    # function to display total area of selected country in ui
    def display_TotalArea(self, selected_index):
        totalArea = float(self.countriesListInMemory[selected_index][2])
        self.labelDisplayTotalArea.setText(f"{totalArea:,.1f}")

    # function to set values in combo box 
    def select_AreaDensity(self, selected_index):
        self.comboBoxTotalArea.addItem("Sq. Miles")
        self.comboBoxTotalArea.addItem("Sq. KM")

    # functon to display poulation density per sq mile by default
    def display_PopulationDensity(self, selected_index):
        self.labelDisplayDensity.show()
        # calculate population density, divide population by area
        pupulation = int(self.countriesListInMemory[selected_index][1])
        area = float(self.countriesListInMemory[selected_index][2])
        densityMile = float(pupulation/area)
        if(self.listDisplayCountries.currentRow()):
            self.labelDisplayDensity.setText(f"{densityMile:,.2f}")
        
    # functon to display poulation density per sq mile when radio button selects sq mile
    def display_PopulationDensityMile(self, selected_index):
        self.labelDisplayDensity.show()
        n_index = int(self.listDisplayCountries.currentRow())
        # calculate population density divide population by area
        pupulation = int(self.countriesListInMemory[n_index][1])
        area = float(self.countriesListInMemory[n_index][2])
        densityMile = float(pupulation/area)
        if(n_index>=0 and n_index <= len(self.countriesListInMemory)):
            self.labelDisplayDensity.show()
            self.labelDisplayDensity.setText(f"{densityMile:,.2f}")

    # functon to display poulation density per sq mile when radio button selects sq km
    def display_PopulationDensityKM(self, selected_index):
        # declare a variable to convert sq mile to sq. kilometer
        sqKilometer = 2.589
        n_index = int(self.listDisplayCountries.currentRow())
        pupulation = int(self.countriesListInMemory[n_index][1])
        area = float(self.countriesListInMemory[n_index][2])
        # calculate density divide population by sq. mile and multiply by sq mile to sq km
        # conversion value
        densityMile = float(pupulation/area)
        densityKM = (densityMile * sqKilometer)
        if(n_index>=0 and n_index <= len(self.countriesListInMemory)):
            self.labelDisplayDensity.show()
            self.labelDisplayDensity.setText("{:,.2f}".format(densityKM))
            
    # function to display sq miles and sq. km when comno box item changes
    def display_TotalAreaUnit(self, selected_index):
        # declare a varible to convert sq mile to sq km
        sqKilometer = 2.589
        p_index = int(self.listDisplayCountries.currentRow())
        totalArea = float(self.countriesListInMemory[p_index][2])
        # calculate total area in sq km
        totalAreaKM = (totalArea * sqKilometer)
        # check combo box text to display appropriate value
        index = self.comboBoxTotalArea.itemText(selected_index)
        if(index == "Sq. KM"):
            self.labelDisplayTotalArea.setText("{:,.1f}".format(totalAreaKM))
        elif(index == "Sq. Miles"):
            self.labelDisplayTotalArea.setText("{:,.1f}".format(totalArea))

    # function to display percentage to selected country's population compared to world 
    # population
    def percentage_Population(self, selected_index):
        totalPopulation = 0
        index = int(self.listDisplayCountries.currentRow())
        selectedPopulation = int(self.countriesListInMemory[index][1])
        # calculate total population by adding all the population numbers in the list
        for count in range(len(self.countriesListInMemory)):
            totalPopulation = totalPopulation + int(self.countriesListInMemory[count][1])
        # calculate the percentage of total population of selected country and display
        perOfTotalPopulation = ((selectedPopulation/totalPopulation) * 100)
        self.labelPercentageOfPopulation.setText(f"{perOfTotalPopulation:.4f}%")

    # function to save updated population into memory
    def save_changes_to_memory(self, selected_index):
        index = int(self.listDisplayCountries.currentRow())
        populationString = self.lineEditPopulation.text()  
        population = populationString.replace(",", "")
        # check user input validation
        if(population.isnumeric() and int(population) > 0):
            self.countriesListInMemory[index][1] = population
            # display an update message 
            QMessageBox.information(self,
                                'Updated',
                                'Data has been updated in memory, but has not been updated in the file yet',
                                QMessageBox.Ok)
            # calls the percentage_Population function to display updated percentage
            self.percentage_Population(selected_index)
            # calls the display_PopulationDensityMile function to display updated population per sq. mile
            self.display_PopulationDensityMile(selected_index)
            # Set the Save to File item enable in file menu after updating population into memory
            self.actionSave_To_File.setEnabled(True)

        else:
            # display a message if data is not valid
            QMessageBox.information(self,
                                'Invalid',
                                'Data is invalid so not updated in memory ',
                                QMessageBox.Ok)
        # set the boolean vatiable value as True if user's changes saved to memory
        self.unsave_changes = True
        
                                
    # function to save changes of population from memory to file
    def save_changes_to_file(self):
        with open(self.fileName, self.accessModeWrite) as countryFile:
            for country in self.countriesListInMemory:
                countryFile.write(",".join(country))
        # set the boolean variable value False after update to file
        self.unsave_changes = False

    # function to exit the program
    def exit_from_program(self):
        # check if updated population is already saved into or not
        if self.unsave_changes == True:
            msg = "Save changes to file before closing?"
            reply = QMessageBox.question(self, 'Save?',
                     msg, QMessageBox.Yes, QMessageBox.No)
            # check if user pres Yes or NO and based on that exit the program or save changes to file
            if reply == QMessageBox.Yes:
                self.save_changes_to_file()
            elif reply == QMessageBox.No:
                QApplication.closeAllWindows()
        # quit the program
        else:
            QApplication.closeAllWindows()



# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY