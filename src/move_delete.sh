#!/bin/bash

SOURCE_DIR="/d/transfer/"
DEST_DIR="/f/misc/favs/transfer"

# Loop through each file in the source directory
for file in "$SOURCE_DIR"/*; do
    # Extract the filename
    filename=$(basename "$file")

    # Check if the file does not exist in the destination directory
    if [ ! -f "$DEST_DIR/$filename" ]; then
        # Move the file to the destination directory
        mv "$file" "$DEST_DIR"
    else
        # Delete the file from the source directory
        rm "$file"
    fi
done
