import argparse

import pytest


@pytest.fixture
def sample_args(tmp_path):
    file_path = tmp_path / "sample_file.txt"
    file_path.write_bytes(b"This is a sample file for testing.\n")

    args = argparse.Namespace(
        bytes=True,
        lines=True,
        words=True,
        chars=True,
        file=file_path.open("rb"),
    )

    return args
