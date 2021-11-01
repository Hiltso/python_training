#import matplotlib.pyplot as plt

import argparse
import sys # read arguments off the command line
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
                # print debugging .
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


def sortby(rows, col_name):
    def get_col_name(row):
        return row[col_name]
    return sorted(rows, key=get_col_name)

def get_value(rows, col_name):
    res = []
    for row in rows:
        res.append(row[col_name])
    return res

# mathpotlib examples https://matplotlib.org/stable/gallery/index.html
# cd to project folder env/scripts >>>activate. Then >>>pip install matpltlib

# make a command line app
def plot_state(state, csvname, plotname):
    res = read_csv(csvname)
    state_res = filter(res, state)
    state_res = sortby(state_res, 'date')
    fig. ax = plt.subplots()
    ax.plot(get_value(state_res, 'positive'))
    ax.plot(get_value(stare_res, 'deaths'))
    ax.plot(get_value(state_res, 'hospitalized'))
    fig.savefig(plotname)


def main(args):
    ap = argparse.ArgumentParser()
    ap.add_argument('-s', '--state')
    ap.add_argument('-c', '--csv')
    ap.add_argument('-o', '--output',
                    help='PNG filename')    
    opt = ap.parse_args(args)
    if opt.state:
        plot_state(opt.state, opt.csv, opt.output)

# to run from command line.
# python covid.py -h
# python covid.py -s WY -c covid.csv -o wy.png

if __name__ == '__main__':
    main(sys.argv[1:])
    
else:
    # loading this file
    print('loading')
    

# plot_state('NY', 'covid.csv', 'ny.png')



    
    
            
        
    
