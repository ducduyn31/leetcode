from typing import List
from collections import OrderedDict


def clazz_runner(steps: List[str], parameters: List[List], out):
    obj = globals()[steps[0]](*parameters[0])
    steps.pop(0)
    parameters.pop(0)

    for f, a in zip(steps, parameters):
        ret_value = getattr(obj, f)(*a)
        if ret_value and out:
            out(ret_value)


class QueueDict:
    def __init__(self):
        self._dict = {}
        self._first = None
        self._last = None

    def enqueue(self, key, value):
        if self._last:
            before, _, v = self._dict[self._last]
            self._dict[self._last] = before, key, v
            self._dict[key] = self._last, None, value
        else:
            self._first = key
            self._dict[key] = (None, None, value)

        self._last = key

    def dequeue(self):
        if len(self) > 0:
            _, after, _ = self._dict[self._first]
            del self._dict[self._first]

            if after:
                _, post_after, post_value = self._dict[after]
                self._dict[after] = None, post_after, post_value
                self._first = after
            else:
                self._last = None

    def pop(self, key):
        my_before, my_after, my_value = self._dict[key]

        if my_before:
            prev_before, _, prev_value = self._dict[my_before]
            self._dict[my_before] = prev_before, my_after, prev_value

        if my_after:
            _, post_after, post_value = self._dict[my_after]
            self._dict[my_after] = my_before, post_after, post_value

        if key == self._first:
            self._first = my_after
        if key == self._last:
            self._last = my_before

        del self._dict[key]
        return my_value

    def __len__(self):
        return len(self._dict)

    def __contains__(self, item):
        return item in self._dict

    def __getitem__(self, item):
        return self._dict[item]


class LRUCache(OrderedDict):

    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return - 1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


if __name__ == '__main__':
    clazz_runner(['LRUCache', 'put', 'put', 'get', 'put', 'put', 'get'],
                 [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]], print)
    # clazz_runner(['LRUCache', 'put', 'put', 'get', 'put', 'get', 'put', 'get', 'get', 'get'],
    #              [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]], print)
