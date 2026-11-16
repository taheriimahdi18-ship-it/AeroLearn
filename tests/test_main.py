"""Regression tests for the AeroLearn console entry point."""

import importlib.util
import subprocess
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
MAIN_PATH = PROJECT_ROOT / "main.py"
EXPECTED_BANNER = (
    "================================\n"
    "       AeroLearn v0.1.0\n"
    " Aerospace Engineering Software\n"
    "================================\n"
    "Python environment is working!\n"
)


class MainTests(unittest.TestCase):
    """Check the callable, script, and import behavior independently."""

    def test_main_prints_banner_and_returns_none(self) -> None:
        """Calling main preserves the complete banner and return contract."""
        spec = importlib.util.spec_from_file_location("main", MAIN_PATH)
        if spec is None or spec.loader is None:
            self.fail("Could not load the AeroLearn entry point.")
        module = importlib.util.module_from_spec(spec)
        stdout = StringIO()
        stderr = StringIO()

        with redirect_stdout(stdout), redirect_stderr(stderr):
            spec.loader.exec_module(module)
            result = module.main()

        self.assertIsNone(result)
        self.assertEqual(stdout.getvalue(), EXPECTED_BANNER)
        self.assertEqual(stderr.getvalue(), "")

    def test_script_execution_prints_banner_and_exits_successfully(self) -> None:
        """Running main.py prints the banner once and exits successfully."""
        result = subprocess.run(
            [sys.executable, str(MAIN_PATH)],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, EXPECTED_BANNER)
        self.assertEqual(result.stderr, "")

    def test_import_is_silent_and_exposes_main(self) -> None:
        """A fresh interpreter can import a callable main without output."""
        result = subprocess.run(
            [sys.executable, "-c", "import main; assert callable(main.main)"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
