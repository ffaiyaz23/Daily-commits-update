import os
import datetime
import json
import random
from git import Repo

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

repo_path = config['repo_path']
readme_path = os.path.join(repo_path, config['readme_path'])
commit_prefix = config['commit_prefix']

# List of animals for the commit message
animals = ["Lion", "Tiger", "Bear", "Fox", "Deer", "Wolf", "Monkey", "Zebra", "Elephant", "Giraffe", "Shark"]

# List of gemstones for the commit message
gemstones = ["Diamond", "Ruby", "Sapphire", "Emerald", "Opal", "Amethyst", "Topaz", "Garnet", "Jade", "Pearl"]

# Generate a random animal name and gemstone
random_animal = random.choice(animals)
random_gemstone = random.choice(gemstones)

# Open the repository
repo = Repo(repo_path)

# Append the current date to README.md
with open(readme_path, 'a') as readme_file:
    readme_file.write(f'\nUpdate on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

# Add README.md to the index
repo.index.add([readme_path])

# Create a commit
commit_message = f'{commit_prefix} {random_gemstone} {random_animal}'
repo.index.commit(commit_message)

# Push the changes to the remote repository
origin = repo.remote(name='origin')
origin.push()
