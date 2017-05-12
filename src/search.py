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
        if doc['_source']['filename'] not in source:
            source.append(doc['_source']['filename'])
            for dataURL in doc['_source']['datasetDistribution']:
                url.append(dataURL)

    if(len(source)>0):
        print("%d documents found" % len(source))
        for index, item in enumerate(source):
            #print("Document Found: %s \t URL Associated: %s" % (item , url[index]))
            print("Document Found: %s" % item )
    else:
        print("No documents containin the query: %s were found" % term)
