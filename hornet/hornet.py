from collections import MutableMapping


class Hornet(MutableMapping):
    def __init__(self, items=(), *, object_pairs_hook=dict):
        pass

    def __getitem__(self, key):
        raise NotImplementedError()

    def __setitem__(self, key, value):
        raise NotImplementedError()

    def __delitem__(self, key, value):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()
