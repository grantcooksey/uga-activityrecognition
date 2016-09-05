import pandas as pd
import os
import sys


class Parser(object):
    @staticmethod
    def parse_file(file_name):
        new_path = os.path.join('.', file_name[:-4])
        if not os.path.exists(new_path):
            os.makedirs(new_path)
            os.chdir(new_path)
        else:
            print 'Error: A directory with the name ' + new_path + ' already exists.'
            sys.exit(1)
        
        data = pd.read_csv(file_name, names=["tick", "timestamp",
                                             "activity", "x", "y",
                                             "z", "user"])
        split_frames = data['activity'].unique().tolist()
        for activity in split_frames:
            activity_df = data.loc[data.activity == activity]
            activity_df.to_csv(str(activity) + '.csv', header=False, index=False)
