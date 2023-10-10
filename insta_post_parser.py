import json
import pandas as pd
import codecs

json_file_path = YOUR FILE PATH

# Load JSON data from the file
with open(json_file_path, 'r') as file:
    json_data = json.load(file)

# Initialize empty lists to store parsed information
creation_timestamp_list = []
latitude_list = []
longitude_list = []
title_list = []

# Iterate through the JSON data and extract the desired values
for item in json_data:
    media_list = item.get('media', [])
    for media_item in media_list:
        creation_timestamp = media_item.get('creation_timestamp', '')
        media_metadata = media_item.get('media_metadata', {})
        photo_metadata = media_metadata.get('photo_metadata', {})
        exif_data = photo_metadata.get('exif_data', [])
        
        # Extract latitude, longitude, and title if available
        for exif_entry in exif_data:
            latitude = exif_entry.get('latitude', None)
            longitude = exif_entry.get('longitude', None)
            title = media_item.get('title', '')
            
            # Decode titles with Unicode escape sequences
            title = codecs.decode(title, 'unicode_escape')
            
            # Append values to lists
            creation_timestamp_list.append(creation_timestamp)
            latitude_list.append(latitude)
            longitude_list.append(longitude)
            title_list.append(title)

# Create a DataFrame
df = pd.DataFrame({
    'creation_timestamp': creation_timestamp_list,
    'latitude': latitude_list,
    'longitude': longitude_list,
    'title': title_list
})

# Display the DataFrame

df['creation_timestamp'] = pd.to_datetime(df['creation_timestamp'], unit='s')

df.head()