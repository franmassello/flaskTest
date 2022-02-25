from pathlib import Path
import sys
import pytest
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from src.functions.gcd_euclides import gcd_euclides

def test_answer():
    assert gcd_euclides(12, 8) == 4
        

