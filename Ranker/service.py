# import logging
# from logging.config import fileConfig
# logging.config.fileConfig('logging.ini')

from CoreMMR import CoreMMR
from SoftMMR import SoftMMR
from HardMMR import HardMMR
import sys

if __name__ == '__main__':
    print 'Declaring the services'
    host = sys.argv[1]
    print("MMR host: " + host)
    services = list()
    services.append(CoreMMR(host=host))
    services.append(SoftMMR(host=host))
    services.append(HardMMR(host=host))

    print 'Staring the services'
    for service in services:
        service.start()

    print 'Waiting for the services to terminate'
    for service in services:
        print 'Waiting for service {}'.format(service.__class__.__name__)
        service.wait_for()

    print 'Done.'
