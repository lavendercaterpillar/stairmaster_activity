from stairmaster import climbStairs

def test_1_step():
    assert climbStairs(1) == 1

def test_2_step():
    assert climbStairs(2) == 2

def test_3_step():
    assert climbStairs(3) == 3

def test_10_step():
    assert climbStairs(10) == 89

def test_30_step():
    assert climbStairs(30) == 1346269

def test_35_step():
    assert climbStairs(35) == 14930352

def test_40_step():
    assert climbStairs(40) == 165580141

def test_50_step():
    assert climbStairs(50) == 20365011074
