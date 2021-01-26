from utils import strtobool
import pytest


class TestStrToBool:
    @pytest.mark.parametrize('user_input', ['y', '1', 'Y', 'yes', 'YES', '', 'YeS   '])
    def test_true_vals(self, user_input):
        assert strtobool(user_input) is True

    @pytest.mark.parametrize('user_input', ['no', 'n', '0'])
    def test_false_vals(self, user_input):
        assert strtobool(user_input) is False

    # commented out individual test for an optimized parametrize test
    # def test_y_is_true(self):
    #     assert strtobool('y') is True

    # def test_1_is_true(self):
    #     assert strtobool('1') is True

    # def test_Y_is_true(self):
    #     assert strtobool('Y') is True

    # def test_yes_is_true(self):
    #     assert strtobool('yes') is True

    # def test_YES_is_true(self):
    #     assert strtobool('YES') is True

    # def test_empty_is_true(self):
    #     assert strtobool("") is True
