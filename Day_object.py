from pickletools import int4
from typing import Dict, List
from bs4 import BeautifulSoup
# from bs4 import SoupStrainer 


class Day():
    def __init__(self, group: int, table: BeautifulSoup.Tag):
        self.group = group
        self.day_date = self.day_date_parse(table)
        self.subject = self.subject_parse(table)
        

    def day_date_parse(self, table: BeautifulSoup.Tag) -> Dict:
        contain = {'day':'', 'date':''}
        for iteration in range(0, len(table.find_all('tr'))-1):
            if len(table.find_all('tr')[iteration].find_all('td')):
                terminator_1 = table.find_all('tr')[0].find_all('td')[0].text.find('-')
                terminator_2 = table.find_all('tr')[0].find_all('td')[0].text.find(',')
                contain['day'] = table.find_all('tr')[0].find_all('td')[0].text[terminator_1+2:terminator_2]
                contain['date'] = table.find_all('tr')[0].find_all('td')[0].text[terminator_2+2:].rstrip()
                return contain
        
        if contain['day'] == '' or contain['date'] == '':
            raise Exception('There is no information about day and data')

    
    def subject_parse(self, table: BeautifulSoup.Tag) ->list:

        def eject_data(row: int, column: int, table: BeautifulSoup.Tag) ->list:
            count = 0
            while table.find_all('tr')[row+2].find('td').text.strip() == str(count+1):
                pass
        


         # search for the position of group number in row
        def find_position(table: BeautifulSoup.Tag) ->int:
            for r in range(0, len(table.find_all('tr'))-1):
                if table.find_all('tr')[r].find('td').text.strip() == '№':
                    for col in range(1, len(table.find_all('tr')[r].find_all('td'))):
                        if table.find_all('tr')[r].find_all('td')[col].text.strip() == str(self.group):
                            return r, col

            raise Exception('No such grop number here')

        
        row, column = find_position(table)
        return eject_data(row, column, table)

        
    def show(self):
        pass


    class Pare():
        def __init__(self, number, main_content, classroom_number):
            self.number = number
            self.main_content = main_content
            self.classroom_number = classroom_number
