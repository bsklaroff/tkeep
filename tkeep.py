#!/usr/bin/env python
import argparse, time, datetime

def start_time(activity):
    f = open(activity, 'a+')
    if len(f.readlines()) % 2 == 0:
        f.write(str(time.time()) + '\n')
        print 'Started keeping time for ' + activity
    else:
        print ('You cannot start the time for ' + activity
               + ' because the time is already running!')
    f.close()

def end_time(activity):
    f = open(activity, 'a+')
    if len(f.readlines()) % 2 == 1:
        f.write(str(time.time()) + '\n')
        print 'Ended the time for ' + activity
    else:
        print ('You cannot end the time for ' + activity
               + ' because the time is not currently running!')
    f.close()

def time_to_str(total_seconds):
    timedelta_str = str(datetime.timedelta(seconds=total_seconds))
    days_str = ''
    time_str = timedelta_str
    split_str = timedelta_str.split(',')
    if len(split_str) == 2:
        days_str = split_str[0] + ', '
        time_str = split_str[1].strip()
    split_time = time_str.split(':')
    hours = int(split_time[0])
    hours_str = str(hours) + ' hours, '
    if hours == 1:
        hours_str = str(hours) + ' hour, '
    minutes = int(split_time[1])
    minutes_str = str(minutes) + ' minutes, '
    if minutes == 1:
        minutes_str = str(minutes) + ' minute, '
    seconds = float(split_time[2])
    seconds_str = str(seconds) + ' seconds'
    final_str = days_str + hours_str + minutes_str + seconds_str
    return final_str

def display_time(activity):
    try:
        f = open(activity, 'r')
    except:
        print 'No data exists for ' + activity
        return
    total = 0
    while True:
        try:
            start = float(f.readline())
        except:
            break
        try:
            end = float(f.readline())
        except:
            end = time.time()
            print 'The time for ' + activity + ' is currently running'
        total += end - start
    time_str = time_to_str(total)
    print 'You have spent ' + time_str + ' total on ' + activity

def main():
    p = argparse.ArgumentParser(description='Keep track of time.')
    p.add_argument('activities', metavar='N', type=str, nargs='+',
                   help='an activity to keep time for')
    group = p.add_mutually_exclusive_group()
    group.add_argument('-s', '--start', action='store_true',
                       help='start timing the specified activities')
    group.add_argument('-e', '--end', action='store_true',
                       help='stop timing the specified activities')
    args = p.parse_args()
    for activity in args.activities:
        if args.start:
            start_time(activity)
        elif args.end:
            end_time(activity)
        else:
            display_time(activity)

if __name__ == '__main__':
    main()
