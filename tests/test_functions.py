# Importo la funcion gcd_euclides
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))
from src.functions.gcd_euclides import gcd_euclides

import pytest

def test_answer():
    assert gcd_euclides(12, 8) == 4
    
@pytest.mark.parametrize("a, b, expected", 
    [
        (12, 8, 4),
        (10, 20, 10),
        (13, 17, 1),
    ]
)
def test_multiple(a, b, expected):
    assert gcd_euclides(a, b) == expected