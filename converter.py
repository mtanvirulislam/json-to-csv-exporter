import json
import csv
import collections

headers = ["UsuarioId",
            "queryId",
            "queryType",
            "ddlType",
            "memoryNode",
            "queryStatus",
            "durationMillis",
            "queryState",
            "startTime",
            "endTime",
            "rowsProduced",
            "hdfs_bytes_written",
            "stats_missing",
            "pool",
            "session_type",
            "stats_corrupt",
            "estimated_per_node_peak_memory",
            "rows_inserted",
            "admission_result",
            "planning_wait_time",
            "admission_wait",
            "memory_per_node_peak",
            "coordinator"]

def flatDict(arrayIn):
    allQueries = []
    for item in arrayIn:
        dictInterno = {}
        
        #get values of 
        for key, value in item.items():
            if type(value) is dict:
                #print key, value, type(value)
                for subKey, subValue in value.items():
                    dictInterno[subKey] = subValue
            else:
                dictInterno[key] = value
        
        #print dictInterno
        
        #order elements
        dictInterno = dict(collections.OrderedDict(sorted(dictInterno.items())))
        
        #print len(dictInterno)
        
        allQueries.append(dictInterno)
        
    return allQueries



def normalizeDict(arrayIn):
    allQueries = []
    for item in arrayIn:
        
        #Set null at not existing key
        for fixedKey in headers:
            if fixedKey not in item:
                item[fixedKey] = "null"

        dictInterno = item.copy()

        #Remove keys
        for key, value in item.items():
            if key not in headers:
                del dictInterno[key]

        #print dictInterno
        
        #order elements
        dictInterno = dict(collections.OrderedDict(sorted(dictInterno.items())))
        
        #print len(dictInterno)
        
        allQueries.append(dictInterno)
        
    return allQueries

#====================================================================================================

#main

#read JSON
with open("querifINAL.json") as file:
    data = json.load(file)

#Write CSV
with open("data.csv", "w") as file:
    csv_file = csv.writer(file)

    #Create dict
    dictToWrite = normalizeDict(flatDict(data['queries']))
    
    #Write header
    csv_file.writerow(dictToWrite[0].keys())

    for item in dictToWrite:
        csv_file.writerow(item.values())
