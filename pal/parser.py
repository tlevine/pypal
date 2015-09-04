import datetime

def file(fp):
    for line in fp:
        yield from entry(line)

def entry(line):
    'Read a pal calendar entry'
    datespec, _, description = line.partition(' ')
    for date in dates(datespec):
        yield date, description

def read_date(datestring):
    try:
        date = datetime.datetime.strptime(datestring, '%Y%m%d')
    except ValueError:
        return None
    else:
        return date.date()

def dates(datespec, today = datetime.date.today()):
    single_date = read_date(datespec)
    if single_date != None:
        yield single_date
    elif datespec.count(':') == 2:
        subset, _start, _end = datespec.split(':')
        if subset == 'DAILY':
            current = read_date(_start)
            end = read_date(_end)
            while current <= end:
                yield current
                current += datetime.timedelta(days = 1)
    elif datespec == 'TODO':
        yield today
    else:
        logger.warn('Unsupported date specification: "%s"' % datespec)
