"""
__author__ = "Ashwinkumar Ajithkumar Pillai"
__date__ = 04/10/24
__version__ = "1.0"
__license__ = "MIT style license file"
"""
import os

def create_required_folders()->None:
    folder_list = ["input_files", "input_json", "output_files/section_data", "assignment_output_files"]

    for folder_path in folder_list:
        os.makedirs(folder_path, exist_ok=True)