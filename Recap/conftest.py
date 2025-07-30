import pytest

from Recap.test_data import form_data


@pytest.fixture(params=form_data)

def tesstdata(request):
    return request.param