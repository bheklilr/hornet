from collections import Mapping, MutableMapping


class Hornet(MutableMapping):
    OBJECT_PAIRS_HOOK = dict

    _underlying_mapping = OBJECT_PAIRS_HOOK()

    def __init__(self, items=(), **kwargs):
        if isinstance(items, Mapping):
            items = items.items()
        for k, v in items:
            if isinstance(v, Mapping):
                v = type(self)(v)
            self._underlying_mapping[k] = v
        for k, v in kwargs.items():
            if isinstance(v, Mapping):
                v = type(self)(v)
            self._underlying_mapping[k] = v

    def __getitem__(self, key):
        if isinstance(key, tuple):
            node = self
            for part in key:
                node = node[part]
            return node
        return self._underlying_mapping[key]

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            node = self
            for part in key[:-1]:
                node = node[part]
            node[key[-1]] = value
        else:
            self._underlying_mapping[key] = value

    def __delitem__(self, key):
        del self._underlying_mapping[key]

    def __iter__(self):
        return iter(self._underlying_mapping)

    def __len__(self):
        return len(self._underlying_mapping)

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value
