import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    # Raw Fire All Section
    def get_raw_fire_all_path(file_name):
        raw_path = "../../data/raw/"
        return raw_path + os.getenv("wildfire_all_prefix") + file_name + ".csv"

    def get_cleaned_fire_all_path(file_name):
        cleaned_path = "../../data/cleaned/"
        return cleaned_path + os.getenv("wildfire_all_prefix") + file_name + ".csv"

    def get_processed_fire_all_path(file_name):
        processed_path = "../../data/processed/"
        return processed_path + os.getenv("wildfire_all_prefix") + file_name + ".csv"

    # Raw Fire Filtered Section
    def get_raw_fire_filtered_path(file_name):
        raw_path = "../../data/raw/"
        return raw_path + os.getenv("wildfire_filtered_prefix") + file_name + ".csv"

    def get_cleaned_fire_filtered_path(file_name):
        cleaned_path = "../../data/cleaned/"
        return cleaned_path + os.getenv("wildfire_filtered_prefix") + file_name + ".csv"

    def get_processed_fire_filtered_path(file_name):
        processed_path = "../../data/processed/"
        return (
            processed_path + os.getenv("wildfire_filtered_prefix") + file_name + ".csv"
        )

    # Raw Fire Filtered Section
    def get_raw_meteorology_path(file_name):
        raw_path = "../../data/raw/"
        return raw_path + os.getenv("meteorology_prefix") + file_name + ".csv"

    def get_cleaned_meteorology_path(file_name):
        cleaned_path = "../../data/cleaned/"
        return cleaned_path + os.getenv("meteorology_prefix") + file_name + ".csv"

    def get_processed_meteorology_path(file_name):
        processed_path = "../../data/processed/"
        return processed_path + os.getenv("meteorology_prefix") + file_name + ".csv"
