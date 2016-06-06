import os
import pytest
from pypeakflow.peakflow_soap import ConnectionOptions, PeakflowSOAP


def get_auth():
    return (os.environ.get("ARBOR_URL"), os.environ.get("ARBOR_USERNAME"),
            os.environ.get("ARBOR_PASSWORD"))


def have_auth():
    url, user, passwd = get_auth()
    return url is None or user is None or passwd is None


@pytest.fixture
def auth():
    return get_auth()


@pytest.fixture
def pf():
    url, user, passwd = get_auth()
    co = ConnectionOptions(url, user, passwd)
    pf = PeakflowSOAP(co)
    return pf
