from jpconjugation.parsing.load import load_json_file

if __name__ == "__main__":
    # Get and parse json data
    try:
        json_data = load_json_file("./data/data.json")
    except Exception as e:
        print(f"Error : {e}")
    else:
        print("Data loaded")