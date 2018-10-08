import datetime

if __name__ == '__main__':
    ct = datetime.datetime.now()

    with open('/home/ubuntu/test.log') as log:
        log.write('...')
        log.write(str(ct))

