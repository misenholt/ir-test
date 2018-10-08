import requests

if __name__ == '__main__':
    # file_path = '512MB.zip'
    file_path = 'test.file'
    data = {'token': 'testtoken'}
    url = 'http://staging.api.simverse.com/v1/files'

    with open(file_path, 'r') as up_file:
        files = {'file': up_file}
        response = requests.put(url,
                                files=files,
                                data=data
                                )
        print(response.status_code)

