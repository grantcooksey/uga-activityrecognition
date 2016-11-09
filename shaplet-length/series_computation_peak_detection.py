
# coding: utf-8

# In[1]:

import sys
import math as mt
from numpy import NaN, Inf, arange, isscalar, asarray, array
from matplotlib.pyplot import plot, scatter, show
import pandas as pd

def peakdet(v, delta, x = None):
    """
    Converted from MATLAB script at http://billauer.co.il/peakdet.html
    
    Returns two arrays
    
    function [maxtab, mintab]=peakdet(v, delta, x)
    %PEAKDET Detect peaks in a vector
    %        [MAXTAB, MINTAB] = PEAKDET(V, DELTA) finds the local
    %        maxima and minima ("peaks") in the vector V.
    %        MAXTAB and MINTAB consists of two columns. Column 1
    %        contains indices in V, and column 2 the found values.
    %      
    %        With [MAXTAB, MINTAB] = PEAKDET(V, DELTA, X) the indices
    %        in MAXTAB and MINTAB are replaced with the corresponding
    %        X-values.
    %
    %        A point is considered a maximum peak if it has the maximal
    %        value, and was preceded (to the left) by a value lower by
    %        DELTA.
    
    % Eli Billauer, 3.4.05 (Explicitly not copyrighted).
    % This function is released to the public domain; Any use is allowed.
    
    """
    maxtab = []
    mintab = []
       
    if x is None:
        x = arange(len(v))
    
    v = asarray(v)
    
    if len(v) != len(x):
        sys.exit('Input vectors v and x must have same length')
    
    if not isscalar(delta):
        sys.exit('Input argument delta must be a scalar')
    
    if delta <= 0:
        sys.exit('Input argument delta must be positive')
    
    mn, mx = Inf, -Inf
    mnpos, mxpos = NaN, NaN
    
    lookformax = True
    
    for i in arange(len(v)):
        this = v[i]
        if this > mx:
            mx = this
            mxpos = x[i]
        if this < mn:
            mn = this
            mnpos = x[i]
        
        if lookformax:
            if this < mx-delta:
                maxtab.append(mxpos)
                mn = this
                mnpos = x[i]
                lookformax = False
        else:
            if this > mn+delta:
                mintab.append(mnpos)
                mx = this
                mxpos = x[i]
                lookformax = True

    return maxtab
    


# In[ ]:

def is_below(x, thres):
    if x > thres:
        return x
    return thres
    
def series_computation(series, percent_series):
    """
        series contains list of all values
        percent_series is how much top perecent you want the data like 0.2, 0.05
        return
            series with all values
            the min value of series
    """
    
    # smoothing the time series and making new series out of it.
    window = 5.0
    half_window = int(mt.floor(window / 2))
    new_series = []

    for i in range(half_window, len(series) - half_window):
        temp = 0
        for j in range(half_window):
            temp += series[i - j]
        temp += series[i]
        for k in range(half_window):
            temp += series[i + k]
        temp = temp / window
        new_series.append(temp)
    
    s_series = pd.Series(new_series)
    
    s_series.sort_values(ascending=False, inplace=True)

    twenty_percent = int(len(s_series) * percent_series)

    new_s_series = s_series[0:twenty_percent]
    
    s_series = s_series.apply(is_below, args=(new_s_series.min(),))
    
    s_series = s_series.sort_index()
    
    return s_series, new_s_series.min()

