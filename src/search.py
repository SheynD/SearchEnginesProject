from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
import json

es = Elasticsearch()
s = Search(using=es)


def search(term):
    res = es.search(index="_all", body={"query": {"query_string": {"query": term}}})
    source = []
    for doc in res['hits']['hits']:
        if doc['_source']['filename'] not in source:
            source.append(doc['_source']['filename'])

    print("%d documents found" % len(source))
    print(json.dumps(source))

