import pytest

from tests.conftest import driver


class TestBrowser:

    @pytest.mark.skip("Just a Test Browser.")
    def test_sample(self,driver):
        pass
