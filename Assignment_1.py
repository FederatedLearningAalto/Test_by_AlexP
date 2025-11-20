import sys
import subprocess
from pathlib import Path

def ensure_requirements():
    req_file = Path(__file__).with_name("requirements.txt")
    if req_file.exists():
        # This is equivalent to: pip install -r requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req_file)])
    else:
        print("requirements.txt not found, skipping dependency install")

# Install requirements before importing packages that depend on them
ensure_requirements()

import pandas as pd
# ... rest of your imports and code ...

data = {
    "student": ["Alice", "Bob", "Charlie", "Diana"],
    "exam_1": [78, 92, 85, 60],
    "exam_2": [88, 75, 90, 70],
}

df = pd.DataFrame(data)

exam_1_mean = data.exam_1.mean()

print(exam_1_mean)