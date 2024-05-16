import csv
import os
import Validation

class CSVHandler:

    FILENAME = 'Inventurprogramm/data/database.csv'
    TEMPFILENAME = 'temp.csv'


    @staticmethod
    def add_record(parameters):
        if len(parameters) != 7: 
            raise ValueError("Expected 7 parameters")
        for atributes in parameters:
            atributes=atributes.strip()

        bezeichnung, typ, hersteller, anschaffungsdatum, anschaffungspreis, abteilung, standort = parameters

        for text in [bezeichnung, typ, hersteller, abteilung]:
            text_validate_result = text_validation(text)
        anschaffungsdatum_validate_result = date_validation(anschaffungsdatum)
        anschaffungspreis_validate_result = price_validation(anschaffungspreis)
        standort_validate_result = room_validation(standort)    

        if bezeichnung_validate_result == True \
        and typ_validate_result == True \
        and hersteller_validate_result == True \
        and anschaffungsdatum_validate_result == True \
        and anschaffungspreis_validate_result == True \
        and text_validate_result == True \
        and standort_validate_result == True:
            with open(CSVHandler.FILENAME, 'a', newline='') as csvfile:
                record_writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                record_writer.writerow([bezeichnung, typ, hersteller, anschaffungsdatum, anschaffungspreis, abteilung, standort])
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

    