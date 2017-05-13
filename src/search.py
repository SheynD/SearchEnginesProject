from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import json

es = Elasticsearch()
s = Search(using=es)


def search(term):
    res = es.search(index="_all", body={"query": {"query_string": {"query": term}}})
    source = []
    url = []
    for doc in res['hits']['hits']:
        if doc['_source']['Filename'] not in source:
            source.append(doc['_source']['Filename'])
            for dataURL in doc['_source']['Distribution']:
                url.append(dataURL)

    if(len(source)>0):
        print("%d documents found" % len(source))
        for index, item in enumerate(source):
            #print("Document Found: %s \t URL Associated: %s" % (item , url[index]))
            print("Document Found: %s" % item )
    else:
        print("No documents containin the query: %s were found" % term)

def searchUI():
    #Performs an aggregate of all Keywords
    my_body = {
   "size": 0, 
   "aggregations": {
      "Keywords": {
         "terms": {
            "field": "Keywords"
            , "size": 10
             }
          }
       }
    }
    aggr = []
    res = es.search(index="_all", body=my_body)
    for doc in res['aggregations']['Keywords']['buckets']:
        aggr.append(doc)
    for word in aggr:
        print("Keyword: %-15s Frequency: %s" % (word['key'],word['doc_count']))


