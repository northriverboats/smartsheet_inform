#!/usr/bin/env python3
"""
download INFORM report and save based on date

pyinstaller --onefile smartsheet.spec smartsheet_inform.py

"""
import smartsheet
import os
import time
from dotenv import load_dotenv

@click.command()
def cli():
    _ = load_dotenv()


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
