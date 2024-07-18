import urllib.request
import re

USER_AGENT = 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36'
url = input("Enter URL (without 'http://'): ")
full_url = 'http://' + url

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', USER_AGENT)]
urllib.request.install_opener(opener)

try:
    response = urllib.request.urlopen(full_url)
    html_content = response.read().decode('utf-8')

    pattern = re.compile(r'[-a-zA-Z0-9._]+@[-a-zA-Z0-9._]+\.[a-zA-Z]+')
    mails = re.findall(pattern, html_content)

    print(mails)
except Exception as e:
    print(f"An error occurred: {e}")
