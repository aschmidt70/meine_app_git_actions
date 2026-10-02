from src.anwendung import differenz, summe, prozent, multiplikation

def test_summe_ganze_zahlen():
    assert summe(2, 3) == 5

def test_summe_mit_null():
    assert summe(0, 7) == 7

def test_differenz():
     assert differenz(10, 4) == 6

def test_prozent():
    assert prozent(2, 4) == 50

def test_ömultiplikation():
    assert multiplikation(5, 6) == 30
