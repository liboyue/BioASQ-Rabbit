from ResultsCollector import ResultsCollector
import sys

if __name__ == '__main__':
    print 'Starting ResultsCollector'
    host = sys.argv[1]
    task = ResultsCollector(host)
    task.start()
    print 'Waiting for the task to terminate.'
    task.wait_for()
    print 'Done.'
