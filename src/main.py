from parsing.load import load_json_file

if __name__ == "__main__":
    # Get json data
    json_data = load_json_file("./data/data.json")

    print("Data loaded")