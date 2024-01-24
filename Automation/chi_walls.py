import os
import random

def change_wallpaper():
    # Replace 'path/to/your/wallpapers' with the actual path to your wallpaper images
    wallpaper_folder = '/Users/kai/2024/chiwallpapers2'
    
    # List all files in the wallpaper folder
    wallpapers = [f for f in os.listdir(wallpaper_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]

    if wallpapers:
        # Select a random wallpaper from the list
        selected_wallpaper = random.choice(wallpapers)
        
        # Build the full path to the selected wallpaper
        wallpaper_path = os.path.join(wallpaper_folder, selected_wallpaper)

        # Use osascript to change the wallpaper
        os.system(f"osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"{wallpaper_path}\"'")

        print(f"Wallpaper changed to: {selected_wallpaper}")
    else:
        print("No valid wallpapers found in the specified folder.")

# Call the function to change the wallpaper
change_wallpaper()
