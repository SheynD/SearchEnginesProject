from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import json

es = Elasticsearch()
s = Search(using=es)


def search(term):
    res = es.search(index="_all", body={"query": {"query_string": {"query": term}}})
    print("%d documents found" % res['hits']['total'])
    source = []
    for doc in res['hits']['hits']:
        for file in doc['_source']['datasetDistribution']:
            if file['title'] not in source:
                source.append(file['title'])

    print(json.dumps(source))

