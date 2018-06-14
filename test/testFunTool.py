import funtools
import pytest

def test_lastfirst():
    assert(funtools.last_first("Oyvor")=="rOyvo")
    assert(funtools.last_first("hei")=="ihe")

def test_mirror():
    assert(funtools.mirror("sa") == "as")
    assert(funtools.mirror("3hei") == "ieh3")
    with pytest.raises(ValueError):
        funtools.mirror(3)


