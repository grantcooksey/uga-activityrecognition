import pandas as pd


class Parser(object):
    @staticmethod
    def parse_file(file_name):
        data = pd.read_csv(file_name, names=["tick", "timestamp",
                                             "activity", "x", "y",
                                             "z", "user"])
        split_frames = data['activity'].unique().tolist()
        activity_df = data.loc[data.activity == split_frames[0]]
        print activity_df
