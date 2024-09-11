# Telegram Follows Exporter

This project is a Python script that uses the Telethon library to export information about Telegram channels, groups, bots and users into a JSON file.

## Requirements

- Python 3
- Telethon library
- SOCKS 5 proxy (optional, if needed)(python_socks rather than pysocks)

## Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/chiqingsong/telegram_follows_backup.git
    cd telegram_follows_backup
    ```

2. **Install Dependencies**
   Ensure you have the necessary Python packages installed. You can install them using pip:

    ```bash
   pip install telethon
   pip install python-socks[asyncio]
    ```

3. **Edit the Configuration**
   Open telegram_follows_backup. ipynb and replace the placeholders with your actual Telegram API credentials:

    ```python
    api_id = ''  # Replace with your API ID
    api_hash = ''  # Replace with your API Hash
    ```

   If you are using a SOCKS5 proxy, ensure the proxy settings are correct:

    ```python
   proxy=(python_socks.ProxyType.SOCKS5, 'yourhost', yourport)  # Update with your proxy details
    ```

4. **Run the Script**
   ```bash
   python -u "...\telegram_export.py"
   ```
## It should be noted that
1. How to get your api_id & api_hash
   https://core.telegram.org/api/obtaining_api_id
2. The telethon Signing In behind a Proxy Doc:[For Python >= 3.6 : install python-socks[asyncio],For Python <= 3.5 : install PySocks](https://docs.telethon.dev/en/stable/basic/signing-in.html#signing-in-behind-a-proxy)
3. Private groups or channels will not be accessible
4. If the telethon or telegram api is changed, it is not guaranteed to remain in effect
5. About Session,you can get your account's session by running this script for the first time, or by going through this [tutorial](https://shef.cc/2023/01/16/%e3%80%90%e6%8a%80%e6%9c%af%e5%90%91%e3%80%91%e5%86%8d%e4%b9%9f%e4%b8%8d%e6%80%95%e6%94%b6%e4%b8%8d%e5%88%b0-telegram-%e7%9a%84%e7%9f%ad%e4%bf%a1%e9%aa%8c%e8%af%81/) (step 3).
6. About proxy,you can google how to get your proxy host and port

## The result 
1. A JSON file
2. The public ones would be like:
```json
   {
    "name": "foo",
    "id": 123456789,
    "access_hash": 00000000000000000000,
    "type": "channel",
    "link": "https://t.me/bar"
    }
```
