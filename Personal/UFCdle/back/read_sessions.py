import os
import pickle

# Define the absolute path to the session directory
session_dir = '/home/adduser/University/Personal/UFCdle/instance/flask_session/'

# Check if the session directory exists
if not os.path.exists(session_dir):
    print(f"Session directory {session_dir} does not exist.")
else:
    # Read and print session files
    for filename in os.listdir(session_dir):
        filepath = os.path.join(session_dir, filename)
        try:
            with open(filepath, 'rb') as f:
                session_data = pickle.load(f)
                print(f"Session data for {filename}: {session_data}")
        except pickle.UnpicklingError:
            print(f"Error reading {filename}: Not a valid pickle file")
        except Exception as e:
            print(f"Error reading {filename}: {e}")
