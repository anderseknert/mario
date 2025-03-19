#!/bin/bash

for file in assets/*.png; do
    if [ -f "$file" ]; then
        echo "Processing $file..."
        # Resize to 300x300 while maintaining aspect ratio and optimizing for web
        convert "$file" -resize 300x300\> -strip -quality 85 "$file"
    fi
done

echo "Image processing complete! Original images are backed up in assets_backup/"