import os
import subprocess
import time

def play_audio_files(directory):
    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Sort the files to play them in order
    files.sort()
    
    for file in files:
        if file.lower().endswith(('.m4a')):
            file_path = os.path.join(directory, file)
            print(f"Playing: {file}")
                
            # Use subprocess to call an external player
            subprocess.run(["ffplay", "-nodisp", "-autoexit", os.path.join(directory, "wakeword.m4a")])
            subprocess.run(["ffplay", "-nodisp", "-autoexit", file_path])

            # Add a delay of 1 minute
            time.sleep(60)   
        

if __name__ == "__main__":
    # Get the directory path from the user
    directory_path = "Audio_Files"

    # Check if the directory exists
    if os.path.exists(directory_path):
        play_audio_files(directory_path)
    else:
        print("Directory not found. Please enter a valid directory path.")
