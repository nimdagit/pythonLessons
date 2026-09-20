from pathlib import Path
import subprocess

root = Path(__file__).parent
print(f'SCANNING: {root}')

scanning = [root]

dirs, files = [], []
notscanning = ['venv', '.git', '.env', '__pycache__']
sufs = {}

while scanning:
    current = scanning.pop(0)
    for item in current.iterdir():
        if item.name not in notscanning:
            if item.is_dir():
                dirs.append(item)
                scanning.append(item)
            else:
                files.append(item)
                sufs[item.suffix] = sufs.get(item.suffix, 0) + 1

sort_list = sorted(files, key=lambda item: item.stat().st_size)

print(f'FOLDERS: {len(dirs)}')
print(f'FILES: {len(files)}')
print(f'FILE TYPES: {sufs}')

for item in sort_list[:-4:-1]:
    print(item, item.stat().st_size)


last_updates = subprocess.run(['git', 'log', '--oneline', '-3'], capture_output=True, text=True)


if last_updates.returncode:
    print(last_updates.stderr)
else:
    print(last_updates.stdout)