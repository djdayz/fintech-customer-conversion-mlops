from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]


def test_required_directories_exist():
    required_dirs = [
        "data/raw",
        "data/processed",
        "docs",
        "notebooks",
        "src/fintech_mlops",
        "tests",
        "models",
        "reports/figures",
        "configs",
        "api",
    ]

    for directory in required_dirs:
        assert (ROOT / directory).exists(), f"Missing directory: {directory}"


def test_required_project_files_exist():
    required_files = [
        "README.md",
        "requirements.txt",
        "Makefile",
        "docs/problem_statement.md",
        "docs/system_design.md",
        "docs/chapter_01_checklist.md",
        "docs/chapter_02_notes.md",
        "docs/user_stories.md",
        "src/fintech_mlops/__init__.py",
        "configs/config.yaml",
    ]

    for file_path in required_files:
        assert (ROOT / file_path).exists(), f"Missing file: {file_path}"


def test_eda_notebook_is_valid_json():
    notebook_path = ROOT / "notebooks" / "01_eda.ipynb"

    with notebook_path.open("r", encoding="utf-8") as file:
        notebook = json.load(file)

    assert notebook["nbformat"] == 4
    assert "cells" in notebook
