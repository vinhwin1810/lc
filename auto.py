import os
import random
import subprocess
import schedule
import time

# Define the function that will be run every 3 hours
def job():
    folder_path = os.path.expanduser(r"C:\Users\Vinh\Desktop\lc")  # Use raw string literal for Windows paths

    # Full path to VS Code executable
    vscode_path = r"C:\Users\Vinh\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd"

    # Open VS Code in the desired folder
    try:
        # Use 'cwd' to change directory and run 'code .' in that directory
        subprocess.run([vscode_path, "."], check=True, cwd=folder_path)
        print("VS Code opened successfully.")
    except FileNotFoundError:
        print("Error: 'code' command not found. Ensure that VS Code CLI is installed and added to PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error opening VS Code: {e}")

    # Modify a specific file
    specific_file_path = os.path.join(folder_path, "decode.py")  # Replace with your specific file name
    modify_specific_file(specific_file_path)

    # Perform Git operations
    git_operations(folder_path)

# Function to modify a specific file
def modify_specific_file(file_path):
    try:
        # Read the content of the specific file
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Choose a random line to modify
        if lines:
            random_line = random.randint(0, len(lines) - 1)
            lines[random_line] = "# Modified by script\n"  # Example modification

            # Write the modified content back to the file
            with open(file_path, "w") as file:
                file.writelines(lines)
            print(f"Modified line {random_line + 1} in {file_path}")
        else:
            print(f"No content in {file_path} to modify.")
    except Exception as e:
        print(f"Error modifying file {file_path}: {e}")

# Function to perform Git add, commit, and push operations
def git_operations(folder_path):
    try:
        subprocess.run(["git", "add", "."], check=True, cwd=folder_path)
        subprocess.run(["git", "commit", "-m", "Automated commit"], check=True, cwd=folder_path)
        subprocess.run(["git", "push"], check=True, cwd=folder_path)
        print("Git operations completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during git operations: {e}")

# Schedule the job to run every 3 hours
schedule.every(2).seconds.do(job)

# Keep the script running and executing the job as scheduled
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for 60 seconds before checking again
