"""Placeholder script: converts raw annotations to YOLO format.

Usage:
    python prepare_data.py --src raw_annotations --out data/holds.yaml
"""
import argparse, pathlib, shutil, yaml

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", required=True)
    parser.add_argument("--out", default="data/holds.yaml")
    args = parser.parse_args()

    print("Prepare data placeholder – implement conversion here.")
