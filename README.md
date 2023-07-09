# Project Costa: Flask Trade Data Analysis App

*Inspired by Project Manhattan, but no Bombs or Nuclear fusion/fission or nuclear science involved, of course, nothing is involved, just kidding!*

Now getting to the real description...

## Description

The Flask Trade Data Analysis App is a web application built using Flask, a lightweight Python web framework. This app provides a convenient way to analyze trade data, including sales, wastage, and stock information for various products.

## Features

- **Data Analysis**: The app allows users to input a specific date or date range and select a product for analysis. It calculates the remaining stock and wastage quantity for the chosen product within the specified date range.

- **Multiple Data Sources**: The app supports importing data from multiple CSV files, including sales data, wastage data, and stock in-hand data. The user can provide the file paths or choose from pre-configured file locations.

- **Interactive Calendar**: The app includes an interactive calendar interface, making it easy to select the desired date or date range for analysis. Users can navigate through different months and years to choose specific dates.

- **Product Name Autocomplete**: The app provides an autocomplete feature for the product name input field, helping users quickly select the desired product from a list of available options.

- **Responsive UI**: The app is designed with a responsive user interface, ensuring compatibility across different devices and screen sizes, including desktops, tablets, and mobile devices.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sriramvinn/Project-Costa-Flask-Trade-Data-Analysis-App.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repo
   ```

3. Download the `CSV files` using this [link](https://drive.google.com/drive/folders/1Y9aJaAO3S4ifkM3Xxv5czcGiAYp7IYAj?usp=sharing), and them in 'your-repo'.

4. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask development server:

   ```bash
   python app.py
   ```

2. Access the app in your web browser:

   ```
   http://localhost:5000
   ```

3. Select the desired date or date range using the interactive calendar.

4. Choose the product from the dropdown or type the beginning part of the product name.

5. Click the "Calculate" button to analyze the trade data for the selected product and date range.

6. The app will display the remaining stock and wastage quantity for the chosen product.

## Dependencies

The Flask Trade Data Analysis App has the following dependencies:

- Python 3.x
- Flask 2.x or later
- pandas library

Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```
