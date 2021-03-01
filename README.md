# Countries of the World

I used PyQT and Visual Studio Code to create a graphical application (.pyw and supporting .py files) in which
Users can select countries name to see some basic information and country’s flag. Users also can update
country’s information.

When the application starts, nothing is visible to the user except the File menu. Selecting the Load Countries
option from the menu will load all country data from the countries text file into a two-dimensional list. To
start, the user will be shown only a list of the country names. Once the user selects any country from the list,
a display area will appear that will show information specific to the selected country.

In addition to displaying the country’s flag and basic demographics, the application should include a
dropdown list to allow users to change the Total Area display from its default setting of square miles to
square kilometers. When this occurs, the country’s Area data should be updated to show the user’s
preference of unit.

For the population density section, the density value should display in sq. miles by default. If the user selects
either of the Per Square Mile/KM choices, the Population Density data should be updated to show the user’s
preference of unit.

Users should be allowed to update the population of the currently selected country by entering a new
population value and clicking the Update Population button. If the new data is invalid, an “invalid data”
message will be displayed, and the value in the population box will revert to its original value (from before
the attempted changes). If the data is valid, this updates the country’s data in the two-dimensional list and
display a “Successfully saved to memory” message but will NOT save the data changes back into the original
countries.txt file at that time.

Any population data changes made by the user should only be saved to file when the user either clicks “Save
To File” in the menu, or if the program is closed without having already saved the changes. In this case, the
program should offer the user the option to save or exit without saving and do as the user chooses.
