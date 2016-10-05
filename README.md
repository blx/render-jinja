# render-jinja

Tiny program to render jinja2 templates.

## Installation

- (Optional) Create and activate a fresh virtualenv
- Install jinja by running `pip install -r requirements.txt`

## Usage

Pass the path to the template and optional JSON-formatted object of context data.

```shell
$ python render_jinja.py test-template.html '{"expletive": "dysfunctional", "a": {"b": 3}}'
<h2>there is functional programming and dysfunctional programming</h2>

<p>a.b is small</p>
```

Alternatively, import the `render` function:
```python
from render_jinja import render

output = render('test-template.html', {
    'expletive': 'dysfunctional',
    'a': {'b': 7}
})
```
