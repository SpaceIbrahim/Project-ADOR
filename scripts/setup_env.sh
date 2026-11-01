#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Creating Python virtual environment 'drawer_env'..."
python3 -m venv ../drawer_env

echo "Activating environment..."
source ../drawer_env/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing project dependencies..."
# Installs MuJoCo, RL framework, and vision processing libraries
pip install mujoco mujoco-menagerie torch torchvision opencv-python dm_control

echo "Environment setup complete. To activate it manually from the project root, run:"
echo "source drawer_env/bin/activate"