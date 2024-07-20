
import os.path
from pathlib import Path


def get_personal_env_path():
    main_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    if os.path.exists(os.path.join(main_path, '.env.personal_data.private')):
        return os.path.join(main_path, '.env.personal_data.private')
    else:
        return os.path.join(main_path, '.env.personal_data.example')


def get_app_path(file: str):
    if file.startswith('./'):
        file = file[2:]

    main_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    path_to_file = os.path.join(main_path, f'files/{file}')
    return path_to_file


def get_mobile_env_path(env):
    main_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    path_to_mobile_env = os.path.join(main_path, 'tests', 'mobile', f'.env.mobile.{env}')
    return path_to_mobile_env


def path(file_name):
    base_path = Path(__file__).resolve().parent.parent
    tests_folder_path = base_path / 'tests'
    absolute_file_path = tests_folder_path / file_name
    return str(absolute_file_path.resolve())

def abs_path_from_project(relative_path):

    return (
        Path(__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
