import datetime
import re

if __name__ == '__main__':
    ct = datetime.datetime.now()
    ct = re.sub(r'[\.: -]', '_', str(ct))

    with open('./{}.log'.format(ct), 'w') as log:
        log.write('...')

