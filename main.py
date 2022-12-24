import filedate
import os
import json
import time
from datetime import datetime

def main():
    # Get the folder where the the files are.
    main_directory = input("Where is the folder where the extracted photos reside?")
    delete_json = input("Would you like to delete the json files after merging the dates ( they're not needed once we merge the dates ) [ y/n ]")

    if delete_json == "y":
        delete_json = 1
    else:
        delete_json = 0

    iterate_through_files(main_directory, delete_json)


def iterate_through_files(directory, delete_json):
    for filename in os.listdir(directory):
        complete_path = os.path.join(directory, filename)

        if os.path.isdir(complete_path):
            iterate_through_files(complete_path)

        if ".json" in filename:
            continue

        json_path = complete_path + ".json"

        # Check if the .json of the file exists in the first place.
        if not os.path.exists(json_path):
            continue

        print(complete_path)
        
        with open(json_path, "r", encoding="utf8") as json_file:
            json_object = json.loads(json_file.read())
        
        if delete_json:
            os.remove(json_path)
        
        creation_time = datetime.fromtimestamp(int(json_object["photoTakenTime"]["timestamp"]))
        modified_time = datetime.fromtimestamp(int(json_object["photoLastModifiedTime"]["timestamp"]))

        print("--Creation time: " + str(creation_time))
        print("--Modified time: " + str(modified_time))
        print("\n")

        test = filedate.File(complete_path)

        test.set(
            created = creation_time,
            modified = modified_time
        )


if __name__ == '__main__':
    main()