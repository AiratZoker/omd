from one_hot_encoder import fit_transform
import pytest


def test_transform_first():
    seq = ['Aйрат', 'Закиров', 'Ленарович']
    seq_transform = fit_transform(seq)
    true_transform = [
        ('Aйрат', [0, 0, 1]),
        ('Закиров', [0, 1, 0]),
        ('Ленарович', [1, 0, 0])
    ]
    assert seq_transform == true_transform


def test_transform_second():
    seq = ['Avito', 'Yandex', 'Avito']
    seq_transform = fit_transform(seq)
    seq_true_transform = [
        ('Avito', [0, 1]),
        ('Yandex', [1, 0]),
        ('Avito', [0, 1])
    ]
    assert seq_transform == seq_true_transform


def test_transform_third():
    seq = ['Avito', 'Yandex']
    seq_transform = fit_transform(seq)
    seq_true_transform = [
        ('Avito', [0, 1]),
        ('Yandex', [1, 0])
    ]
    assert seq_transform == seq_true_transform


def test_exception():
    data = True
    with pytest.raises(TypeError):
        fit_transform(data)
