from requests_haor import RequestHaor
import requests

URL = "http://jsonip.com/"

with RequestHaor(proxy_count=5) as requests_haor:
    for _ in range(10):
        try:
            resp = requests_haor.get(URL)

            if resp.ok:
                print(resp.text)

        except Exception as e:
            print(e)
