#!/bin/bash

# Ensure the output and input directories exist
mkdir -p extremeTestOutputs
mkdir -p extremeTest


# Prompt the user for memory sizes
echo "This will NOT overwrite existing test files!"
echo "This allows you to generate a massive test dataset and test individual files or sections at a time!"
echo "Enter the memory sizes to test with, separated by spaces like \"10 20 30 40\":"
read -a ram_sizes

# Call the Python script to generate new test files
python3 createFile.py "${ram_sizes[@]}"


# Iterate through the selected memory sizes
for size in "${ram_sizes[@]}"
do
    echo "Processing RAM size: $size"

    ./allocator -m $size -s first extremeTest/$size.txt > extremeTestOutputs/${size}_first.txt
    ./allocator -m $size -s best extremeTest/$size.txt > extremeTestOutputs/${size}_best.txt
    ./allocator -m $size -s worst extremeTest/$size.txt > extremeTestOutputs/${size}_worst.txt
done

# Call the Python script to validate test files
python3 validator.py "${ram_sizes[@]}"

echo "DONE!"
