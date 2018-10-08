import requests

if __name__ == '__main__':
    # file_path = '512MB.zip'
    file_path = 'test.file'
    data = {'token': 'testtoken'}
    url = 'http://staging.api.simverse.com/v1/files'
    instance_id = requests.get('http://169.254.169.254/latest/meta-data/instance-id').read().decode()

    with open(file_path, 'r') as up_file:
        files = {'file': up_file}
        response = requests.put(url,
                                files=files,
                                data=data
                                )
        assert(response.status_code == 201)

