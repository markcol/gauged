'''
Gauged
https://github.com/chriso/gauged (GPL Licensed)
Copyright 2014 (c) Chris O'Hara <cohara87@gmail.com>
'''

class Aggregate(object):

    SUM = 'sum'
    MIN = 'min'
    MAX = 'max'
    MEAN = 'mean'
    STDDEV = 'stddev'
    PERCENTILE = 'percentile'
    MEDIAN = 'median'
    COUNT = 'count'

    ALL = set(( SUM, MIN, MAX, MEAN, STDDEV, PERCENTILE, MEDIAN, COUNT ))
