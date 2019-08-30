import json
from pathlib import Path

from skua.files import FindFilesByExtension, calculate_save_location
from skua.render import Templates

templates = Templates(Path('src/templates'), template_prefix='dict_')

file_finder = FindFilesByExtension(extension='json')
for file in file_finder():
    json_file = json.load(file.open())
    for (key, value) in json_file.items():
        output = templates.render_template('dict_entry', **value)
        save_location = calculate_save_location(Path('src/' + value['word']), Path('src'), Path('build'))
        save_location.open(mode='w+')
        save_location.write_text(output)
