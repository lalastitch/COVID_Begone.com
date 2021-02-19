from collections import defaultdict, namedtuple
import os


def CountyDict():
    countyDict = defaultdict(list)
    empty = []
    document_path = os.getcwd()+'\\backend\\County vaccination information.txt'
    document = open(document_path, 'r')
    for section in open(document_path, "r"):
        line = section.strip().split(";")
        for i in line[1:]:
            empty.append(i)
        countyDict[line[0].lower()].append(tuple(empty))
        empty = []
    return countyDict


class VaccinesZipcode():

    def __getitem__(self, county):
        dictofCounties = CountyDict()
        # looks up county name in dictionary and returns the vaccination information
        return dictofCounties[county.lower()]


def getItem(county):
    dictofCounties = CountyDict()
    return {"results": dictofCounties[county.lower()]}
