import os
import pickle

session_dir = '../instance/flask_session/'

# Read and print session files
for filename in os.listdir(session_dir):
    with open(os.path.join(session_dir, filename), 'rb') as f:
        session_data = pickle.load(f)
        print(session_data)
