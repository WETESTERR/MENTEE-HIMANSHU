import json
import config


class DataRead:

    @classmethod
    def json_read(cls,file_name):
        with open(config.test_data_path +'\\'+ file_name) as f:
            data_file = json.loads(f.read())

        return data_file