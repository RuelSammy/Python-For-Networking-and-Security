import requests
def get_tor_session():
    session = requests.session()
    session.proxies = {'http': 'socks5h://127.0.0.1:9050','https': 'socks5h://127.0.0.1:9050'}
    return session
print("Default Public IP:",requests.get("http://httpbin.org/ip").text)
session = get_tor_session()
print("IP for Tor connection:",session.get("http://httpbin.org/ip").text)
response = session.get('http://3g2upl4pq6kufc4m.onion')
for key,value in response.headers.items():
    print(key,value)
    