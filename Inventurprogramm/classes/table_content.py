from .csv_handler import CSVHandler

#tests for CSV Handler
# CSVHandler.add_record(['N358', 'Notebook', 'Sony', '16.05.2024', 119.99, 'Development', 4011])
# print (CSVHandler.read_all_records())
# CSVHandler.delete_record('N356')

class TableContent:

    @staticmethod
    def get_tablecontent():

        data = CSVHandler.read_all_records() 
        tablecontent = ''

        for record in data:
            tablecontent += '<tr>'
            for atribute in record:
                tablecontent += '<td>' + atribute + '</td>'
            tablecontent += '<td><a href=\'/delete_record/' + record[0] + '\'>löschen</a></td><tr>'    

        return tablecontent

print (TableContent.get_tablecontent)        