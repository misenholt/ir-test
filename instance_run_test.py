import datetime

if __name__ == '__main__':
    ct = datetime.datetime.now()

    with open('test.log') as log:
        log.write(ct)

