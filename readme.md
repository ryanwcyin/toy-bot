# An end-to-end bot POC
A for fun toy project to explore exchange API

## Config
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
   
download data
python3.8 download_data.py BNBUSDT data/bnbustd.csv 1633970700
## TODO:
- [ ] Move data to DB
- [ ] Send logs to Telegram
- [ ] Streamlit dashboard