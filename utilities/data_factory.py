import json
import config


class DataRead:

    def json_read(self, file_name):
        with open(config.project_root + file_name) as f:
            data_file = json.loads(f.read())

        return data_file