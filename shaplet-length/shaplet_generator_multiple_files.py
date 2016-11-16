import shaplet_util as util
import pandas as pd
import numpy as np
import os
import sys

def dist(row, walking, shaplet_len):
    return row.apply(row_dist, args=(row.name, walking, shaplet_len,))


def row_dist(column, row, walking, shaplet_len):
    test_shaplet = walking.loc[int(row):int(row)+shaplet_len].reset_index()
    ts_slice = walking.loc[int(column):int(column)+shaplet_len].reset_index()
    return np.linalg.norm(test_shaplet['x']-ts_slice['x'])


def set_column(x):
    return x.fillna(x.name)


def get_best(row):
    num_best = int(row.size * .1)
    sorted_row = row.sort_values().reset_index()
    return sorted_row.loc[0:num_best, row.name]


def main():
    if len(sys.argv) < 2:
        print("Usage: python shapelet_generator_multiple_files.py <activity_numbers>")
        print("Pleas give activity numbers like 13 23 17 ")
        sys.exit()
    
    # Set the directory you want to start from or where all the data is stored
    rootDir = '../../Working_Data'

    activity_list = sys.argv[1:]
    # recursively find all matching files and generate shapelets
    for dirName, subdirList, fileList in os.walk(rootDir):
        # print('Found directory: {}'.format(dirName))
        for fname in fileList:
            # only process files matching with those in activity list provided by user
            if fname.split('_')[0] in activity_list:
                # print('\t{}'.format(fname))
                person_number = dirName.split('/')[-1]
                # absolute path of file to read
                fname_path = os.path.join(rootDir, dirName, fname)
                sample = pd.read_csv(fname_path, names=["tick", "timestamp", "activity",
                                                             "x", "y", "z", "user"], index_col=False)
                # Extract walking data, aka remove the noise at the beginning and end
                walking = sample.iloc[3000:19000]
                walking = walking.reset_index()

                # find the shaplet length, manually checked to see which side is valid
                # TODO: automate valid side detection
                period = util.find_single_peak_dist(walking, window_size=5000, step=100)
                shaplet_len = period['upper'].median()

                # For testing purposes only
                walking = walking.iloc[0:200]

                df = pd.DataFrame(data=[], index=np.arange(0, walking['x'].index.size - shaplet_len, 20),
                                  columns=walking.index)
                df.index = df.index.map(int)
                df = df.apply(set_column, axis=0)

                # Main calculation
                euclidean_dist_df = df.apply(dist, axis=1, args=(walking, shaplet_len,))
                euclidean_dist_df = euclidean_dist_df.apply(get_best, axis=1)

                # Store data
                euclidean_dist_df.to_csv(person_number + "_" + fname.split('_')[0] + "_candidate_shaplets.csv")

if __name__ == "__main__":
    main()