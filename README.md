# dirtynamepython
process names stored in dirtyname file
there are names stored in csv file.


this python program will read files, manipulating the data, and storing the clean files back to a different file. During this process you must check for and catch errors.
You will be provided with a comma delimited file called DirtyNames.csv this file consists of thousands of names that are horribly formatted and must be cleaned up. A clean name is all lower case letters except the first letter which must be capitalized. In addition, some of the names have symbols or other invalid characters, if a name contains an invalid character it should be put in a separate file called InvalidNames.csv. Clean names should be put in CleanNames.csv.
A dirty name will consist of a name with randomly placed upper and lowercase letters. For example:
-	joRdaN
A clean name should be formatted with and uppercase first letter followed by lowercase letters. However, if a name is hyphenated the name after the hyphen should also start with an upper case letter. For example:
-	Jordan
-	Pitt-Rivers
Invalid names are entries in the list that are not names at all or names that contain invalid symbols. For the purpose of this task a name should be considered valid if it only contains letters a-z, A-Z, or a hyphen. Any other symbols (including spaces and numbers) should put the name in the invalid name list. Examples of invalid names:
-	123-123-1234
-	J@ke
-	John Doe
Task	Points
Open DirtyNames.csv file	/1
Create InvalidNames.csv file	/1
Create CleanNames.csv File	/1
Fix formatting of all valid names and save to CleanNames.csv	/1
Populate InvalidNames.csv with invalid names	/1
Names in InvalidNames.csv are not mutated in any way from the original entry	/1
Use exceptions properly	/1
Program also works with instructors’ word list	/1
Use modules to compartmentalize code.	/1
Functions make sense in modules (eg. Math module should only have math functions)	/1
Use correct accessors for opening and reading files	/1
Works with 10,000 name list	/1
Works with 100,000 name list	/1
Works with 10,000,000	/1

Submission
Submit a zip file named Firstname-Lastname_Assignment-3.zip containing your project
