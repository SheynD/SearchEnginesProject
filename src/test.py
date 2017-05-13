from elasticsearch import Elasticsearch
import json
import index

es = Elasticsearch()

dataset1 = {
	'title': 'dataSet1',
	'text': "I'm the first data set",
}

dataset2 = {
	'title': 'dataSet2',
	'text': "I'm the second data set",
}

dataset3 = {
	'title': 'dataSet3',
	'text': "I'm the third data set",
}

def simpleIndex():
	index.initIndex("simpletest")
	res = es.index(index="simpletest", body=dataset1)
	print(res)

	res = es.index(index="simpletest", body=dataset2)
	print(res)

	res = es.index(index="simpletest", body=dataset3)
	print(res)

	es.indices.refresh(index="simpletest")

	res = es.search(index="simpletest", body={"query": {"match_all": {}}})

	source = []
	print("Got %d Hits:" % res['hits']['total'])
	for hit in res['hits']['hits']:
		source.append(hit["_source"])

	print(json.dumps(source))









