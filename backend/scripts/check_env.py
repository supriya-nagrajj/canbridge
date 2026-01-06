import os
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))

print('CWD->', Path.cwd())
print('PYTHON->', os.sys.executable)
try:
    from app.services import guidance_generator as gg
    print('Imported guidance_generator OK')
except Exception as e:
    print('Import error:', repr(e))
print('GROQ_API_KEY->', os.getenv('GROQ_API_KEY'))
