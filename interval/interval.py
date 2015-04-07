#!/usr/bin/env python

class Time(object):
    def __init__(self, hour, minute):
        '''Simple time wrapper.

        :param hour: Integer, from 0 to 24.
        :param minute: Integer, from 0 to 59.
        '''

        self.hour = hour
        self.minute = minute

class Interval(object):
    def __init__(self, start, end):
        '''Interval represents a task on schedule. 

        :param start: Time, when the task starts.
        :param end: Time, when the task ends.

        TODO: add support for passing timestap strings.For example,
              Interval('00:00', '02:39').
        TODO: make Interval objects more readable in a python shell.e.g.,

              >>> Interval(Time(0,0), Time(2,30))
              Interval(00:00 -> 02:30)
        '''
        start = self.modifyType(start)
        if not start:
            return
        end = self.modifyType(end)
        if not end:
            return
          
        self.start = start
        self.end = end
        
    def __str__(self):
        try:
            return "Interval(%02d:%02d -> %02d:%02d)" %(self.start.hour, self.start.minute, self.end.hour, self.end.minute)
        except:
            return "param err."
    
    def __repr__(self):
        try:
            return "Interval(%02d:%02d -> %02d:%02d)" %(self.start.hour, self.start.minute, self.end.hour, self.end.minute)
        except:
            return "param err."
        
    def modifyType(self,param):
        if isinstance(param, str):  # change string to Time
            TimeElems = param.split(":")
            try:
                param = Time(int(TimeElems[0]),int(TimeElems[1]))
                return param
            except:
                return None
        elif isinstance(param, Time):
            return param
        else:
            return None


def most_intervals_overlap_count(intervals):
    '''count the maximum overlappes in a schedule.

    tasks on the schedule may overlaps.For example, task A was scheduled
    from 06:00 to 08:00, and task B was scheduled from 07:30 to 09:00, then
    A and B overlap in 07:30-08:00.

    mutiple tasks may overlap on the same time interval, you job is to find
    out the number of tasks when maximum overlap happens.

    :param intervals: list of Interval

    >>> most_intervals_overlap_count([Interval(Time(6,0), Time(8,0))])
    1
    >>> most_intervals_overlap_count([Interval(Time(6,0), Time(8,0)), Interval(Time(7, 30), Time(9,0))])
    2
    >>> most_intervals_overlap_count([Interval(Time(6,0), Time(8,0)), Interval(Time(8, 0), Time(9,0))])
    1
    '''
    # TODO: implement this function
    sorted(intervals, key=attrgetter("hour","minute"))
    
    pass
