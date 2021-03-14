"""Tests for `nondefacedDetector.cli.main`."""

from click.testing import CliRunner
import pytest

from nondefacedDetector.cli import main as climain


def test_info():
    runner = CliRunner()
    result = runner.invoke(climain.cli, ["info"])
    assert result.exit_code == 0
    assert "Python" in result.output
    assert "System" in result.output
    assert "Timestamp" in result.output
