from pprint import pprint

import requests

if __name__ == '__main__':
    data = {'token': 'testtoken'}
    url = 'http://staging.api.simverse.com/v1/files'
    response = requests.get(url,
                            # files=files,
                            data=data
                            )

    if response.status_code == 200:
        pprint(response.json())
        print('Success')
    else:
        raise Exception(response.status_code)

