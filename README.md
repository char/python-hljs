# python-hljs

An ugly hack to use highlight.js from Python using a node.js worker process.

**Note:** Requires `node` to be in the `PATH` at runtime.

## Setup

1. Clone the repo
2. `npm install` (or yarn!)
3. Import `hljs.py` as usual

## Usage

```python3
from hljs import Highlighter

SOURCE_CODE = '''print("Hello, world!")'''

with Highlighter() as h:
  print(h.highlight(SOURCE_CODE, "python"))

# print(<span class="hljs-string">"Hello, world!"</span>)
```
