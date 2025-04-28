PAL2: PHYSICAL AI DESKTOP ASSISTANT

Pal2 is a lightweight AI-powered digital pet that can talk to you via typed or voice interactions!
It uses AIML (Artificial Intelligence Markup Language) for conversation, and supports TTS (Text-to-Speech) for natural voice responses. This version of Pal2 contains the basic fed AIML conversational capabilities, which will be replaced by NLP in future versions. The ultimate goal is to load Pal2 to a physical microcontroller with more capabilities, like Emotion Recognition and improved awareness.

✨ Features
🧠 AIML Brain: Pre-trained conversational responses.

🎤 Voice & Text Mode: Talk by typing or speaking.

🗣️ Natural Voice Responses: Powered by Coqui TTS (Jenny Model).

🔄 Hot Reload: AIML files update without restarting.

🖥️ Lightweight: TTS runs without a GPU; use a GPU for faster responses.

🚀 Setup
1) Clone the repo:
    git clone https://github.com/Bhuvanlakhera23/Pal2-AI-Based-Pet.git
    cd Pal2-AI-Based-Pet

2) Create a virtual environment:
    python -m venv venv-gpu

3) Activate the environment:
    Windows:
    venv-gpu\Scripts\activate

    Linux/Mac:
    source venv-gpu/bin/activate

4) Install requirements:
    pip install -r requirements.txt

5) Run Pal2:
    python main.py

NOTE: 
Hot Reload Notes
- On first run, `brain.brn` will be auto-generated from AIML files.
- Delete this file to force a full AIML reload.
    

🛠️ Project Structure
PAL2/
├── aiml_data/          # AIML knowledge base
├── config/             # Settings files
├── core/               # Main program logic
├── brain.brn           # Saved AIML brain cache
├── coqui_tts.py        # TTS Integration
├── main.py             # Program Entry Point
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── .gitignore          # Files to ignore

📚 Technologies Used
Python 3.11+
AIML (python-aiml)
Coqui TTS
SpeechRecognition
Pyttsx3 (fallback if no GPU)
Watchdog (Allows instant changes in AIML responses without restarting Main.py)

🎯 Future Plans
Add emotion responses.
Movement animations (After connecting to the hardware).
Smarter NLP with intent detection.

🤝 Contributions
PRs are welcome. Feel free to fork.

📜 License
This project is open-source and available under the MIT License.
