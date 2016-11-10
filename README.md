# UGA - Activity Recognition

We will share all the necessary code for the project here.

## Activity Parser

This section contains information on all the parsing utilities for the
project.
 
### Requirements
 
 You need the [pandas](http://pandas.pydata.org) library 
 installed on your machine.
 
 Instructions for installation can be found at 
 
 http://pandas.pydata.org/pandas-docs/stable/install.html

 This project uses python 3.x
 
### Parsing

Parser to separate accelerometer data into separate files by activity.
The parser takes a single command line argument, a path to the file to 
 parse.  The parser then creates a new directory named after the user
 id and creates and saves a csv file for each activity in the file.  If
 a directory already named after the user exists, the program throws an
 error.  Runs under the assumption that each activity is performed only
 once per user.
 
 Run the parser using the `single_file_driver.py` script.  The script
 takes a single command line argument, a path to the file to parse. 
 The path can either be relative to the current working directory 
 or absolute.
 
 The format is `python single_file_driver.py <path_to_file>`
 
### Activity Searching

This was created due to a need to have an easy way to find all users 
in the data set that performed a particular activity.  Run the search
using the `find_activities_driver.py` script.  The script takes in 
command line arguments to determine where to look for files and a 
list of activities to search for.  Results of this search are printed 
to stdout.

Results are of the form
`<activity_number> [<list_of_users]`

The format to run the script is 
`python find_activities_driver.py <path_to_dir> <list_of_activities>`, 
where path to dir can be either relative or absolute and the list of
activities is a whitespace separated list of activity numbers.

#### Example

Assuming data set is in a file named `data` in the parent directory and
the activities to search for are 13 and 17, the command would be 
`python find_activities_driver.py data/ 13 17`.
 
### Future Work
 
 Create a new driver to parse multiple user activity data files at once.
 
 Search functionality for matching users between activities

***

## Period Lengths

 The shaplet-length directory contains jupyter notebooks that experiment
 with different techniques for searching for the length of periods.
 `period-search.ipynb` is more of an experimental environment while
 `comparing_periods.ipynb` demonstrates some of the more successful
 methods of searching for a shaplet length.


## Shaplet Generation

 The shaplet euclidean distance generator script is called 'shaplet_generator.py'
 and requires 'shaplet_util.py' in the same file.  Numpy, pandas, and
 [peakutils](http://pythonhosted.org/PeakUtils/) need to be installed. I have set
 it to run on user 144's walking data but you can change that if you want.  Just verify that
 that it gets the correct length and you are getting the correct side.  My
 'play_shaplet_gen' notebook should make this easy to check.  The path for the
 data file is set for the same directory but this can be changed in the first
 line in the main method.