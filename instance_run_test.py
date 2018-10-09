import os

import requests

if __name__ == '__main__':
    # file_path = '512MB.zip'
    file_path = 'test.file'
    data = {'token': 'testtoken'}
    url = 'http://staging.api.simverse.com/v1/files'
    instance_id = requests.get('http://169.254.169.254/latest/meta-data/instance-id').content.decode()
    print(instance_id)

    new_file_path = '{}_{}'.format(file_path, instance_id[2:])
    os.rename(file_path, new_file_path)

    with open(new_file_path, 'r') as up_file:
        files = {'file': up_file}
        response = requests.put(url,
                                files=files,
                                data=data
                                )

    if response.status_code == 201:
        print('Success')
    else:
        raise Exception(response.status_code)

