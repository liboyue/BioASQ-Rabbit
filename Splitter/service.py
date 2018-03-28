from deiis.rabbit import Task, Message
from deiis.model import Serializer, Question, Sentence
#from deiis.json import Serializer, Message
from nltk import word_tokenize, sent_tokenize
import sys

class Splitter(Task):
    def __init__(self, host='localhost'):
        super(Splitter, self).__init__('splitter', host=host)
        print("init splitter")
        self.logger.info("init splitter")

    def perform(self, input):
        print('\nsplitter\n\n')
        message = Serializer.parse(input, Message)
        if message.type == 'command':
            if message.body == 'DIE':
                self.logger.info("Received command message DIE")
                self.stop()
            else:
                self.logger.error('Unknown command message: %s', message.body)

            self.deliver(message)

        question = Question(message.body)
        question.tokens = word_tokenize(question.body)
        for snippet in question.snippets:
            snippet.sentences = sent_tokenize(snippet.text)
            #print(snippet.text)
            print(snippet.sentences)

        message.body = question
        self.deliver(message)

    def tokenize(self, text):
        sentences = []
        for s in sent_tokenize(text):
            sentence = Sentence(s)
            sentence.tokens = word_tokenize(s)
            sentences.append(sentence)
        return sentences

if __name__ == '__main__':
    print 'Declaring splitter service'
    host = sys.argv[1]
    service = Splitter(host)
    print("splitter host: " + host)

    print 'Staring splitter service'
    service.start()

    print 'Waiting for splitter service to terminate'
    service.wait_for()

    print 'Splitter stopped.'
