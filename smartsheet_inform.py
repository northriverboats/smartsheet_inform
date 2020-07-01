#!/usr/bin/env python3
"""
download INFORM report and save based on date

pyinstaller --onefile smartsheet.spec smartsheet_inform.py

"""
import smartsheet
import click
import os
import time
from dotenv import load_dotenv


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


@click.command()
def cli():
    env_path = resource_path('.env')
    _ = load_dotenv(dotenv_path=env_path)

    api = os.getenv('SMARTSHEET_API')
    user = os.getenv('SMARTSHEET_USER')
    target_dir = os.getenv('TARGET_DIR')
    file_name = time.strftime(os.getenv('FILE_NAME'))
    report = os.getenv('REPORT')

    smart = smartsheet.Smartsheet(api)
    smart.assume_user(user)
    _ = smart.Reports.get_report_as_excel(report, target_dir, alternate_file_name=file_name)


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
