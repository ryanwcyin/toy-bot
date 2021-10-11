# An end-to-end bot POC :8ball:
A for fun toy project to explore exchange API

## Project structure :seedling:
```
project
├── data  # for temp storage of data
├── notebooks  # for experiments and visualization
├── secrets  # for storing API secrets and keys
│   ├── dev
│   └── prod
├── strategies  # for implement different strategies
├── tests  # unit test for utils functions
└── utils  # get data or other misc functions
```

## Config :gear:
1. install the dependences
   ```
   pip install -Ur requirements.txt
   ```
2. Set up the keys
    create a directory named `dev` inside secrets and put the exchange key and secret in inside.
    e.g.:  
    ```
    secrets
    ├── dev
    │   ├── binance_api_key
    │   └── binance_api_secret
    └── prod
        ├── binance_api_key
        └── binance_api_secret
    ```

## To Run :runner:
To discover the usage:  
```python main.py --help```  

e.g:  
```
# To download data  
python main.py BNBUSDT data/bnbustd.csv 1633970700
# To run backtesting
python main.py bt data/bnbustd.csv 15m
```

## TODO: :ballot_box_with_check:
- [ ] Move data to DB
- [ ] multiple data for backtest
- [ ] Paper trade
- [ ] Send logs to Telegram
- [ ] Streamlit dashboard