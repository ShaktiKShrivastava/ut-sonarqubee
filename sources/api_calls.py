import requests


def api_call_one(url):
    resp = requests.get(url)
    out = resp.json()
    return out['Value'][0]['status']


def api_call_one_with_exception(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        raise Exception('Error while making the API call')
    out = resp.json()
    return out['Value'][0]['status']


if __name__ == '__main__':
    print(api_call_one('None'))