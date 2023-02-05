class Config:
    # All fire
    wildfire_all_prefix = "wildfire_all_"

    # Big fire
    wildfire_filtered_prefix = "wildfire_filtered_"

    # Meterology
    meteorology_prefix = "meteorology_"
    # Raw Fire All Section
    def get_raw_fire_all_path(this, file_name):
        raw_path = "../../data/raw/"
        return raw_path + this.wildfire_all_prefix + file_name + ".csv"

    def get_cleaned_fire_all_path(this, file_name):
        cleaned_path = "../../data/cleaned/"
        return cleaned_path + this.wildfire_all_prefix + file_name + ".csv"

    def get_processed_fire_all_path(this, file_name):
        processed_path = "../../data/processed/"
        return processed_path + this.wildfire_all_prefix + file_name + ".csv"

    # Raw Fire Filtered Section
    def get_raw_fire_filtered_path(this, file_name):
        raw_path = "../../data/raw/"
        return raw_path + this.wildfire_filtered_prefix + file_name + ".csv"

    def get_cleaned_fire_filtered_path(this, file_name):
        cleaned_path = "../../data/cleaned/"
        return cleaned_path + this.wildfire_filtered_prefix + file_name + ".csv"

    def get_processed_fire_filtered_path(this, file_name):
        processed_path = "../../data/processed/"
        return processed_path + this.wildfire_filtered_prefix + file_name + ".csv"

    # Raw Fire Filtered Section
    def get_raw_meteorology_path(this, file_name):
        raw_path = "../../data/raw/"
        return raw_path + this.meteorology_prefix + file_name + ".csv"

    def get_cleaned_meteorology_path(this, file_name):
        cleaned_path = "../../data/cleaned/"
        return cleaned_path + this.meteorology_prefix + file_name + ".csv"

    def get_processed_meteorology_path(this, file_name):
        processed_path = "../../data/processed/"
        return processed_path + this.meteorology_prefix + file_name + ".csv"
