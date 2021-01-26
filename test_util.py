import util


class TestFloats:

    def setup(self):
        print("\nthis is setup")

    def teardown(self):
        print("\nthis is teardown")

    def setup_class(cls):
        print("\nthis is teardown class")

    def teardown_class(cls):
        print("\nthis is teardown class")

    def test_float_rounds_down(self):
        result = util.str_to_int('1.99')
        assert result == 1

    def test_float_round_down_lesser_half(self):
        result = util.str_to_int('1.2')
        assert result == 1
