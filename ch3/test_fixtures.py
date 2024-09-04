"""Demonstrate simple fixtures."""

import pytest

@pytest.fixture()
def some_list():
    """Return some list."""
    return [0, 1, 2, 3]


@pytest.fixture(scope="module")
def some_dict():
    """Return some dictionary."""
    print('-------------------')
    yield {1: "test", 2: "test", 3: "test"}
    print('-------------------')

def test_some_list(some_list):
    """Try to use valid list."""
    assert [0, 1, 2, 3] == some_list


def test_some_dict(some_dict):
    """Try to use valid dict."""
    assert {1: "test", 2: "test", 3: "test"} == some_dict


def test_len_some_dict(some_dict):
    assert 3 == len(some_dict)


@pytest.fixture()
def some_data():
    """Return answer to ultimate question."""
    return 42


def test_some_data(some_data):
    """Use fixture return value in a test."""
    assert some_data == 42


@pytest.fixture()
def some_other_data():
    """Raise an exception from fixture."""
    x = 43
    assert x == 42
    return x


def test_other_data(some_other_data):
    """Try to use failing fixture."""
    assert some_data == 42


@pytest.fixture()
def a_tuple():
    """Return something more interesting."""
    return (1, 'foo', None, {'bar': 23})


def test_a_tuple(a_tuple):
    """Demo the a_tuple fixture."""
    assert a_tuple[3]['bar'] == 32
