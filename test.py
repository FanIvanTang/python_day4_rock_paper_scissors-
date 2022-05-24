from main import compete


def test_case_1_compete():

    assert compete(1, 2) == "lost"


def test_case_2_compete():

    assert compete(2, 2) == "tie"


def test_case_3_compete():

    assert compete(0, 1) == "lost"


def test_case_4_compete():

    assert compete(1, 0) == "win"
