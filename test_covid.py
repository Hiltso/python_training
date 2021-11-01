import unittest
import covid

class TestCovid(unittest.TestCase):
    def test_read_csv(self):
        res = covid.read_csv('covid.csv')
        self.assertEqual(len(res), 20780)

    def test_get_value(self):
        data =[{'name': 'matt'},
                {'name': 'suzy'}]
        res = covid.get_value(data, 'name')
        self.assertEqual(res, ['matt', 'suzy'])

if __name__ == '__main__':
    # executing
    unittest.main()
else:
    # loading this file
    print('loading')
    
# in command line run coverage
# >pip install coverage >coverage -h >coverage run test_covid.py >coverage html

                       
