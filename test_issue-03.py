from one_hot_encoder import fit_transform
import unittest


class Test_fit_transform(unittest.TestCase):
    def test_transform_first(self):
        seq = ['Aйрат', 'Закиров', 'Ленарович']
        seq_transform = fit_transform(seq)
        true_transform = [
            ('Aйрат', [0, 0, 1]),
            ('Закиров', [0, 1, 0]),
            ('Ленарович', [1, 0, 0])
        ]
        self.assertEqual(seq_transform, true_transform)

    def test_transform_second(self):
        seq = ['Avito', 'Yandex', 'Avito']
        seq_transform = fit_transform(seq)
        seq_true_transform = [[
            ('Avito', [0, 1]),
            ('Yandex', [1, 0]),
            ('Avito', [0, 1])
        ]]
        self.assertIn(seq_transform, seq_true_transform)

    def test_transform_third(self):
        seq = ['Avito', 'Yandex', 'Avito']
        seq_transform = fit_transform(seq)
        seq_true_transform = [[
            ('Avito', [0, 0, 0]),
            ('Yandex', [0, 0, 1]),
            ('Avito', [0, 1, 0])
        ]]
        self.assertNotIn(seq_transform, seq_true_transform)

    def test_exception(self):
        data = True
        with self.assertRaises(TypeError):
            fit_transform(data)
