import attrs
import pytest


@attrs.define()
class Empty:
    ...


def test_basic_empty():
    assert Empty() == Empty()
    assert Empty() is not Empty()


@attrs.define()
class Parameters:
    x: int
    y: int


def test_basic_parameter():
    c1 = Parameters(1, 2)
    c2 = Parameters(x=1, y=2)
    c3 = Parameters(**dict(x=1, y=2))

    assert c1 == c2 == c3


@attrs.define()
class Private:
    _x: int


def test_basic_private():
    p1 = Private(x=1)
    p2 = Private(1)

    assert p1 == p2


@attrs.define()
class KeywordOnly:
    v: int = attrs.field(kw_only=True)


def test_keyword_only():
    with pytest.raises(TypeError):
        _ = KeywordOnly(1)

    ko = KeywordOnly(v=1)
    assert ko.v == 1


@attrs.define()
class Coordinates:
    x: int
    y: int


@pytest.fixture()
def coordinates_data():
    return dict(x=0, y=1)


@pytest.fixture()
def coordinates(coordinates_data) -> Coordinates:
    return Coordinates(**coordinates_data)


def test_asdict(coordinates: Coordinates, coordinates_data: dict):
    assert attrs.asdict(coordinates) == coordinates_data


def test_asdict_filter(coordinates: Coordinates, coordinates_data: dict):
    k = "x"
    coordinates_data.pop(k)
    assert attrs.asdict(coordinates, filter=lambda attr, value: attr.name != k) == coordinates_data
