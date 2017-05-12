# SearchEnginesProject
The final project(s) for the course CSE 445, WWW Search Engines.
## Instalation
First we must make sure elastic search and kibana are installed.
```
brew install elasticsearch
brew install kibana
```
Python version must also be > 2.7
We are going to also want to install elastic search in python
``pip install elasticsearch``

Once we move to indexing all of the datasets we are going to run our of JVM heap space.
A solution to this was to switch to 4GB of RAM. Change the `/usr/local/etc/elasticsearch/jvm.options`.
Change the default `-Xms2g` & `-Xmx2g` to 4g each. Or half your RAM size.  

## Simple Usage
First run the elasticsearch server by typing `elasticsearch`
We are currently only indexing one directory of csv files
To create an initial database please do:

```
$ ./main test
$ ./main init
$ ./main search [query term]
```

test will create a small index of a few dataset and respond to a query. Use this to make sure elastic search is working.
init will create an index of one csv file in the data folder. 
Search will run a query on all indices in the database and return the corresponding csv files

## Next Steps
- What kind of queries are we going to be issuing? Just simply "Alabama"? or is it more complex?
- What are we doing with these responses?
	- We have the ability to return:
		- ``datasetName``
		- ``datasetDescription``
		- ``datasetDistribution``
			- ``title``
			- ``downloadURL``
			- ``format``
			- ``description``
		- ``keyword``
		- ``filename``
		- ``attrList``
	- Should we have the JavaScript ask the user for a query, find the dataset, then a screen with description and link to the download?


## Useful Tools
- Kibana
	- data visualization tool for elastic search
	- https://www.elastic.co/products/kibana
