# Scrape courses based on given credit hour

Welcome to this project! To get started, follow the steps below:

## Installation

1. Install the required dependencies using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

## Edits

1. Edit the constants in the `constants.py` file to customize the behavior of the project.
    - Replace TERM in constants.py with fall or sprng and the year you want the data from --> example fall2023, sprng2020
    - Replace credit_hour with whatever you want but it should have .0 at the end --> example 1.0, 2.0, 3.0

## Running the Project

Run the `main.py` script to execute the main functionality of the project. --> print data to terminal

```bash
python3 main.py
```

Run the `main.py > results.txt` script to execute the main functionality of the project. --> saves data to results.txt file

```bash
python3 main.py > results.txt