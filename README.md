# freeciv-score-graph

This is a python script to make graphs from the freeciv score log

## Requirements
* python (This has been tested with python 2.7.5)
* This script also requires Plotly

You can install Plotly using pip

```Shell

sudo pip install plotly

```

## Usage
Usage of this script is very easy 

### Setup

> Remember to check the [Requirements section](#requirements)

1. Clone the repository  
  ```Shell

  git clone https://github.com/aditaa/freeciv-score-graph.git

  cd freeciv-score-graph
  
  ```
2. Set plotly API credentials  
  ```Python
  
  python -c "import plotly; plotly.tools.set_credentials_file(username='user', api_key='key')"
  
  ```


### Get Help

  ```Shell
  
  python freeciv-score-graph.py --help
  
  ```


  ```
$ python freeciv-score-graph.py --help
usage: Freeciv score graph [-h] [-l [LOGFILE]] [--listgraphs]

optional arguments:
  -h, --help            show this help message and exit
  -l [LOGFILE], --logfile [LOGFILE]
                        The FreeCIV score file to proccess
  --listgraphs          Lists graphs and there option numbers

  ```

### Get List of graphs

  ```Shell
  
  python freeciv-score-graph.py --listgraphs
  
  ```

  ```
$ python freeciv-score-graph.py --listgraphs
Key      Description    
--------------------
0        pop            
1        bnp            
2        mfg            
3        cities         
4        techs          
5        munits         
6        settlers       
7        wonders        
8        techout        
9        landarea       
10       settledarea    
11       pollution      
12       literacy       
13       spaceship      
14       gold           
15       taxrate        
16       scirate        
17       luxrate        
18       riots          
19       happypop       
20       contentpop     
21       unhappypop     
22       specialists    
23       gov            
24       corruption     
25       score          
26       unitsbuilt     
27       unitskilled    
28       unitslost      
--------------------
  ```

### Get Graphs
Pass the script the log file  

  ```Shell
  
  python freeciv-score-graph.py -l freeciv-score.log
  
  ```

## Examples
After running the script to will give you a graph like this
![Example](https://github.com/aditaa/freeciv-score-graph/raw/master/examples/-0JINiwF90PDgg9ROm8R7aPQ6r8etHsn.png)
