# ******************************************************************************************************************************

#                               AIML LOADER MODULE (LOADS AIML FILES AND CREATES BRAIN FILE)

# import aiml
# import os

# class AIMLLoader:
#     def __init__(self):
#         self.kernel = aiml.Kernel()

#     def load_aiml_files(self):
#         """Load AIML files for the AI."""
#         # Delete the brain file if it exists to force reload of AIML files
#         if os.path.exists("brain.brn"):
#             os.remove("brain.brn")
#             print("Old brain file removed. Creating a new one...")

#         print("Brain not found, bootstrapping...")
#         self.kernel.bootstrap(learnFiles="aiml_data/std-startup.xml", commands="LOAD AIML B")
        
#         # No need to manually learn individual AIML files here now.

#         # Save the brain
#         self.kernel.saveBrain("brain.brn")
#         print("Brain saved to brain.brn.")

#     def get_response(self, user_input):
#         """Get response from the AIML kernel."""
#         response = self.kernel.respond(user_input)
#         return response
    
# ******************************************************************************************************************************

#                  LOADS THE AIML FILES WITH WATCHDOG (UPDATES AIML FILES WITHOUT REQUIRING MAIN.PY RESTART)

import aiml
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class AIMLLoader:
    def __init__(self):
        self.kernel = aiml.Kernel()
        self.load_aiml_files()  # Initial load of AIML files
        self.start_file_watcher()  # Start watching for file changes

    def load_aiml_files(self):
        """Load AIML files for the AI."""
        # Delete the brain file if it exists to force reload of AIML files
        if os.path.exists("brain.brn"):
            os.remove("brain.brn")
            print("Old brain file removed. Creating a new one...")

        print("Brain not found, bootstrapping...")
        self.kernel.bootstrap(learnFiles="aiml_data/std-startup.xml", commands="LOAD AIML B")
        
        # Load AIML files dynamically
        print("Loading AIML files...")
        self.kernel.learn("aiml_data/greetings.aiml")  # Add more AIML files here as needed
        
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
        """Reload the AIML files if any file changes."""
        if event.src_path.endswith(".aiml"):
            print(f"AIML file changed: {event.src_path}. Reloading...")
            self.aiml_loader.load_aiml_files()

# Ensure the watcher stops on exit
def stop_watcher(loader):
    """Stop the AIML file watcher gracefully."""
    print("Stopping AIML file watcher.")
    if hasattr(loader, '_watcher_thread'):
        loader._watcher_thread.stop()
        loader._watcher_thread.join()


