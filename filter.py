import json

input_file_path = 'results.json'
output_file_path = 'output.json'

try:
    with open(input_file_path, 'r') as file:
        data = json.load(file)
        
        extracted_data = []
        documents = data["resultset"]["documents"]
        
        for doc in documents:
            title = doc["fields"].get("_str.title", ["No Title Found"])[0]
            url = doc["fields"].get("_str.url", ["No URL Found"])[0]
            extracted_data.append({"_str.title": title, "_str.url": url})
        
        with open(output_file_path, 'w') as output_file:
            json.dump(extracted_data, output_file, indent=4)
            
        print(f"Extracted data saved to {output_file_path}")
except FileNotFoundError:
    print(f"File {input_file_path} not found.")
except json.JSONDecodeError:
    print("Error decoding JSON from the input file.")
except KeyError:
    print("The specified key was not found in the JSON structure.")
