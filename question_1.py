import csv

class HashTable:

    def __init__(self):
        self.size = 100
        self.temps = [[] for i in range(self.size)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.temps[h] += [[key, value]]
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.temps[h]:
            if element[0] == key:
                return element[1]

    def readCsv(self):      
        with open('nyc_weather.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                self.__setitem__(item['date'], int(item['temperature(F)']))
    
    def averaging(self, start, end):
        start_day = int(start.split(' ')[1])
        end_day = int(end.split(' ')[1])
        sum = 0
        
        for day in range(end_day - start_day + 1):
            temp = self.__getitem__('Jan ' + str(day + 1))
            sum += int(temp)
        return sum / (end_day - start_day + 1)
        

output = HashTable()

output.readCsv()





