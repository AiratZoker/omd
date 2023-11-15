from morse import decode
import pytest


@pytest.mark.parametrize(
    "source_string, result",
    [
        ("... --- ...", "SOS"),
        ('.- ...- .. - ---', "AVITO"),
        ('.... .--', "HW")
    ],
)
def test_decode(source_string, result):
    assert decode(source_string) == result
