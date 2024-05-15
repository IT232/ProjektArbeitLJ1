import csv
import os

class CSVHandler:

    FILENAME = 'Inventurprogramm/data/database.csv'
    TEMPFILENAME = 'temp.csv'

    @staticmethod
    def add_record(bezeichnung: str, typ: str, hersteller: str, anschaffungsdatum: str, anschaffungspreis: float, abteilung: str, standort: int):
        with open(CSVHandler.FILENAME, 'a', newline='') as csvfile:
            record_writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            record_writer.writerow([bezeichnung] + [typ] + [hersteller] + [anschaffungsdatum] + [anschaffungspreis] + [abteilung] + [standort])

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

    