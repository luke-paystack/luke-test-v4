import os
import sys
import subprocess

REMOVE_PATHS = [
    '',
    ' src/loaders/kafkaLoader.ts ',
    ' src/utils/test/e2e/kafkaLoader.ts ',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)

# Format using prettier
subprocess.run(["npx", "prettier", "--write", "."])
