import argparse
import datetime

from date_range import date_range

from .parser import file

p = argparse.ArgumentParser(prog = 'pypal')
p.add_argument('-r', help = 'Date range', default = '0')

def main():
    args = p.parse_args()
    try:
        forward = int(args.r)
    except ValueError:
        forward, back = map(int, args.r.split('-'))
    else:
        back = 0

    t = datetime.date.today()
    dates = date_range(t - datetime.timedelta(back), t + datetime.timedelta(forward + 1))
