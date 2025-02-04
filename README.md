This project is licensed under the Apache License 2.0 - see the LICENSE file for details.


# Artifact Appendix

Paper title: **Echoes of Privacy: Uncovering the Profiling Practices of Voice Assistants**

Artifacts HotCRP Id: **16**

Requested Badge: **Available**

## Description

This artifact includes automation scripts for conducting voice and web experiments with voice assistants and Google searches, the dataset of queries used in our experiemtns, and the labels gathered from Google's My Ad Center and Amazon's Profile Hub for individual personas evaluated in the paper. It also includes a pre-configured virtual machine (VM) to facilitate the setup and execution of these experiments. The provided VM is configured with all the necessary dependencies and tools for running these scripts.

- **Voice Experiments:** The `voiceassistantscript.py` script plays recorded audio queries one after another, with a one-minute delay between each playback. This delay gives the voice assistant time to finish responding to the previous query before starting the next one.

- **Web Experiments:** The `seleniumscript.py` script automates Google search experiments. By entering queries and login credentials in the code, the script logs into a Google account and submits each query automatically. This allows us to observe how these queries may influence user profiling over time.

These scripts provide a way to run and observe interactions with both voice and web interfaces in an automated fashion.

There are two folders `Amazon Queries` and `Google Queries` containing the queries we used in our experiments for Amazon and Google and Siri (We used the same Google queries for Siri as discussed in the paper). There is also a `Data` folder containing labels gathered from Google's My Ad Center and Amazon's Profile Hub for individual personas that were used to report results in Section 5 of the paper.


### Security/Privacy Issues and Ethical Concerns (All badges)

- **Account Credentials:** Since the `seleniumscript.py` script requires reviewers to enter their Google login credentials, there is a risk associated with storing and processing these credentials. Reviewers should use a test account rather than a personal or sensitive account to avoid unintended data exposure. Additionally, please ensure that credentials are not stored in code files or shared inadvertently.
- **Intended Use:** The artifact should only be used for research and review purposes as intended by the submission guidelines. The automation scripts are not intended for any malicious or unauthorized use.

## Basic Requirements (Only for Functional and Reproduced badges)

This document outlines the hardware and software requirements for executing the artifact, either within the provided Virtual Machine (VM) or on your own system. The VM is pre-configured with all dependencies, simplifying setup for reviewers.



### Hardware Requirements

#### Using the VM:
- **Host System Requirements:**
  - **RAM:** At least 8 GB (6 GB allocated to the VM, 2 GB for the host OS).
  - **CPU:** A multi-core processor with virtualization support (e.g., VT-x/AMD-V enabled).
  - **Storage:** Minimum 20 GB of free disk space to accommodate the VM file and additional data.
  - **Virtualization Software:** VirtualBox (latest version recommended).
  - **Audio Output:** A speaker connected to the computer is necessary for the `voiceassistantscript.py` python file.
  

 - **VM Audio Specifications:**
  - **Host Driver**: Windows DirectSound, configured to use the host system's audio capabilities.
  - **Controller**: ICH AC97, commonly supported and emulated audio controller.


If your system meets the above requirements, simply download and import the pre-configured VM to get started.

#### Without the VM:

If you prefer to run the artifact directly on your host system, ensure the following hardware configurations:

- **Processor:** A multi-core CPU is recommended to handle the computational demands efficiently.
- **RAM:** Minimum of 4 GB required to ensure smooth operation.
- **Storage:** At least 1 GB of free disk space is needed for installation and runtime data.
- **Audio Output:** Ensure that a speaker is connected to the computer for the `voiceassistantscript.py` python file.


### Software Requirements

- The VM is pre-installed with:
  - **Operating System:** Ubuntu 20.04 LTS.
  - **Python Version:** 3.8.10
  - **Additional Software:**
    - `ffmpeg`: (Version 4.2.7-0ubuntu0.1) For audio playback using the `play_audio_files()` script.
    - Google Chrome Version: 131.0.6778.85
    - Chromedriver (managed by SeleniumBase for compatibility). 
    - All required Python packages from `requirements.txt`.

