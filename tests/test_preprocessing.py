import pandas as pd
from modeltools.preprocessing import get_numerical_features # Hay que importar las funciones que hay que testearpyte

def test_get_numerical_features_simple():
    """En este vamos a probar que logra distinguir
    entre cadenas de texto y número enteros"""

    df = pd.DataFrame({
      "numerica": [5],
      "categorica": ["rojo"]
    })

    # assert es "como un if" pero que falla si la condición
    # es falsa. Esto es ideal para los tests.

    assert get_numerical_features(df) == ["numerica"]


def test_get_numerical_features_empty():
    """Este test comprueba que se devuelve una lista vacía si no hay ninguna variable num."""
    
    df = pd.DataFrame({
      "categorica": ["rojo"]
    })
    assert get_numerical_features(df) == []
    

def test_get_numerical_features_zero_columns():
    """Este test comprueba que se devuelve una lista vacía si el dataframe no tiene ninguna columna."""
    
    assert get_numerical_features(pd.DataFrame()) == []

def test_get_numerical_features_zero_rows():
    """Este test comprueba que se devuelve la variable correspondientes
    con una variable si el DF tiene una variable numérica pero NINGUNA FILA."""

    df = pd.DataFrame({
        "numerica": pd.Series(dtype=int)
    })

    assert get_numerical_features(df) == ["numerica"]
    

def test_get_numerical_features_int_and_float():
    """Este test comprueba que funciona correctamente
    cuando hay una columna integer y una flotante"""
    
    df = pd.DataFrame({
      "numerica": [5],
      "numerica2": [5.05]
    })

    assert get_numerical_features(df) == ["numerica", "numerica2"]

def test_get_numerical_features_columns_withoutname():
    """Este test comprueba que funciona correctamente
    cuando hay columnas numéricas sin nombre (columnas
    con numeros/posiciones)"""
    df = pd.DataFrame([
        [1, "a"]
    ])

    assert get_numerical_features(df) == [0]

def test_get_numerical_features_complex():
    """Este test comprueba que funciona correctamente con número complejos."""

    df = pd.DataFrame({
        "compleja": [complex(3, 5)]
    })

    assert get_numerical_features(df) == ["compleja"]
