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

1. Clone the repository  
  ```Shell

  git clone https://github.com/aditaa/freeciv-score-graph.git

  cd freeciv-score-graph
  
  ```
2. Set plotly API credentials  
  ```Python
  
  python -c "import plotly; plotly.tools.set_credentials_file(username='user', api_key='key')"
  
  ```
3. Pass the script the log file  
  ```Shell
  
  python freeciv-score-graph.py freeciv-score.log
  
  ```

## Examples
After running the script to will give you a graph like this
![Example](https://github.com/aditaa/freeciv-score-graph/raw/master/examples/-0JINiwF90PDgg9ROm8R7aPQ6r8etHsn.png)
