# DXC-Git
A script to easily search for leaked sensitive data belonging to DXC (aswell as HPE and CSC).
  
This script was written by:<br> https://twitter.com/Daley  
https://github.com/0days  

All Credit Goes To Him, in fact, the entire creation of this project is credited to him. By reporting sensitive information found in public repos

## Setup
```
pip3 install -r requirements.txt  
```
## Usage
```
python main.py -h  -- help  
python main.py -dxc, --dxc  -- scan for dxc assets  
python main.py -csc, --csc  -- scan for csc assets   
python main.py -hpe, --hpe  -- scan for hpe assets
python main.py -io, --io  -- scan for dxcdigital.io assets
python main.py -full, --full  -- scan for all assets   
```
<hr>

![dxc-git](https://i.imgur.com/KB6nhmP.gif)
