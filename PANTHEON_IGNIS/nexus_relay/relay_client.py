import requests
class NexusRelayClient:
    def __init__(self, relay_url):
        self.url = relay_url
    def send_command(self, cmd):
        return requests.post(f"{self.url}/command", json=cmd)
