from flask import Flask, request, jsonify
import pytest

from pathlib import Path
import sys
path_root = Path(__file__).parents[1] #[2]
sys.path.append(str(path_root))
from main import app

def test_response_endpoint():
    response = app.test_client().get('/gcd?A=12&B=10')
    assert response.status_code == 200

def test_response_endpoint_error():
    response = app.test_client().get('/gcd?A=12&B=10&C=20')
    assert response.status_code == 400

def test_get_data():
    response = app.test_client().get('/gcd?A=12&B=10')
    assert response.json == 2