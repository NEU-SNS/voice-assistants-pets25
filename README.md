# Artifact Appendix

Paper title: **Echoes of Privacy: Uncovering the Profiling Practices of Voice Assistants**

Artifacts HotCRP Id: **#Enter your HotCRP Id here** (not your paper Id, but the artifacts id)

Requested Badge: Either **Available**, **Functional**, or **Reproduced**

## Description

This artifact includes automation scripts for conducting voice and web experiments with voice assistants and Google searches. It contains sample queries for both types of experiments.

- **Voice Experiments:** The `voiceassistantscript.py` script plays recorded audio queries one after another, with a one-minute delay between each playback. This delay gives the voice assistant time to finish responding to the previous query before starting the next one.

- **Web Experiments:** The `seleniumscript.py` script automates Google search experiments. By entering queries and login credentials in the code, the script logs into a Google account and submits each query automatically. This allows us to observe how these queries may influence user profiling over time.

These scripts provide a way to run and observe interactions with both voice and web interfaces in an automated fashion.

There are also two folders `Amazon Queries` and `Google Queries` containing the queries we used in our experiments for Amazon and Google and Siri. (We used the same Google queries for Siri as discussed in the paper).


### Security/Privacy Issues and Ethical Concerns (All badges)
- **Account Credentials:** Since the `seleniumscript.py` script requires reviewers to enter their Google login credentials, there is a risk associated with storing and processing these credentials. Reviewers should use a test account rather than a personal or sensitive account to avoid unintended data exposure. Additionally, please ensure that credentials are not stored in code files or shared inadvertently.
- **Intended Use:** The artifact should only be used for research and review purposes as intended by the submission guidelines. The automation scripts are not intended for any malicious or unauthorized use.

## Basic Requirements (Only for Functional and Reproduced badges)

### Hardware Requirements
If your artifact requires specific hardware to be executed, mention that here.
Provide instructions on how a reviewer can gain access to that hardware through remote access, buying or renting, or even emulating the hardware.
Make sure to preserve the anonymity of the reviewer at any time.

### Software Requirements
The artifact is tested on the following software:
- **Operating System:** Ubuntu 20.04 (recommended), also other Linux distributions should work. The code should also work on Windows and macOS with minor adjustments.
- **Python Version:** 3.8 or higher

- Additional Software:
   -**ffmpeg:** Required for audio playback with ffplay in play_audio_files() script.
   -**Google Chrome:** For Selenium-based web interactions. Install the latest stable version.
   -**Chromedriver:** Compatible version with Chrome. This will be handled by SeleniumBase.
   -**Third-party Python packages:** Managed via pip in requirements.txt.

### Estimated Time and Storage Consumption
- Compute Time: Running each script individually should take a few minutes. However, the Audio file execution time depends on the audio files that are needed to be played.
- Storage Consumption: Approximately 250–400 MB, including Python dependencies, Chrome installation, and any temporary logs or files generated during script execution.
  
## Environment 

### Accessibility (All badges)
This artifact is accessible through a Git repository. To ensure a persistent and accessible version of the artifact, please use the following repository link and commit ID for evaluation:
```bash
Repository URL: https://github.com/elaineezhu/PETS2025.git
Commit ID: XXXXXXX
```


### Set up the environment (Only for Functional and Reproduced badges)
1. Clone the repository.
   
```bash
git clone https://github.com/elaineezhu/PETS2025.git
cd PETS2025
```

2. Install Dependencies:

To set up dependencies on a host system:
- Install ffmpeg (for audio playback):
  
```bash
sudo apt update
sudo apt install -y ffmpeg
```
- Install Chrome and Chromedriver: Follow instructions at https://www.google.com/chrome/ to install the latest version.
- Python Dependencies:

```bash
pip install -r requirements.txt
```

### Testing the Environment (Only for Functional and Reproduced badges)

1. **Verify Chrome Installation:** Run the following to confirm Chrome is installed correctly.

```bash
google-chrome --version
```

2. **TestAudio Playback:** To verify `ffmpeg` functionality, run:

```bash
ffplay -nodisp -autoexit path/to/sample_audio.m4a
```

Each test ensures that Chrome, Selenium, and audio playback (using `ffmpeg`) are correctly set up and that the scripts can function as intended.

## Artifact Evaluation (Only for Functional and Reproduced badges)
This section outlines the necessary steps to evaluate the artifact’s functionality and validate the key results and claims presented in the paper. The following sections highlight the main results and claims supported by the artifact, along with instructions for running the relevant experiments.

### Main Results and Claims

#### Main Result 1: Automating the voice interactions using sequential queries
This artifact supports Section 4.1 of the paper claiming that we developed an automated Python script to systematically
play back these recordings.

#### Main Result 2: Automating the Web Modality Interaction
This artifact automates the web modality interaction experiment (Section 4.3.5) for each account.

### Experiments 

This section outlines the experiments to evaluate the artifact's functionality and validate the automation process mentioned in the paper.
Each experiment provides:
- **Execution Steps:** Detailed instructions to guide the reviewer through running the experiment.
- **Expected Results:** Specific outcomes to verify successful execution.
- **Time and Storage Requirements:** Estimated duration and storage needs for each experiment.
- **Supporting Claims and Results:** A summary of the claim each experiment supports, demonstrating how the artifact fulfills its intended functionality.

#### Experiment 1: Audio Playback Automation
This experiment validates the automation of sequential audio playback. Expected results include successful playback of each audio file in the specified order, with a delay of 1 minute between files.
**Execution Steps:**
1. Set the `directory-path` variable to the folder containing `.m4a' files for testing.
2. Run the script using the following command.

```bash
python voiceassistantscript.py
```
3. The audio files should start being played in sequence.

**Expected Results:**
- Console logs confirming playback of each file in the specified order.
- Each file plays successfully, with a 1-minute delay between each playback.
  
**Time and Storage Requirements:**
- Estimated time: Depends on the number of audio files; each file has a 1-minute delay after playback.
- Disk space: Minimal, limited to log outputs.

**Supporting Claims and Results:**
This experiment demonstrates the artifact's ability to:
- Automate the sequential playback of audio files without manual intervention.



#### Experiment 2: Gmail Login and Google Search Automation with Selenium

This experiment tests the ability of the Selenium script to:

1. Log into a Gmail account automatically.
2. Navigate to Google and perform a series of search queries.
3. Verify the artifact's automation capabilities for both login and search functionality.

**Execution Steps:**
1. Open the provided Selenium script `seleniumscript.py`.
2. Replace `"USERNAME"` with your actual Gmail username and `"PASSWORD"` with your Gmail password:

```bash
mail_address = "your-email"  # If your email address is your_email@gmail.com
password = "your-password"             # Replace with your actual password

```

3. Update the `questions` list with your search queries:

```bash
questions = ["Query 1", "Query 2", "Query 3"]
```

4. Execute the script using the following command:

```bash
python seleniumscript.py
```

**Expected Results:**
- The script should open Gmail's login page, enter your credentials, and successfully log into your Gmail account.
- After logging in, it should redirect to Google’s homepage.
- The script will then automatically search each query in the `questions` list, one at a time, using Google’s search bar.
- For each search query, the script waits for the search input element to be available, enters the query, and submits it.

**Time and Storage Requirements:**
- **Time:** The script should take approximately 5 minutes to complete, depending on network speed.
- **Storage:** Minimal, as no files are saved; only temporary logs may be generated.

**Supporting Claims and Results:**
This experiment demonstrates the artifact's ability to:

- Automate login functionality for web applications.
- Handle multiple search queries sequentially.


