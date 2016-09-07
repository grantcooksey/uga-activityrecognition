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
            print 'Error: A directory with the name ' + new_path + \
                  ' already exists.'
            sys.exit(1)
        
        data = pd.read_csv(file_name, names=["tick", "timestamp",
                                             "activity", "x", "y",
                                             "z", "user"], index_col=False)
        split_frames = data['activity'].unique().tolist()  # Splits files by activity
        for activity in split_frames:
            activity_df = data.loc[data.activity == activity]
            activity_df.to_csv(Parser.lookup_activity(activity) + '.csv',
                               header=False, index=False)

    @staticmethod
    def lookup_activity(activity_num):
        if activity_num == 2:
            return '2_male_walk_hard'
        elif activity_num == 3:
            return '3_female_walk_hard'
        elif activity_num == 4:
            return '4_male_run_hard'
        elif activity_num == 5:
            return '5_female_run_hard'
        elif activity_num == 6:
            return '6_run_flat'
        elif activity_num == 7:
            return '7_no_disability_hard'
        elif activity_num == 8:
            return '8_SPPB_hard'
        elif activity_num == 9:
            return '9_cane'
        elif activity_num == 10:
            return '10_walker'
        elif activity_num == 11:
            return '11_treadmill_1mph_0%'
        elif activity_num == 12:
            return '12_treadmill_2mph_0%'
        elif activity_num == 13:
            return '13_treadmill_3mph_0%'
        elif activity_num == 14:
            return '14_treadmill_3mph_5%'
        elif activity_num == 15:
            return '15_treadmill_4mph_0%'
        elif activity_num == 16:
            return '16_treadmill_5mph_0%'
        elif activity_num == 17:
            return '17_treadmill_6mph_0%'
        elif activity_num == 18:
            return '18_treadmill_6mph_5%'
        elif activity_num == 19:
            return '19_seated_folding_laundry'
        elif activity_num == 20:
            return '20_standing_while_talking'
        elif activity_num == 21:
            return '21_brushing_teeth_hair'
        elif activity_num == 22:
            return '22_driving'
        elif activity_num == 23:
            return '23_walking'
        elif activity_num == 24:
            return '24_walking_pocket'
        elif activity_num == 25:
            return '25_walking_carrying_8lb'
        elif activity_num == 26:
            return '26_walking_holding_cell'
        elif activity_num == 27:
            return '27_walking_holding_coffee'
        elif activity_num == 28:
            return '28_carpet_heels'
        elif activity_num == 29:
            return '29_grass_barefoot'
        elif activity_num == 30:
            return '30_uneven_dirt'
        elif activity_num == 31:
            return '31_uphill_heels'
        elif activity_num == 32:
            return '32_downhill_heels'
        elif activity_num == 33:
            return '33_walking_up_stairs'
        elif activity_num == 34:
            return '34_walking_down_stairs'
        elif activity_num == 35:
            return '35_alignment_activity_post'

        return str(activity_num)


