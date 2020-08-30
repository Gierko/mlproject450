
import mlproject

from mlproject.tools import haversine
import pytest

def test_haversine():

    out = haversine(48.865070, 2.380009, 48.8150576, 2.4595967)

    assert out == 10.449355318910523
