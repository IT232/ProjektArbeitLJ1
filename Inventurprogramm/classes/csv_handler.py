import csv
import os
from .validation import Validation

class CSVHandler:

    FILENAME = 'data/database.csv'
    TEMPFILENAME = 'temp.csv'


    @staticmethod
    def add_record(parameters):
        if len(parameters) != 7: 
            raise ValueError('Expected 7 parameters')

        for i in range(len(parameters)):
            if isinstance(parameters[i], str):
                parameters[i] = parameters[i].strip()

        bezeichnung, typ, hersteller, anschaffungsdatum, anschaffungspreis, abteilung, standort = parameters 

        validation_results = {
            'bezeichnung': Validation.text_validation(bezeichnung),
            'bezeichnung_unique': CSVHandler.find_record(bezeichnung),
            'typ': Validation.text_validation(typ),
            'hersteller': Validation.text_validation(hersteller),
            'anschaffungsdatum': Validation.date_validation(anschaffungsdatum),
            'anschaffungspreis': Validation.price_validation(anschaffungspreis),
            'abteilung': Validation.text_validation(abteilung),
            'standort': Validation.room_validation(standort)
        }

# Einkommentieren zum Debuggen 
        for key, value in validation_results.items():
            print(f'Validation result for {key}: {value}')

        if all(validation_results.values()):
            with open(CSVHandler.FILENAME, 'a', newline='') as csvfile:
                record_writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                record_writer.writerow(parameters)
        else:
            return False     



    @staticmethod
    def read_all_records():
        data_records = []
        with open(CSVHandler.FILENAME, 'r', newline='') as csvfile:
            records_reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in records_reader:
                data_records.append(row)
        return data_records      


    @staticmethod 
    def delete_record(bezeichnung: str):
        with open(CSVHandler.FILENAME, 'r', newline='') as records_csvfile, \
            open(CSVHandler.TEMPFILENAME, 'a', newline='') as temp_csvfile:
            records_reader = csv.reader(records_csvfile, delimiter=';', quotechar='"')
            temp_writer = csv.writer(temp_csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in records_reader:
                if row[0]==bezeichnung:
                    continue
                temp_writer.writerow(row)
        os.remove(CSVHandler.FILENAME)        
        os.rename(CSVHandler.TEMPFILENAME, CSVHandler.FILENAME)

    @staticmethod
    def find_record(bezeichnung):
        with open(CSVHandler.FILENAME, 'r', newline='') as csvfile:
            records_reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for row in records_reader:
                if row[0] == bezeichnung:
                    return False
        return True