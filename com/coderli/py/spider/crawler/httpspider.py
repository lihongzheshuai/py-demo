import urllib.request

url = "abcd"

class HttpSpider:

    def do_request(self, url):
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        data = resp.read().decode('utf-8')
        return data
