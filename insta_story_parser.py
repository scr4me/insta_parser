import pandas as pd
import json

# Specify the path to your JSON file
json_file_path = YOUR FILE PATH

# Load JSON data from the file
with open(json_file_path, 'r') as file:
    json_data = json.load(file)

#Create a Dataframe with predefined columns
df = pd.DataFrame(columns=["uri",
        "creation_timestamp",
        "device_id",
        "camera_position",
        "source_type",
        "title",
        "source_app",
        "date_time_original"])

ig_stories = json_data['ig_stories']
for story in ig_stories:
    uri = story["uri"]
    creation_timestamp = story["creation_timestamp"]
    media_metadata = story.get("media_metadata", {})
    exif_data = media_metadata.get("video_metadata", {}).get("exif_data", []) or media_metadata.get("photo_metadata", {}).get("exif_data", [])
    
    # Check if "exif_data" is not empty before accessing its elements
    if exif_data:
        device_id = exif_data[0].get("device_id", "")
        camera_position = exif_data[0].get("camera_position", "")
        source_type = exif_data[0].get("source_type", "")
        latitude = exif_data[0].get("latitude", "")
        longitude = exif_data[0].get("longitude", "")
        date_time_original = exif_data[0].get("date_time_original", "")
    else:
        device_id = ""
        camera_position = ""
        source_type = ""
        latitude = ""
        longitude = ""
        date_time_original = ""
    
    title = story["title"]
    source_app = story["cross_post_source"]["source_app"]

    df = df.append({
        "uri": uri,
        "creation_timestamp": creation_timestamp,
        "device_id": device_id,
        "camera_position": camera_position,
        "source_type": source_type,
        "title": title,
        "source_app": source_app,
        "latitude": latitude,
        "longitude": longitude,
        "date_time_original": date_time_original
    }, ignore_index=True)

df.head()