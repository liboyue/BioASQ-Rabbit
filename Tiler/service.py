from deiis.rabbit import Task, Message
from deiis.model import Serializer

from Concatenation import Concatenation
import sys



if __name__ == "__main__":
    print 'Starting Tiler services.'
    host = sys.argv[1]
    print("Tiler host: " + host)
    task = Concatenation(host)
    task.start()
    task.wait_for()


