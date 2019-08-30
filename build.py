import json
from pathlib import Path

from skua.files import FindFilesByExtension
from skua.render import Templates

templates = Templates(Path('src/templates'), template_prefix='dict_')
file_finder = FindFilesByExtension(extension='json')
for file in file_finder():
    json_file = json.load(file.open())
    for (key, value) in json_file.items():
        word: str = value['word']
        word = word.replace('#', 'hash')
        word = word.replace('?', 'question-mark')
        word = word.replace('/', '')
        word = word.replace(' ', '-')
        save_location = 'build/' + word + '.json'
        json.dump(value, open(save_location, 'w+'))
"""
output = templates.render_template('dict_entry', **value)
output = htmlmin.minify(output)
word: str = value['word']
word = word.replace('#', 'hash')
word = word.replace('?', 'question-mark')
word = word.replace('/', '')
word = word.replace(' ', '-')
save_location = calculate_save_location(Path('src/' + word), Path('src'), Path('build'))
save_location.write_text(output)
"""
