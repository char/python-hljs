import subprocess
import json
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

class Highlighter:
  def __init__(self):
    self.worker = subprocess.Popen(
      ["node", "hljs_worker.js"],
      cwd=current_dir,
      stdout=subprocess.PIPE, stdin=subprocess.PIPE,
      encoding='utf-8',
      bufsize=1, universal_newlines=True
    )

  def highlight(self, code, lang):
    request = json.dumps({ "code": code, "language": lang })

    self.worker.stdin.write(request + "\n")
    response = json.loads(self.worker.stdout.readline())

    return response

  def close(self):
    self.worker.terminate()


  def __enter__(self):
    return self
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.close()
