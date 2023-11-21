#!/bin/bash

read -p "Enter the path to the source directory: " SOURCE_DIR
read -p "Enter the path to the destination directory: " DEST_DIR

echo "Starting file transfer from $SOURCE_DIR to $DEST_DIR..."

# Count the total number of files in the source directory
total_files=$(ls -1 "$SOURCE_DIR" | wc -l)
current_file=0

# Loop through each file in the source directory
for file in "$SOURCE_DIR"/*; do
    current_file=$((current_file + 1))
    filename=$(basename "$file")

    # Check if the file does not exist in the destination directory
    if [ ! -f "$DEST_DIR/$filename" ]; then
        echo "Moving file $current_file of $total_files: '$filename'"
        mv "$file" "$DEST_DIR"
    else
        echo "Deleting already transferred file $current_file of $total_files: '$filename'"
        rm "$file"
    fi
done

echo "File transfer completed."
