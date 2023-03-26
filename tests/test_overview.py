import attrs
import pytest


@attrs.define
class Some:
    number: int = 42
    numbers: list[int] = attrs.field(factory=list)

    def hard_math(self, another) -> int:
        return self.number + sum(self.numbers) * another


@pytest.fixture
def some() -> Some:
    return Some(1, [1, 2, 3])


@pytest.fixture()
def data(some: Some):
    return {"number": some.number, "numbers": some.numbers}


def test_func(some: Some):
    got = some.hard_math(3)
    assert got == 19, f"{got=}"


def test_as_dict(some: Some, data: dict):
    got = attrs.asdict(some)
    assert got == data, f"{got=}, want={data}"
