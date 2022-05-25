import xmltodict
import requests
import sqlite3
import os

"""
Fetches Israel's Knesset's ODATA laws XML and inserts them in a newly created 
sqlite3 DB
"""


def query_and_print(query: str):
    """
    Receives a SQL query, executes and prints the output
    this method is used for presentation and testing

    >>> query_and_print('SELECT TypeID from laws where LawID == 2001430')
    6002

    >>> query_and_print('SELECT Name from laws where LawID == 2001456 and TypeID == 6001')
    תיקון טעות דפוס בחוק לתיקון חוק בול ביטחון (תיקון והארכת תקופת ההיטל) (תיקון מס' 11), התשל"ה-1975

    >>> query_and_print('SELECT PublicationSeriesID from laws where LawID == 2001456 and TypeID == 6001')
    6071

    >>> query_and_print('SELECT LastUpdatedDate from laws where LawID == 2001456 and TypeID == 6001')
    2021-01-27T22:45:56.127
    """
    db, cursor = restart_db()
    xml_dict = fetch_laws_xml()
    laws_list = generate_laws_list(xml_dict)
    insert_laws_list(db, cursor, laws_list)
    cursor.execute(f'{query}')
    for row in cursor:
        if len(row) == 1:
            print(row[0])
        else:
            print(row)


def restart_db():
    """
    Will delete and recreate an empty sqlite database for exercising
    this method is used for constant recreating and testing of the database
    and should not be implemented outside of this exercise framework

    :return: The created database and cursor objects
    """
    try:
        os.remove('laws_database.db')
    except FileNotFoundError:
        pass
    db = sqlite3.connect('laws_database.db')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE laws(
            LawID	int,
            TypeID	int,
            TypeDesc	varchar (125),
            SubTypeID	int,
            SubTypeDesc	varchar (125),
            KnessetNum	int,
            Name	varchar (255),
            PublicationDate	datetime2,
            PublicationSeriesID	int,
            PublicationSeriesDesc	varchar (125),
            MagazineNumber	varchar (50),
            PageNumber	varchar (50),
            LastUpdatedDate	datetime2)
    ''')
    return db, cursor


def fetch_laws_xml() -> dict:
    """
    Sends a request in order to fetch the laws database XML
    then formats it to a dict/json format

    :return: dictionary representation of all the entries in the XML
    """
    url = 'http://knesset.gov.il/Odata/ParliamentInfo.svc/KNS_Law()'
    req = requests.get(url)
    xml_dict = xmltodict.parse(req.content.decode())['feed']['entry']
    return xml_dict


def generate_laws_list(xml_dict: dict) -> list:
    """
    Iterates over the laws dictionary and generates a
    list of tuples for the db cursor to insert into the newly created DB

    :param xml_dict: dict representation of the XML database
    :return: list of tuples that is formatted in the order for db cursor to add many listing
    to the database
    """
    laws_list = []
    for law in xml_dict:
        current_law = []
        for law_column, law_content in law['content']['m:properties'].items():
            if type(law_content) == dict:
                try:
                    current_law.append(law_content['#text'])
                except KeyError:
                    current_law.append("None")
            else:
                current_law.append(law_content)
        laws_list.append(tuple(current_law))
    return laws_list


def insert_laws_list(db, cursor, laws_list):
    """
    Inserts a generated list of tuples into the received database
    cursor

    :param db: sqlite3 databse cursor object
    """
    cursor.executemany('''
        INSERT INTO laws(
            LawID,
            TypeID,
            TypeDesc,
            SubTypeID,
            SubTypeDesc,
            KnessetNum,
            Name,
            PublicationDate,
            PublicationSeriesID,
            PublicationSeriesDesc,
            MagazineNumber,
            PageNumber,
            LastUpdatedDate
            )
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
    ''', laws_list)
    db.commit()


if __name__ == "__main__":
    import doctest
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
