import os
import json

dir = os.path.join(os.path.dirname(__file__), '2025-07-08-09-05')

files = os.listdir(dir)

for file in files:
    if file.endswith('.json'):
        # if int(file.split('.')[0]) < 7:
        #     continue
        with open(os.path.join(dir, file), 'r') as f:
            data = json.load(f)
        data["manual"]["checks"] = []

        with open(os.path.join(dir, file), 'w') as f:
            json.dump(data, f, indent=2)