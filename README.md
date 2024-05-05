# Car Scraping

This project involves developing a web scraper tailored for a car dealership. Its purpose is to extract information crucial for understanding how prices correlate with various car features, including model, year, mileage, and more.

## Objective

The objective of this project is purely academic and has no commercial purpose. It is carried out with the purpose of learning and practicing web scraping techniques.

## Technologies Used

The project is based on the following technologies:

- **Selenium**: Selenium is used to automate web navigation and extract information from the pages.
- **Python 3**: The primary programming language used in the development of the scraper.
- **Web Scraping**: Web scraping techniques are employed to obtain data from web pages in an automated manner.

## Setting up the Virtual Environment and Installing Dependencies

Below are the steps to create a Python virtual environment and install the necessary dependencies:

1. **Clone the Repository:** Clone this repository to your local machine using the following command:
    ```
    git clone git@github.com:Anonymate054/MCD-ML01.git
    cd MCD-ML01
    ```

2. **Create a Virtual Environment:** Navigate to the project directory and create a virtual environment using the following command:
    ```
    python3 -m venv venv
    ```

3. **Activate the Virtual Environment:** Activate the virtual environment with the following command:
    - On Windows:
    ```
    venv\Scripts\activate
    ```
    - On macOS and Linux:
    ```
    source venv/bin/activate
    ```

4. **Install Dependencies:** Once the virtual environment is activated, install the project dependencies by running the following command:
    ```
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

5. **Get Drivers:** Download drivers by run following command:
    ```
    chmod +x get_drivers.sh
    sudo ./get_drivers.sh
    ```

6. **Create directories:** Create directories by run following command:
    ```
    mkdir app/car_files
    mkdir app/links
    ```

7. **Run script:** Run pythons script by running the following command:
    ```
    python app/<python_script>.py
    ```

With these steps, you will have successfully set up the virtual environment and installed all the necessary dependencies to run the scraper.

## Usage

To use the scraper, simply run the main script and follow the instructions provided in the code.

