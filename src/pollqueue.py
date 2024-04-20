class ArrayQueue:
    'A queue backed with a built-in Python list'

    def __init__(self):
        'Creates an empty ArrayQueue instance'
        self._data = list()

    def enqueue(self, e):
        'Enqueue element at the back of the queue'
        self._data.append(e)

    def dequeue(self):
        '''Dequeue the element from the front of the queue

        Raise exception if the queue is empty
        '''
        if len(self._data) == 0:
            print('The queue is empty')
            exit(1)
        return self._data.pop(0)

    def front(self):
        '''Return a reference to the element at the front

        Raise an exception if the queue is empty
        '''
        if len(self._data) == 0:
            print('The queue is empty')
            exit(1)
        return self._data[0]

    def is_empty(self):
        'Return true if the queue is empty'
        return len(self._data) == 0

    def __len__(self):
        'Return the length of the queue'
        return len(self._data)