**The role of backend is to obtain data from web3 exchanges using the cctx open source software library.**

# usage

## 1、 Getting Third-party libraries

[ccxt information](https://github.com/ccxt/ccxt/tree/master)

```bash
    pip install pymysql 
    pip install ccxt
    pip install tenacity
```

## 2、 Configuring SQL information

- Replace the following fields in __*config.py*__, including host , port, user and password, etc.
- SQL information can be obtained from [TiDB Cloud](https://dev.tidbcloud.com/console/clusters).

```python
    # example
    hostVal = "127.0.0.1"
    portVal = 3306
    userVal = "root"
    passwordVal = ""
    databaseVal = "web3_exchange_data"
    # ssl_mode="VERIFY_IDENTITY",
    sslVal = {
        "ca": "/etc/ssl/cert.pem"
    }
```

# 3、run example

- run __*main.py*__.

```bash
    python main.py
```