class csv_handler:
    import csv
    FILENAME = 'data/database.csv'

    @staticmethod
    def add_record(bezeichnung: str, typ: str, hersteller: str, anschaffungsdatum: str, anschaffungspreis: float, abteilung: str):
        with open(csv_handler.FILENAME, 'w', newline='') as csvfile:
            record_writer = csv.writer(csvfile, delimiter=' ',
                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            record_writer.writerow([bezeichnung] + [typ] + [hersteller] + [anschaffungsdatum] + [anschaffungspreis] + [abteilung])
    