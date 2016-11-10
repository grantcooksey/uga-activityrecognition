import numpy as np
import pandas as pd
import peakutils


def estimate_period(df, threshold, axis='x'):
    indexes = peakutils.indexes(df[axis].values, thres=threshold, min_dist=10)
    indexes = pd.Series(indexes)
    if indexes.index.size != 0:
        diff = indexes.drop(0) - indexes.shift(1).drop(0)
        return diff.median()
    return float('nan')


# ## Single Peak Detection
# Our parameters are the time series to search, the window size, and the threshold to examine.  To improve accuracy, we are using a sliding window to improve the accuracy the peak detection algorithm.  Rather than find peaks over the entire data set, we use a fixed window length and calculate the average peak distance as the window slides over the time series from beginning to end.  The function gives control over how far to slide the window at each calucation and how big the window should be.  The function returns a list of lists of average peaks from the upper half and lower half of the time series. 
# 
# Parameters 
# * timeseries(pandas dataframe) - dataframe of activity data. index starts at 0 and increases by 1.
# * threshold(float between [0.,1.]) - Normalized threshold. Only the peaks with amplitude higher than the threshold will be detected.
# * window_size(int) - size of the sliding window, less than the length of the time series.  If greater, window_size will be set to the length of the time series.
# * axis(str) - either 'x', 'y', or 'z', corresponding to the axis to check
# * step(int) - how far to slide the window for each calculation of peak distance.  If step is greater than window_size, the window size will be used as the step value.
# 
# Returns
# * dic : 'upper' is upper peak averages, 'lower' is lower peak averages

def find_single_peak_dist(timeseries, threshold=0.8, window_size=500, axis='x', step=100):
    if window_size > timeseries.last_valid_index():
        window_size = timeseries.last_valid_index()
    if axis not in ('x', 'y', 'z'):
        raise ValueError('invalid axis value, use x, y, or z')
    if step > window_size:
        step = window_size
    upper = []
    lower = []
    ts_flipped = timeseries * -1
    for i in np.arange(0, timeseries.index.size - window_size, step):
        upper.append(estimate_period(timeseries.iloc[i:i+window_size], threshold, axis=axis))
        lower.append(estimate_period(ts_flipped.iloc[i:i+window_size], threshold, axis=axis))
    return {'upper': pd.Series(upper), 'lower': pd.Series(lower), 'threshold': threshold, 'window': window_size}
