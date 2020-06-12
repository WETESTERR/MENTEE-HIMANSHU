import pytest


class TestBrowser:
    @pytest.mark.skip(reason="I do not want to run.")
    def test_sample(self,driver):
        pass
