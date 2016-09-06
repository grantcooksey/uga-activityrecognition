# UGA - Activity Recognition

We will share all the necessary code for the project here.

## Activity Parser

Parser to separate accelerometer data into separate files by activity.
The parser takes a single command line argument, a path to the file to 
 parse.  The parser then creates a new directory named after the user
 id and creates and saves a csv file for each activity in the file.  If
 a directory already named after the user exists, the program throws an
 error.
 
 ### Requirements
 
 You need the [pandas](http://pandas.pydata.org) library 
 installed on your machine.
 
 Instructions for installation can be found at 
 
 http://pandas.pydata.org/pandas-docs/stable/install.html
 
 ### Parsing
 
 Run the parser using the `single_file_driver.py` script.  The script
 takes a single command line argument, a path to the file to parse. 
 The path can either be relative to the current working directory 
 or absolute.
 
 The format is `python single_file_driver.py <path_to_file>`
 
 ### Future Work
 
 Create a new driver to parse multiple user activity data files at once.