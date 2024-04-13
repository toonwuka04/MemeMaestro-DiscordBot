class Queue:
    'The queue abstract data type'

    def __init__(self):
        'Creates an empty ArrayQueue instance'
        self._data = list()

    def enqueue(self, e):
        'Add element e to the back of the queue'
        pass

    def dequeue(self):
        'Remove and return (first) element from the front of the queue'
        pass

    def first(self):
        'Return a reference to the first element in the queue'
        pass

    def is_empty(self):
        'Return true if the queue is empty'
        pass

    def __len__(self):
        'Return the number of elements in the queue'
        pass