# Daily Commit Python Script

This Python script automates the process of making daily commits to a Git repository. It appends the current date to a `README.md` file, creates a commit with a randomly generated message, and pushes the changes to a remote repository.

## Prerequisites

Before running the script, ensure you have the following installed:

- **Python 3.x**: The script requires Python 3.
- **GitPython**: A Python library used to interact with Git repositories.

You can install GitPython using pip:

```bash
pip install gitpython
```

## Configuration

1. **Create a Configuration File**

   Copy the provided `config.template.json` file to `config.json`:

     ```bash
     cp config.template.json config.json
     ```

2. **Edit the Configuration File**

   Open `config.json` in a text editor and modify the fields as needed:

   ```json
   {
       "repo_path": "/path/to/your/repository",
       "readme_path": "README.md",
       "commit_prefix": "Daily update :"
   }
   ```

   - `repo_path`: The path to your Git repository on your local machine.
   - `readme_path`: The path to the `README.md` file within your repository.
   - `commit_prefix`: A prefix for your commit message.

## Script Overview

The script performs the following actions:

1. **Load Configuration**: Reads the `config.json` file to get repository details.
2. **Generate Commit Message**: Chooses a random animal and gemstone to include in the commit message.
3. **Append to README.md**: Adds the current date and time to the `README.md` file.
4. **Create Commit**: Stages the changes and creates a commit with a message.
5. **Push Changes**: Pushes the commit to the remote repository.

## Usage

1. **Clone the Repository** (if you haven’t already):

     ```bash
     git clone https://github.com/Warckoooooo/daily-commit-python.git
     ```

2. **Navigate to the Script Directory**:

     ```bash
     cd daily-commit-python
     ```

3. **Run the Script**:
4. 
     ```bash
     python3 main.py
     ```

   The script will automatically make a commit and push it to the remote repository based on the configuration provided.

## Setting Up a Scheduled Task or Cron Job

### Windows

To automate the execution of the script daily on Windows, you can use Task Scheduler.

1. **Open Task Scheduler**

   Search for "Task Scheduler" in the Start menu and open it.

2. **Create a Basic Task**

   - Click on "Create Basic Task" in the Actions pane.
   - Provide a name and description for your task.
   - Choose "Daily" for the trigger and set the desired time.
   - Select "Start a program" and browse to the Python executable (`python.exe`), typically located at `C:\PythonXX\python.exe`.
   - In the "Add arguments" field, enter the full path to your script, for example: `"C:\path\to\daily-commit-python\main.py"`.
   - Finish the setup and ensure the task is enabled.

3. **Verify the Task**

   Make sure the task is listed and enabled in Task Scheduler. You can run it manually to test if it works correctly.

### Linux

To automate the execution of the script daily on Linux, you can set up a cron job.

1. **Open the Crontab Configuration**

   Edit your crontab file using the following command:

   ```bash
   crontab -e
   ```

2. **Add a Cron Job Entry**

   Add the following line to schedule the script to run daily at a specific time (e.g., 2:00 AM):

   ```bash
   0 2 * * * /usr/bin/python3 /path/to/daily-commit-python/main.py >> /path/to/daily-commit-python/cron.log 2>&1
   ```

   - Replace `/path/to/daily-commit-python/main.py` with the full path to your `main.py` script.
   - The `>> /path/to/daily-commit-python/cron.log 2>&1` part redirects the script’s output and errors to a log file (`cron.log`), which you can check for troubleshooting.

3. **Save and Exit**

   Save the changes and exit the editor. The cron job is now scheduled to run daily at the specified time.

## Troubleshooting

- **Authentication Issues**: Ensure you have set up the remote URL with the correct credentials or token. Refer to GitHub's documentation on Personal Access Tokens (PAT) for more details.
- **File Paths**: Verify that the `repo_path` and `readme_path` in `config.json` are correct and point to the appropriate locations.
- **Dependencies**: Make sure all required Python libraries are installed.
- **Scheduled Task / Cron Job Issues**: Check the respective logs (`cron.log` for Linux, Task Scheduler history for Windows) for any errors or messages.

## Contributing

If you have suggestions or improvements for the script, feel free to submit a pull request or open an issue.
