import json

# Load static data from data.json
def load_static_data(file_path="../data.json"):  # Use relative path
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        print("Static data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading static data: {e}")
        return None

# Load scraped data from scraped_data.json
def load_scraped_data(file_path="../scraped_data.json"):  # Use relative path
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        print("Scraped data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading scraped data: {e}")
        return None

if __name__ == "__main__":
    # Load the data
    static_data = load_static_data()
    scraped_data = load_scraped_data()

    # Print a preview of the loaded data (optional)
    print("\nPreview of Static Data:", static_data[:2])  # Display first two items from static data
    print("\nPreview of Scraped Data:", {key: scraped_data[key][:1] for key in scraped_data})  # Display first item of each scraped data section
