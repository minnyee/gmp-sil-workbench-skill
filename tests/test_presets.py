"""Compile configuration examples without linking or accessing hardware."""

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INCLUDE = ROOT / "examples" / "preset-layout" / "src" / "user"
CC = shutil.which("gcc") or shutil.which("clang")


@unittest.skipUnless(CC, "GCC or Clang is required for C configuration checks")
class PresetChecks(unittest.TestCase):
    def compile(self, source, *defines):
        return subprocess.run(
            [CC, "-std=c11", "-Wall", "-Wextra", "-Werror", "-pedantic",
             "-fsyntax-only", "-x", "c", "-I", str(INCLUDE), *defines, "-"],
            input=source, text=True, capture_output=True, timeout=30,
        )

    def test_default_configuration(self):
        source = (ROOT / "examples" / "preset-layout" / "check_presets.c").read_text()
        source = source.replace('"src/user/ctrl_settings.h"', '"ctrl_settings.h"')
        result = self.compile(source)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_explicit_control_selection_takes_precedence(self):
        with tempfile.TemporaryDirectory() as temporary:
            header = Path(temporary) / "control.h"
            header.write_text("#define EXAMPLE_CONTROL_DIVIDER 4UL\n", encoding="utf-8")
            result = self.compile(
                '#include "ctrl_settings.h"\n'
                '_Static_assert(APP_CONTROL_HZ == 5000UL, "Build override must win");\n',
                f'-DAPP_CONTROL_PRESET_FILE="{header.as_posix()}"',
            )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_zero_and_nondividing_periods_are_rejected(self):
        for divider in (0, 3):
            with self.subTest(divider=divider), tempfile.TemporaryDirectory() as temporary:
                header = Path(temporary) / "control.h"
                header.write_text(f"#define EXAMPLE_CONTROL_DIVIDER {divider}UL\n", encoding="utf-8")
                result = self.compile(
                    '#include "ctrl_settings.h"\nint example;\n',
                    f'-DAPP_CONTROL_PRESET_FILE="{header.as_posix()}"',
                )
            self.assertNotEqual(result.returncode, 0)

    def test_second_board_selection_is_rejected(self):
        result = self.compile(
            '#include "ctrl_settings.h"\nint example;\n',
            "-DAPP_BOARD_PRESET_SELECTED=1",
        )
        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
