from __future__ import print_function

import json
import os
import sys
from jinja2 import Environment, FileSystemLoader

def render(template_path, context):
    path, filename = os.path.split(template_path)
    loader = FileSystemLoader(path or './')

    return (Environment(loader=loader)
            .get_template(filename)
            .render(context))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: %s <path to template> [<JSON string of data>]' % sys.argv[0])
        sys.exit()

    f = sys.argv[1]
    data = json.loads(sys.argv[2]) if len(sys.argv) >= 3 else {}
    print(render(f, data))
