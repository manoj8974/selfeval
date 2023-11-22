import json

# Given string
df = "067 StartCall 1 0 29 0 = AR_ORG=400 Account Balance=-45.32"

# Split the string into words
words = df.split()
print(words)
# Create an empty dictionary
data_dict = {}

# Check if there are enough words to create key-value pairs
if len(words) >= 9:
    data_dict = {
        "Code": words[0],
        "Action": words[1],
        "Value1": words[2],
        "Value2": words[3],
        "Value3": words[4],
        "Value4": words[5],
        "Parameter1": words[7].split('=')[0],
        "Parameter1Value": words[7].split('=')[1],
        "Parameter2": words[8].split('=')[0],
        "Parameter2Value": words[9].split('=')[1]
    }
# If Parameter2 is "Account", change it to "Account Balance"
if data_dict["Parameter2"] == "Account":
    data_dict["Parameter2"] = "Account Balance"

# Convert the dictionary to JSON
json_data = json.dumps(data_dict, indent=2)

# Print the resulting JSON
print(json_data)
