import csv
from Fight import Fight

class Interview():

    def __init__(file_path):
        if file_path == '' or file_path == None:
            raise Exception('Give me the file!!!')
        

