# coding=utf-8
import os
import csv
import json
import sys

from elasticsearch import Elasticsearch

es = Elasticsearch(timeout=500)

reload(sys)
sys.setdefaultencoding('utf8')

def slice_list(input, size=30):
    input_size = len(input)
    slice_size = input_size / size
    remain = input_size % size
    result = []
    iterator = iter(input)
    for i in range(size):
        result.append([])
        for j in range(slice_size):
            result[i].append(iterator.next())
        if remain:
            result[i].append(iterator.next())
            remain -= 1
    return result

def doIndex(indexname, input_data): 
    res = es.index(index=indexname, doc_type='basetype', body=input_data)
    return res['created']

def initIndex(indexname):
    if es.indices.exists(indexname):
        print("deleting '%s' index..." % (indexname))
        res = es.indices.delete(index = indexname)
        print(" response: '%s'" % (res))
    index_settings = {
        "settings": {
            "index.mapping.total_fields.limit": 5000
        },
        "mappings": {
            "basetype": {
                "_all": { "enabled": True  }, 
            "properties": { 
                "data" : {"type": "nested"}
              }
            }
        }
    }
    print("creating '%s' index..." % (indexname))
    res = es.indices.create(index = indexname, body=index_settings)
    print(" response: '%s'" % (res))




def searchDirec():
    DataPath = '../data'
    dataset_count = 0
    dirs = os.listdir(DataPath)
    for dir in dirs:
        jsonPath = os.path.join(DataPath, dir, 'meta.json')
        if os.path.exists(jsonPath):
            metajson = json.load(open(jsonPath))
            print("Indexing DataSet: %s",dir)
            indexname = "dataset" + str(dataset_count)
            initIndex(indexname)
            dataset_count = dataset_count +1;
            for file_name in os.listdir(os.path.join(DataPath, dir)):
                if file_name.endswith('.csv'):
                    filepath = os.path.join(DataPath, dir, file_name)
                    print("Reading file %s",file_name)
                    with open(filepath) as f:
                        csv_file_object = csv.DictReader(f)
                        dataList = list(csv_file_object)
                        attrList = list(dataList[0].keys())
                        dataslices = slice_list(dataList)
                        for index, datagroup in enumerate(dataslices):
                            input_data = {'data': datagroup}
                            input_data['datasetName'] = metajson['title']
                            input_data['datasetDescription'] = metajson['description']
                            input_data['datasetDistribution'] = metajson['distribution']
                            input_data['keyword'] = metajson['keyword']
                            input_data['filename'] = file_name
                            input_data['attrList'] = attrList
                            # index name can be the name of dataset
                            # doc_type name doesn't matter.
                            print('indexing slices %s' % str(index))
                            print(doIndex(indexname, input_data))



    


