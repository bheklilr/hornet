from unittest import TestCase

from hornet import Hornet


class TestHornet(TestCase):
    def test_construction(self):
        Hornet()

    def test_construction_with_items(self):
        Hornet([('a', 1), ('b', 2)])

    def test_construction_with_mapping(self):
        Hornet({'a': 1, 'b': 2})

    def test_construction_with_kwargs(self):
        Hornet(a=1, b=2)

    def test_getitem(self):
        h = Hornet(a=1, b=2)
        assert h['a'] == 1
        assert h['b'] == 2

    def test_setitem(self):
        h = Hornet()
        h['a'] = 1
        assert h['a'] == 1

    def test_delitem(self):
        h = Hornet(a=1)
        del h['a']

    def test_iter(self):
        h = Hornet(a=1)
        for k in h:
            assert k == 'a'

    def test_len(self):
        h = Hornet(a=1, b=2)
        assert len(h) == 2

    def test_nested(self):
        h = Hornet(a={'b': 1}, c=2, d={'e': {'f': 3}})
        assert h['a']['b'] == 1
        assert isinstance(h['a'], Hornet)
        assert isinstance(h['d']['e'], Hornet)
        assert h['d']['e']['f'] == 3
