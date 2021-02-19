from collections import defaultdict, namedtuple

def CountyDict():
    countyDict = defaultdict(list)
    empty = []
    for section in open("County vaccination information.txt","r"):
        line = section.strip().split(";")
        for i in line[1:]:
            empty.append(i)
        countyDict[line[0]].append(tuple(empty))
        empty = []
    return countyDict

class VaccinesZipcode():

    def __getitem__(self, county):
        dictofCounties = CountyDict()
        # looks up county name in dictionary and returns the vaccination information
        return dictofCounties[county]

