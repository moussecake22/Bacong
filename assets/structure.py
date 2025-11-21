import os
import json

# Load JSON
with open("/home/cidee/Bacong/assets/Bacong.json", "r") as f:
    data = json.load(f)

# Function to create folders and empty files
def create_structure(items):
    for item in items:
        file_path = item.get("file")
        if file_path:
            folder = os.path.dirname(file_path)
            os.makedirs(folder, exist_ok=True)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write("")  # empty placeholder

# Create folders/files for all sections
create_structure(data.get("prelim_hoa", []))
create_structure(data.get("midterm_hoa", []))
create_structure(data.get("final_hoa", []))
create_structure(data.get("examinations", []))
create_structure([data.get("reflection")])

print("Folder structure for Bacong created successfully!")
