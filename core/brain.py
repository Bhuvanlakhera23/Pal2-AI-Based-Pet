#***************************************************************************************************************************************
#                       BRAIN MODULE WITHOUT WATCHDOG (DOESNT UPDATE AIML FILES WITHOUT MAIN.PY RESTART)

# from core.aiml_loader import AIMLLoader

# class AIMLBrain:
#     def __init__(self):
#         # Initialize AIMLLoader to handle loading AIML files
#         self.loader = AIMLLoader()
#         self.loader.load_aiml_files()

#     def get_response(self, user_input):
#         """Get response from AIML loader."""
#         return self.loader.get_response(user_input)

#***************************************************************************************************************************************
#                      BRAIN MODULE WITH WATCHDOG (UPDATES AIML FILES WITHOUT REQUIRIG MAIN.PY RESTART)

import aiml
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class AIMLLoader:
    def __init__(self):
        self.kernel = aiml.Kernel()
        self.load_aiml_files()  # Load initially
        self.start_file_watcher()  # Start watching for file changes

    def load_aiml_files(self):
        """Load AIML files for the AI."""
        # Delete the brain file if it exists to force reload of AIML files
        if os.path.exists("brain.brn"):
            os.remove("brain.brn")
            print("Old brain file removed. Creating a new one...")

        print("Brain not found, bootstrapping...")
        self.kernel.bootstrap(learnFiles="aiml_data/std-startup.xml", commands="LOAD AIML B")
        
        # Load custom AIML files
        print("Loading custom AIML files...")
        self.kernel.learn("aiml_data/greetings.aiml")  # Your custom AIML files go here
        self.kernel.learn("aiml_data/identity.aiml")  # Add other AIML files similarly
        
        # Save the brain
        self.kernel.saveBrain("brain.brn")
        print("Brain saved to brain.brn.")

    def get_response(self, user_input):
        """Get response from the AIML kernel."""
        response = self.kernel.respond(user_input)
        return response

    def start_file_watcher(self):
        """Start monitoring the AIML files folder for changes."""
        event_handler = AIMLFileChangeHandler(self)
        observer = Observer()
        observer.schedule(event_handler, path='aiml_data', recursive=False)
        observer.start()
        print("Watching for AIML file changes...")

        # Keep the watcher running in the background
        self._watcher_thread = observer

class AIMLFileChangeHandler(FileSystemEventHandler):
    def __init__(self, aiml_loader):
        self.aiml_loader = aiml_loader

    def on_modified(self, event):
        if event.src_path.endswith(".aiml"):
            print(f"AIML file changed: {event.src_path}. Reloading...")
            self.aiml_loader.load_aiml_files()

# Ensure the watcher stops on exit
def stop_watcher(loader):
    print("Stopping AIML file watcher.")
    if hasattr(loader, '_watcher_thread'):
        loader._watcher_thread.stop()
        loader._watcher_thread.join()