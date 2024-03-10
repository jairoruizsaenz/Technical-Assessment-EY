# Data Challenge

Welcome! This repository contains the source code for the EY data challenge. 

You can check the step-by-step analysis process and conclusions [here](https://datachallenge.jairo.digital/)

## Important files

1. Scripts Folder: This folder contains the scripts used for the analysis. Scripts are provided in both .ipynb (Interactive Python Notebook) and HTML formats.
1. Results Folder: This folder contains reports, charts, and any other files generated during the analysis.
1. Other Files Folder: This folder contains additional files not directly used in the analysis.

## Installation

To get started, follow these steps:

### Prerequisites

- Python 3.10 installed on your system.

### Setting up a Virtual Environment

It's always a good practice to use a virtual environment for Python projects to manage dependencies. Here's how to set it up:

1. Open your terminal or command prompt.
2. Navigate to the root directory of this project.
3. Run the following command to create a virtual environment (replace `myenv` with your preferred environment name):
   ```bash
   python3 -m venv myenv
   ```

### Activate the virtual environment
On Windows:
   ```bash
   myenv\Scripts\activate
   ```
On macOS and Linux:
   ```bash
   source myenv/bin/activate
   ```

### Installing Dependencies

Once you have activated the virtual environment, you can install the required dependencies using the requirements.txt
   ```bash
   pip install -r requirements.txt
   ```

## Data

In order to replicate the analysis, please note that the data files are missing. Once you have downloaded the data files, create a data folder at the root level with the following structure:

- data
    - Graduate School and University
        - Column names
            - KI9119A_1920.xlsx
            - KI9119A_2021.xlsx
            - KI9119A_2122.xlsx
            - KI9119A_2223.xlsx
            - KI9119B_1920.xlsx
            - KI9119B_2021.xlsx
            - KI9119B_2122.xlsx
            - KI9119B_2223.xlsx            
        - Datasets
            - KI9119A_1920.csv
            - KI9119A_2021.csv
            - KI9119A_2122.csv
            - KI9119A_2223.csv
            - KI9119B_1920.csv
            - KI9119B_2021.csv
            - KI9119B_2122.csv
            - KI9119B_2223.csv
    - High School
        - Column names
            - F9117G_1920.xlsx
            - F9117G_2021.xlsx
            - F9117G_2122.xlsx
            - F9117G_2223.xlsx
        - Datasets
            - F9117G_1920.csv
            - F9117G_2021.csv
            - F9117G_2122.csv
            - F9117G_2223.csv
