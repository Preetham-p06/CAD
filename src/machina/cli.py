"""Minimal entry point; no corpus processing is implemented."""
import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Machina CAD De-ID development scaffold. Processing is not implemented."
    )
    parser.add_argument("--version", action="version", version="machina-deid 0.0.1")
    parser.parse_args()
    parser.print_help()
