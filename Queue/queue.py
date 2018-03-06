import Queue
import time
import threading
import random


class Producer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self, name=name)
        self.que = queue

    def run(self):
        for i in xrange(10):
            num = random.randint(1,99)
            self.que.put(num)
            print "%s is runing,number is %d" %(self.getName(), num)

class Consumer_even(threading.Thread):
    def __init__(self, queue):
        super(Consumer_even,self).__init__()
        self.que = queue

    def run(self):
        while 1:
            try:
                num = self.que.get(1,5)
                if num%2 == 0:
                    print "%s is runing in consumer_even, consume number is %d" %(self.getName(), num)
                else:
                    self.que.put(num)
            except:
                break

class Consumer_odd(threading.Thread):
    def __init__(self, queue):
        super(Consumer_odd,self).__init__()
        self.que = queue

    def run(self):
        while 1:
            try:
                num = self.que.get(1,5)
                if num%2 != 0:
                    print "%s is runing in consumer_odd, consume number is %d" %(self.getName(), num)
                else:
                    self.que.put(num)
            except:
                break


def main():
    q = Queue.Queue()
    #  for i in xrange(10):
        #  num = random.randint(1,99)
        #  q.put(num)
    
    producer = Producer('producer',q)
    consumer_even = Consumer_even(q)
    consumer_odd = Consumer_odd(q)
    producer.start()
    consumer_even.start()
    consumer_odd.start()
    producer.join()
    consumer_even.join()
    consumer_odd.join()

    print "all done"

if __name__ == '__main__':
    main()
