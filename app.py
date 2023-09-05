# app.py
from flask import Flask, render_template, request, redirect, url_for
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Google Sheets API setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('./expence-tracker-398008-bee26deccd2b.json', scope)
client = gspread.authorize(creds)

# Google Sheet name
sheet_name = "Money"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    earn = request.form.get('earn')
    expense = request.form.get('expense')
    amount = float(request.form.get('amount'))
    date = request.form.get('date')
    category = request.form.get('category')
    
    # Open the Google Sheet
    sheet = client.open(sheet_name).sheet1
    
    # Append data to the sheet
    row = [earn, expense, amount, date, category]
    sheet.append_row(row)
    
    # Redirect back to the main page after successful submission
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)










# # app.py
# from flask import Flask, render_template, request, redirect, url_for
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# app = Flask(__name__)

# # Google Sheets API setup
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name('./expence-tracker-398008-bee26deccd2b.json', scope)
# client = gspread.authorize(creds)

# # Google Sheet name
# sheet_name = "Money"

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     earn = request.form.get('earn')
#     expense = request.form.get('expense')
#     amount = float(request.form.get('amount'))
#     date = request.form.get('date')
#     category = request.form.get('category')
    
#     # Open the Google Sheet
#     sheet = client.open(sheet_name).sheet1
    
#     # Calculate remaining balance based on earn and expense
#     if earn == 'Yes':
#         balance_change = amount
#     elif expense == 'Yes':
#         balance_change = -amount
#     else:
#         balance_change = 0.0

#     # Append data to the sheet
#     row = [earn, expense, amount, date, category, balance_change]
#     sheet.append_row(row)
    
#     # Calculate the total remaining balance and update it in the sheet
#     total_balance = sheet.cell(sheet.row_count, 7).value + balance_change
#     sheet.update_cell(sheet.row_count, 7, total_balance)
    
#     # Redirect back to the main page after successful submission
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)



# # app.py
# from flask import Flask, render_template, request, redirect, url_for
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# app = Flask(__name__)

# # Google Sheets API setup
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name('./expence-tracker-398008-bee26deccd2b.json', scope)
# client = gspread.authorize(creds)

# # Google Sheet name
# sheet_name = "Money"

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     earn = request.form.get('earn')
#     expense = request.form.get('expense')
#     amount = request.form.get('amount')
#     date = request.form.get('date')
#     category = request.form.get('category')
    
#     # Open the Google Sheet
#     sheet = client.open(sheet_name).sheet1
    
#     # Append data to the sheet
#     row = [earn, expense, amount, date, category]
#     sheet.append_row(row)
    
#     # Redirect back to the main page after successful submission
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)


# # app.py
# from flask import Flask, render_template, request
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# app = Flask(__name__)

# # Google Sheets API setup
# scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# creds = ServiceAccountCredentials.from_json_keyfile_name('./expence-tracker-398008-bee26deccd2b.json', scope)
# client = gspread.authorize(creds)

# # Google Sheet name
# sheet_name = "Money"

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     earn = request.form.get('earn')
#     expense = request.form.get('expense')
#     amount = request.form.get('amount')
#     date = request.form.get('date')
#     category = request.form.get('category')
    
#     # Open the Google Sheet
#     sheet = client.open(sheet_name).sheet1
    
#     # Append data to the sheet
#     row = [earn, expense, amount, date, category]
#     sheet.append_row(row)
    
#     return "Data saved successfully!"

# if __name__ == '__main__':
#     app.run(debug=True)
