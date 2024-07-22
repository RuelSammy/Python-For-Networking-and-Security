from torrequest import TorRequest

with TorRequest(proxy_port=9050, ctrl_port=9051, password=None) as tr:
    response = tr.get('http://ipecho.net/plain')
    print("Current IP:", response.text.strip())
    
    print("Control interface type:", type(tr.ctrl))
    
    # Clear DNS cache
    tr.ctrl.signal('CLEARDNSCACHE')
    
    # Reset identity to get a new IP address
    tr.reset_identity()
    
    response = tr.get('http://httpbin.org/ip')
    print("New IP:", response.text)
