from datetime import datetime
from elasticsearch import Elasticsearch
import json
import index

es = Elasticsearch(timeout=500)

dataset1 = {
	'title': '1st dataset',
	'text': "I'm the first data set",
	'timestamp': datetime.now(),
}

dataset2 = {
	'title': '2nd dataset',
	'text': "I'm the second data set",
	'timestamp': datetime.now(),
}

dataset3 = {
	'title': '3rd dataset',
	'text': "I'm the third data set",
	'timestamp': datetime.now(),
}

def simpleIndex():
	index.initIndex("simpletest")
	res = es.index(index="simpletest", doc_type='test', id=1, body=dataset1)
	print(res)

	res = es.index(index="simpletest", doc_type='test', id=2, body=dataset2)
	print(res)

	res = es.index(index="simpletest", doc_type='test', id=3, body=dataset3)
	print(res)

	es.indices.refresh(index="simpletest")

	res = es.search(index="simpletest", body={"query": {"match_all": {}}})

	source = []
	print("Got %d Hits:" % res['hits']['total'])
	for hit in res['hits']['hits']:
		source.append(hit["_source"])

	print(json.dumps(source))









