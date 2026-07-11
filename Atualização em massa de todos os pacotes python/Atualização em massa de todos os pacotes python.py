import subprocess
from importlib.metadata import distributions

packages = [dist.metadata['Name'] for dist in distributions()]

for pkg in packages:
    subprocess.run(['pip', 'install', '--upgrade', pkg])
    
"""pip list --outdated --format=json | python -c "import json, sys; from subprocess import call; [call(['pip', 'install', '--upgrade', pkg['name']]) for pkg in json.load(sys.stdin)]"""
