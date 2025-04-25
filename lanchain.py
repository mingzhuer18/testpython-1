from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model
import os, getpass
from dotenv import load_dotenv

import requests
#
# proxies = {
#     "http": "http://web-proxy.in.softwaregrp.net:8080",  # HTTP 代理
#     "https": "http://web-proxy.in.softwaregrp.net:8080",  # HTTPS 代理
# }

os.environ["HTTP_PROXY"] ="http://web-proxy.in.softwaregrp.net:8080"
os.environ["HTTPS_PROXY"] ="http://web-proxy.in.softwaregrp.net:8080"
try:
    response = requests.get("https://api.openai.com", timeout=5)
    # response = requests.get("https://www.baidu.com", timeout=5)
    print("网络连接正常" if response.status_code < 500 else "API服务可能不可用")
except Exception as e:
    print(f"网络连接失败: {str(e)}")

