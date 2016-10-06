import sys
import glob
from collections import defaultdict
from parser import Parser


def main():
    if len(sys.argv) < 3:
        print('Usage: find_activities_driver.py <path_to_dir> <list_of_activities>')
        sys.exit(1)

    if sys.argv[1].endswith("/"):
        extension = '*.csv'
    else:
        extension = '/*.csv'

    user_dict = defaultdict(list)

    for filename in glob.iglob(sys.argv[1] + extension):
        activities_for_user = Parser.get_list_of_activities(filename)
        for activity in sys.argv[2:]:
            if int(activity) in activities_for_user:
                user_dict[activity].append(filename[len(sys.argv[1]):-4])
    for x in user_dict:
        print(Parser.lookup_activity(int(x)), user_dict[x])

if __name__ == '__main__':
    main()
