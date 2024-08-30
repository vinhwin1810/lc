import os
import random
import subprocess
import schedule
import time
# Step 1: Define the folder path
# Define the folder path

def job():
    folder_path = os.path.expanduser(r"C:\Users\Vinh\Desktop\lc")  # Use raw string literal for Windows paths

    # Full path to VS Code executable
    vscode_path = r"C:\Users\<YourUsername>\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd"

    # Open VS Code in the desired folder
    try:
        # Use 'cwd' to change directory and run 'code .' in that directory
        subprocess.run([vscode_path, "."], check=True, cwd=folder_path)
        print("VS Code opened successfully.")
    except FileNotFoundError:
        print("Error: 'code' command not found. Ensure that VS Code CLI is installed and added to PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error opening VS Code: {e}")

    # Step 3: Find a random file and modify a random line
    def modify_random_line():
        # Get all code files in the folder (adjust the file type if needed)
        files = []
        for root, dirs, filenames in os.walk(folder_path):
            for filename in filenames:
                if filename.endswith(".py"):  # Replace with your desired file extension
                    files.append(os.path.join(root, filename))

        # Select a random file
        if files:
            random_file = random.choice(files)

            # Read the content of the file
            with open(random_file, "r") as file:
                lines = file.readlines()

            # Choose a random line to modify
            if lines:
                random_line = random.randint(0, len(lines) - 1)
                lines[random_line] = "// Modified by script\n"  # Example modification

                # Write the modified content back to the file
                with open(random_file, "w") as file:
                    file.writelines(lines)
                print(f"Modified line {random_line + 1} in {random_file}")
            else:
                print(f"No content in {random_file} to modify.")
        else:
            print("No files found to modify.")

    # Step 4: Git add, commit, and push
    def git_operations():
        try:
            subprocess.run(["git", "add", "."], check=True, cwd=folder_path)
            subprocess.run(["git", "commit", "-m", "Automated commit"], check=True, cwd=folder_path)
            subprocess.run(["git", "push"], check=True, cwd=folder_path)
            print("Git operations completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error during git operations: {e}")
    if __name__ == "__main__":
        modify_random_line()
        git_operations()
schedule.every(30).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(60)


