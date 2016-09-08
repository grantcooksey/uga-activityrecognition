from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

def main():
    if not len(sys.argv) == 4:
        print('Usage: graph_creator.py <path_to_file> <directory_path_data_files> <number_of_input_files>')
        sys.exit(1)
    # master file contains the file names on each line
    master_file = sys.argv[1]
    # directory contains the path where the data is stored
    directory = sys.argv[2]
    #number of input files in master file
    number_of_input_files = int(sys.argv[3])
    # open master file
    # then open directory and do stuff for each file name provided in the master file
    count = 1
    with open(master_file) as master:
        fig1 = plt.figure(figsize=(10,30))
        fig1.subplots_adjust(hspace=1)
        
        for master_line in master:
            with open(directory + master_line.strip() + '.csv', 'rU') as f:
                file_data = np.genfromtxt(f, usecols=(0,2,3,4), delimiter = ',', names=['tick', 'activity', 'x', 'y'])

                file_data_frame = pd.DataFrame(file_data)
                file_data_frame_17_2000 = file_data_frame[file_data_frame.activity == 17][500:2500]
                file_data_frame_17_2000['index'] = range(1, len(file_data_frame_17_2000) + 1)
                file_data_frame_20_2000 = file_data_frame[file_data_frame.activity == 20][500:2500]
                file_data_frame_20_2000['index'] = range(1, len(file_data_frame_20_2000) + 1)

                tick_17 = file_data_frame_17_2000['index']
                activity_17 = file_data_frame_17_2000['activity']
                X1_17 = file_data_frame_17_2000['x']
                Y1_17 = file_data_frame_17_2000['y']
                
                fig1.text(0.5, 0.04, 'Ticks', ha='center')
                fig1.text(0.04, 0.5, 'X-Axis', va='center', rotation='vertical')
                ax = fig1.add_subplot( 100 * number_of_input_files + 10 + count)
                ax.plot(tick_17, X1_17, 'r')
                plt.title('Person ' + str(master_line.strip()))
                count += 1

        plt.show()
        # plt.savefig('output.png')
        # plt.clf()
                

if __name__ == "__main__":
	main()