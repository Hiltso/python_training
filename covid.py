import urllib.request as req

# url = 'https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_daily_4pm_et.csv'
# fname = 'covid.csv'

def fetch_url(url, fname):
    """
    Save a url to a local file
    """
    fin = req.urlopen(url)
    data = fin.read()
    with open(fname, mode='wb')as fout:
        fout.write(data)
    # upon unindent file is closed


def read_csv(fname):
    '''
    read a csv file and create a dictionary if rows and headers values
    '''
    # start built in debugger
    # import pdb; pdb.set_trace()
    with open(fname, encoding='utf8') as fin:
        rows = []
        for i, line in enumerate(fin):
            # check if at first line
            values = line.strip().split(',')
            if i == 0:
                # print debugging
                # print (values, rows)
                headers = values
            else:
                for j, val in enumerate(values):
                    # loop over values to convert to integers - stick it back into list with j/enumterate(pulls out position in that list)
                    # To avoid ValueError: invalid literal for int() with base 10: 'AK'
                    try:
                        val = int(val)
                    except ValueError:
                        pass
                    else:
                        values[j] = val
                rows.append(dict(zip(headers, values)))
    return rows

def filter(rows, state):
    # filter rows which are a list of dictionaries and pull out the value from the state key
    res = []
    for row in rows:
        if row['state'] == state:
            res.append(row)
    return res
