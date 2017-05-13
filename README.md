# SearchEnginesProject
The final project(s) for the course CSE 445, WWW Search Engines.
## Installation
First, we must make sure elastic search and kibana are installed.
```
brew install elasticsearch
brew install kibana
```
Python version must also be > 2.7
We are going to also want to install elastic search in Python
``pip install elasticsearch``

Once we move to indexing all of the datasets we are going to run out of JVM heap space.
A solution to this was to switch to 4GB of RAM. Change the `/usr/local/etc/elasticsearch/jvm.options`.
Change the default `-Xms2g` & `-Xmx2g` to 4GB each. Or half your RAM size.  


## Simple Python Usage
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
A useful query term to see utility is `./main search "Alabama"

## Advanced HTML Usage
We have designed an html webpage that queries elastic search dynamicly as the user types into the search bar. 
Queries are run using the ElasticUI javascript files. ElasticUI provides a convenient way to wrap Angular-Elastic
queries into easy to use functions and widgets. The word cloud is create us the D3 javascript library. D3 is a 
common data visualization tool. The word cloud is populated using the top frequent keywords in the data base. Ideally,
this should be dynamic, but it proved to be very difficult in HTML/JS.

To run everything:
	- 1) start up elastic search
	- 2) create "data" directory in root directory
	- 3) populate data directory with data sets found in Google Drive link (One is already provided)
	- 4) `cd src`
	- 5) `./main init` This will index all of the data sets. Should take a long time if starting fresh
	- 6) Once finished, open webUI/search.html in local browser
	- 7) Query in search bar
### Problems between ElasticUI & your elasticsearch node
There seems to be a strange problem where you can't run elastic search on your localhost, then try and query localhost
from an html page. HTML just wont let it happen. I found that using the following chrome extension solved the issue.
Unfortunately, I see no other way around it. Make sure it is on, when using search.html 
```
https://chrome.google.com/webstore/detail/allow-control-allow-origi/nlfbmbojpeacfghkpbjhddihlkkiljbi?hl=en
```


## Data Set
Here will be a Google Drive link to the full data set zip file
```
https://drive.google.com/open?id=0B0SxqlhtYz_kZjZra1hCQ3J3aGM
```

## Next Steps
- Improve the UI. Add color. Add Checklist widget to fine tune returned data from the phrase query
- Add some kind of visualization of the dataSets
- Make the word cloud dynamic at runtime
	- Use all terms in the data base as opposed to just keywords
- Solve sharding issue, where different shards are returned, but the same index/dataset

## Useful Tools
- Kibana
	- data visualization tool for elastic search
	- https://www.elastic.co/products/kibana
