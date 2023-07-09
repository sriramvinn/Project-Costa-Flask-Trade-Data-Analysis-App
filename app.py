from flask import Flask, render_template, request
from flask_restful import Api, Resource
import pandas as pd


app = Flask(__name__, static_url_path='/static')


def calculate_stock_and_wastage(start_date, end_date, product_name):
	# Load sales data for the specified period
    sales_df = pd.read_csv('sales_data.csv')
    # sales_df['Date'] = pd.to_datetime(sales_df['Date'], format='%d/%m/%Y')
    sales_df = sales_df[(sales_df['Date'] >= start_date) & (sales_df['Date'] <= end_date) & sales_df['Product'].str.startswith(product_name)]
    total_sold = int(sales_df['Quantity'].astype('float').sum())

    # Load wastage data for the specified period
    wastage_df = pd.read_csv('merged_data.csv')
    # wastage_df['Date'] = pd.to_datetime(wastage_df['Date'], format='%d/%m/%Y')
    wastage_df = wastage_df[(wastage_df['Date'] >= start_date) & (wastage_df['Date'] <= end_date) & wastage_df['Product'].str.startswith(product_name)]
    total_wastage = int(wastage_df['Quantity'].astype('float').sum())

    # Load stock in hand data for the beginning of the week
    stock_df = pd.read_csv('on_hand.csv')
    stock_in_hand = stock_df.loc[stock_df['Description'].str.startswith(product_name), 'On Hand'].sum()

    # Calculate remaining stock in hand
    print(stock_in_hand, total_sold, total_wastage)
    remaining_stock = int(stock_in_hand - total_sold - total_wastage)

    return remaining_stock, total_wastage, total_sold


@app.route('/', methods=['GET'])
def home():
    stock_df = pd.read_csv('on_hand.csv')
    product_names = stock_df['Description'].unique().tolist()
    return render_template('index.html', product_names=product_names)

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get the selected date range from the form
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    product_name = request.form['product_name']

    # Perform the stock and wastage calculations based on the selected date range and product name
    remaining_stock, total_wastage, total_sold = calculate_stock_and_wastage(start_date, end_date, product_name)

    # Render the result template with the calculated values
    return render_template('result.html', remaining_stock=remaining_stock, total_wastage=total_wastage, total_sold= total_sold)


if __name__ == '__main__':
    app.run(debug=True)
