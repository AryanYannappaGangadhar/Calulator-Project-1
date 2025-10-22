#!/bin/bash

# This script sets up the development environment for the advanced-python-calculator project.

# Update package list and install Python3 and pip if not already installed
sudo apt update
sudo apt install -y python3 python3-pip

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

echo "Development environment setup complete. Activate the virtual environment using 'source venv/bin/activate'."