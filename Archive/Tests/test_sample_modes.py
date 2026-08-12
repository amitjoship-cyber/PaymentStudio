"""
Payment Studio
Sample Mode Test
"""

from App.Core.Generation.generation_options import GenerationOptions


def test_sample_modes():

    minimal = GenerationOptions(
        sample="minimal",
    )

    complete = GenerationOptions(
        sample="complete",
    )

    assert minimal.sample == "minimal"
    assert complete.sample == "complete"