Reviewers can simply boot the VM and navigate to `/home/pets2025/Desktop/voice-assistants-pets25` to access and execute the artifact. For executing artifact on your system, please refer to [This Section](https://github.com/NEU-SNS/voice-assistants-pets25/blob/main/README.md#installing-dependencies-manually-on-your-own-system) for more details on how to install dependencies.


### Estimated Time and Storage Consumption

- **Compute Time:** Running each script individually should take a few minutes. The time required for audio file processing depends on the size and length of the files.
- **Storage Consumption:** The initial download size of the OVA file is approximately 4 GB. Dpeneding on the usecase, the VM's storage can expand up to the maximum allocated size of 14.32 GB as specified in the VM settings.



## Environment 

### Accessibility (All badges)
This artifact is accessible through a Git repository. To ensure a persistent and accessible version of the artifact, please use the following repository link and commit ID for evaluation:
```bash
Repository URL: https://github.com/NEU-SNS/voice-assistants-pets25.git
Commit ID: f278e0f303d2f63e1463beff2241fd264b68e08f
```


### Set up the environment (Only for Functional and Reproduced badges)

### Using the VM with installed dependencies

- **Download and Launch the VM**
  
1. **Download the VM**: Click [This link](https://drive.google.com/file/d/1ObeBIE6YvhY-PZb61gVXBt9ynfu_ZCm8/view?usp=sharing) to download the OVA file for the VM.
2. **Import the OVA into VirtualBox** (or your preferred virtualization software): Open VirtualBox, navigate to `File > Import Appliance`, and follow the prompts to import the downloaded OVA file.
3. **Start the VM**: Once imported, start the VM. When prompted, use the password `123` to log in.

- **Access the Project Files**
Once logged into the VM:
1. Open a terminal window.
2. Navigate to the project directory with the following command:
   
   ```bash
   cd /home/pets2025/Desktop/voice-assistants-pets25
   ```
Now you can run the python codes there. For more instructions on how to run experiments, please refer to [the Experiments Section](https://github.com/NEU-SNS/voice-assistants-pets25/blob/main/README.md#experiments).

   
### Installing Dependencies Manually on your own System

If you prefer to set up the environment on your own system, follow the steps below to clone the repository and install all necessary dependencies:

1. Clone the repository.
   
```bash
git clone https://github.com/NEU-SNS/voice-assistants-pets25.git
cd voice-assistants-pets25
```

2. Install Dependencies:
To set up dependencies manually on a host system:
- Install ffmpeg (for audio playback):
  
```bash
sudo apt update
sudo apt install -y ffmpeg
```
- Install Google Chrome: Follow instructions at https://www.google.com/chrome/ to install version 131.0.6778.85.
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
ffplay -nodisp -autoexit /home/pets2025/Desktop/voice-assistants-pets25/Audio_Files/sample.m4a
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
python3 voiceassistantscript.py
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
python3 seleniumscript.py
```
**Execution Notes:**
- The script requires the user to replace `"USERNAME"` and `"PASSWORD"` with actual Google account credentials. Keeping them as `"USERNAME"` and `"PASSWORD"`, Google will detect the attempt as a bot and prevent login.

- The script does not incorporate stealth mechanisms to bypass detection. In our evaluations across multiple accounts, we did not encounter any reCAPTCHA challenges. However, in case a reCAPTCHA is triggered, manual intervention will be required to proceed with the login steps.


**Expected Results:**
- The script should open Gmail's login page, enter your credentials, and successfully log into your Gmail account.
- After logging in, it should redirect to Google’s homepage.
- The script will then automatically search each query in the `questions` list, one at a time, using Google’s search bar.
- For each search query, the script waits for the search input element to be available, enters the query, and submits it.

**Time and Storage Requirements:**
- **Time:** The script should take approximately 2 minutes to complete, depending on network speed.
- **Storage:** Minimal, as no files are saved.

**Supporting Claims and Results:**
This experiment demonstrates the artifact's ability to:

- Automate login functionality for web applications.
- Handle multiple search queries sequentially.

**Future Works:**

While this experiment focuses on audio playback and Google web search automation, additional meaningful actions to perform with the voice assistant automation such as personalized data retrieval, text-to-voice conversion, and other interactive tasks could be explored in future extensions to enhance its capabilities.
