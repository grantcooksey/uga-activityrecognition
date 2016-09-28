from __future__ import print_function
from activity_list import activity_list
from people_list import people_list
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

def main():
    if not len(sys.argv) == 6:
        print('Usage: graph_creator.py <path_to_file> <directory_path_data_files> <activity_number> <number_of_input_files> <axis - x, y or z>')
        sys.exit(1)
    # master file contains the file names on each line
    master_file = sys.argv[1]
    
    # directory contains the path where the data is stored
    directory = sys.argv[2]
    
    # activity number
    activity_number = int(sys.argv[3])
    
    # number of input files in master file
    number_of_input_files = int(sys.argv[4])
    
    # which axis the plot should be
    axis = sys.argv[5].lower()

    # open master file
    # then open directory and do stuff for each file name provided in the master file
    count = 1
    with open(master_file) as master:
        fig = plt.figure(figsize=(10,30))
        fig.subplots_adjust(hspace=1)
        fig.suptitle("Activity " + activity_list[str(activity_number)], fontsize= 14)
    
        for master_line in master:
            with open(directory + master_line.strip() + '.csv', 'rU') as f:
                file_data_frame = pd.DataFrame(np.genfromtxt(f, usecols=(0,2,3,4,5), delimiter = ',', names=['tick', 'activity', 'x','y','z']))

                # see if the user has completed that activity and make new data frame
                file_data_frame_activity = file_data_frame[file_data_frame.activity == activity_number][1500:3500]
                # make this extra column to index value from 0 to n instead of what given in data
                file_data_frame_activity['index'] = range(1, len(file_data_frame_activity) + 1)

                tick = file_data_frame_activity['index']
                x_y_z = file_data_frame_activity[axis]
                
                fig.text(0.5, 0.04, 'Ticks', ha='center')
                fig.text(0.04, 0.5, axis.upper() + '-Axis', va='center', rotation='vertical')
                ax = fig.add_subplot( 100 * number_of_input_files + 10 + count)
                ax.plot(tick, x_y_z, 'r')
                plt.title('Person ' + str(master_line.strip()) + " - " + people_list[master_line.strip()])
                count += 1

        plt.show()
        # plt.savefig('output.png')
        # plt.clf()
                
if __name__ == "__main__":
	main()