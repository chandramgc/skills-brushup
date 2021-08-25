import os
from typing import Optional, List
from pymong import MongoClient

def import_csv():
    """Takes a csv file, converts each row into json, and inserts the rows into mongo """

    
    client = pymongo.MongoClient("mongodb+srv://bluemoon:pE3ovB8BJ2TfJVim@bluemoon-cluster.rwcoi.mongodb.net/sample_restaurants?retryWrites=true&w=majority")
    db = client.restaurants


if __name__ == '__main__':
    import sys, os
    sys.path.append(os.getcwd())
    import_csv()

