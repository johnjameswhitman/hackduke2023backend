from pathlib import Path


def get_text_fixture(fixture_name: str) -> str:
    """Loads text fixture into a string."""
    with Path(__file__).resolve().parent.joinpath(fixture_name).open() as fixture_file:
        return fixture_file.read()
