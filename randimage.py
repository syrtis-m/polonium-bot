#.woop command. goal of this is to send a random image of wooper

import csv


class randimage():

    images = set()

    def __init__(self, file):                
        self.images = set()
        with open(file, newline='') as file_input: #this bit of code should read in lines from the csv of wooper images
            file_reader = csv.reader(file_input)
            for row in file_reader:
                self.images.add(str(row))


    def rand(self):
        result = self.images.pop()
        result = result.replace("'","")
        result = result.strip("[]")
        self.images.add(result)
        return(result)