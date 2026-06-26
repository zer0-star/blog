#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.12"
# dependencies = ["pyyaml"]
# ///

import argparse
import os
import re
import hashlib
import subprocess
import glob
import tempfile
import yaml

CONTENT_DIR = "content"
SVG_OUT_DIR = "assets/images/latex"

os.makedirs(SVG_OUT_DIR, exist_ok=True)

FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
MATH_BLOCK_PATTERN = re.compile(r"```math\n(.*?)```", re.DOTALL)

force = False


def process_markdown_file(working_dir: str, filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    preamble = ""
    fm_match = FRONTMATTER_PATTERN.match(content)
    if fm_match:
        try:
            fm_data = yaml.safe_load(fm_match.group(1))
            if fm_data and "preamble" in fm_data:
                preamble = fm_data["preamble"]
        except yaml.YAMLError:
            print(f"Warning: Frontmatter parse error in {filepath}")

    matches = MATH_BLOCK_PATTERN.finditer(content)
    for match in matches:
        math_code = match.group(1).strip()

        hash_text = preamble + math_code

        file_hash = hashlib.sha256(hash_text.encode()).hexdigest()

        generate_svg(working_dir, file_hash, preamble, math_code)


def generate_svg(working_dir, file_hash, preamble, math_code):
    svg_path = os.path.join(SVG_OUT_DIR, f"{file_hash}.svg")

    if not force and os.path.exists(svg_path):
        return

    print(f"Generating SVG for hash: {file_hash[:8]}...")

    tex_filename = f"{file_hash}.tex"
    tex_filepath = os.path.join(working_dir, tex_filename)

    tex_content = rf"""
\documentclass[border=1mm]{{standalone}}
\usepackage{{tikz-cd}}
\usepackage{{luatexja}}
\usepackage{{xcolor}}
\usepackage{{amsmath}}

{preamble}

\begin{{document}}
\pagecolor{{white}}

{math_code}
\end{{document}}
"""

    with open(tex_filepath, "w", encoding="utf-8") as f:
        f.write(tex_content)

    subprocess.run(
        [
            "lualatex",
            "--interaction=nonstopmode",
            f"--output-directory={working_dir}",
            tex_filepath,
        ],
        capture_output=True,
        check=True,
    )

    pdf_filepath = os.path.join(working_dir, f"{file_hash}.pdf")
    if os.path.exists(pdf_filepath):
        subprocess.run(
            [
                "dvisvgm",
                "--pdf",
                "--font-format=woff2",
                "--zoom=2.2",
                f"--output={svg_path}",
                pdf_filepath,
            ],
            capture_output=True,
            check=True,
        )
    else:
        print(f"Error: PDF compilation failed for {file_hash[:8]}")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--force", action="store_true")

    args = parser.parse_args()

    global force
    force = args.force

    with tempfile.TemporaryDirectory() as tmpdir:
        md_files = glob.glob(f"{CONTENT_DIR}/**/*.md", recursive=True)
        for filepath in md_files:
            process_markdown_file(tmpdir, filepath)

        print("Asset generation complete.")


if __name__ == "__main__":
    main()
