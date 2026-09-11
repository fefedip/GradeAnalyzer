from esame import Esame
from analyzer import Analyzer

def test_media_ponderata():
    analyzer = Analyzer.__new__(Analyzer)  # crea l'oggetto SENZA chiamare __init__
    analyzer.lista_esami = [
        Esame("Test A", 12, 30),
        Esame("Test B", 3, 18)
    ]
    
    risultato = analyzer.calculate_weighted_average()
    assert risultato == 27.6

def test_media_aritmetica():
    analyzer = Analyzer.__new__(Analyzer)  # crea l'oggetto SENZA chiamare __init__
    analyzer.lista_esami = [
        Esame("Test A", 12, 30),
        Esame("Test B", 3, 18)
    ]
    
    risultato = analyzer.calculate_average()
    assert risultato == 24

def test_previsione():
    analyzer = Analyzer.__new__(Analyzer)  # crea l'oggetto SENZA chiamare __init__
    analyzer.lista_esami = [
        Esame("Test A", 12, 30),
        Esame("Test B", 3, 18)
    ]

    cfu=6
    traguardo=25
    voto = analyzer.estimate_vote_for_average(traguardo, cfu)
    assert voto == 18.5

def test_previsione_fail():
    analyzer = Analyzer.__new__(Analyzer)  # crea l'oggetto SENZA chiamare __init__
    analyzer.lista_esami = [
        Esame("Test A", 12, 30),
        Esame("Test B", 3, 18)
    ]

    cfu=9
    traguardo=30
    voto = analyzer.estimate_vote_for_average(traguardo, cfu)
    assert voto is None

