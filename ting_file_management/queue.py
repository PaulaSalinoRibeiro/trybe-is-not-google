class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.pop(0)

    def search(self, index):
        data_length = self.__len__()
        if index < 0 or index > data_length - 1:
            raise IndexError

        return self._data[index]
