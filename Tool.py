import csv
from time import *

import pythonping

error_log = open('error_log.csv', 'a', newline='')
eWriter = csv.writer(error_log)


def ping_result(ip) -> tuple:
    """

    :param ip: could be a ip address or any web name
    :return: a tuple return[0] is a flag of success a[1] is the time or error info
    """
    try:
        a = pythonping.ping(target=ip, count=1)
    except Exception as e:
        data = [asctime(localtime(time())), e]
        eWriter.writerow(data)
        return False, 'Error check log file'
    a = str(a)
    pos1 = a.find('in ') + 3
    pos2 = a.find('ms')
    if pos1 is -1:
        return False, 'Timeout'
    else:
        return True, a[pos1:pos2]
