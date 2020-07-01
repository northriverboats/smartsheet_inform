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

log_text = ''
errors = ''
error_level = 0

def log(text, level, error=None):
    """
    print text to screen and make log to send by email in case of error
    """
    global log_text, error_level, errors

    if level > 0 and level <=  error_level:
        print(text)
        log_text += text + "\n"
    if (error):
        errors = True


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


@click.command()
@click.option('--verbose', '-v', default=0, type=int, help='verbosity level 0-3')
def cli(verbose):
    global error_level
    error_level = verbose
    env_path = resource_path('.env')
    _ = load_dotenv(dotenv_path=env_path)

    api = os.getenv('SMARTSHEET_API')
    user = os.getenv('SMARTSHEET_USER')
    target_dir = os.getenv('TARGET_DIR')
    file_name = time.strftime(os.getenv('FILE_NAME'))
    report = os.getenv('REPORT')

    smart = smartsheet.Smartsheet(api)
    smart.assume_user(user)
    log("Downloading Inform Report", 1)
    _ = smart.Reports.get_report_as_excel(report, target_dir, alternate_file_name=file_name)
    log("Saving as {}/{}".format(target_dir, file_name), 1)


if __name__ == "__main__":
    cli()  # pylint: disable=no-value-for-parameter
