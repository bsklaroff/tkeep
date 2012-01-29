#!/usr/bin/env python
import argparse, time, datetime

def start_time(activity):
    f = open(activity, 'a+')
    if len(f.readlines()) % 2 == 0:
        f.write(str(time.time()) + '\n')
        print 'Started keeping time for ' + activity
    else:
        print 'Error: Time already running for ' + activity
    f.close()

def end_time(activity):
    f = open(activity, 'a+')
    if len(f.readlines()) % 2 == 1:
        f.write(str(time.time()))
        print 'Stopped the time for ' + activity
    else:
        print 'Error: Time not already running for ' + activity
    f.close()

def display_time(activity):
    pass

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
    print datetime.datetime.fromtimestamp(time.mktime(time.localtime(time.time())))

if __name__ == '__main__':
    main()
