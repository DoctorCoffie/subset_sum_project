#!/bin/bash

# Update requirements.txt
echo "Updating requirements.txt..."
pip freeze > requirements.txt
echo "Requirements updated."

# Generate integer arrays
echo "Generating integer arrays..."
python generate_arrays.py
echo "Integer arrays generated."

# Run main.py
echo "Running main.py..."
python main.py
echo "Project execution completed."
