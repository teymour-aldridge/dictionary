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
        word: str = value['word']
        word = word.replace('#', 'hash')
        word = word.replace('?', 'question-mark')
        word = word.replace('/', '')
        word = word.replace(' ', '-')
        save_location = calculate_save_location(Path('src/' + word), Path('src'), Path('build'))
        save_location.write_text(output)
