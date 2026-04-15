from main calcular_media

def test_media_valores_normais():
    assert calcular_media(7, 8, 9) == 8.0

def test_media_zeros():
    assert calcular_media(0, 0, 0) == 0.0

def test_media_outro_caso():
    assert calcular_media(10, 5, 5) == 20/3