import os
from flask import Flask, request, render_template, send_from_directory, redirect, url_for
from csv_util import CSVUtility
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        csv_file = request.files['file']
        if csv_file.filename.endswith('.csv'):
            path = os.path.join(app.config['UPLOAD_FOLDER'], csv_file.filename)
            csv_file.save(path)
            return redirect(url_for('index', filename=csv_file.filename))

    filename = request.args.get('filename')
    if filename:
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        util = CSVUtility(path)
        return render_template(
            'index.html',
            filename=filename,
            uploaded=True,
            columns=util.columns,
            numeric_columns=util.numeric_columns
        )
    return render_template('index.html', uploaded=False)

@app.route('/display/<filename>')
def display(filename):
    util = CSVUtility(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    preview = util.df.head(3).to_html(index=False)
    return render_template('display.html', table=preview, filename=filename)

@app.route('/filter', methods=['POST'])
def filter_csv():
    filename = request.form['filename']
    column = request.form['column']
    op = request.form['operator']
    value = request.form['value']
    util = CSVUtility(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    try:
        result_df = util.filter_rows(column, op, value)
    except Exception as e:
        return f"Error: {e}"
    output_path = os.path.join(app.config['OUTPUT_FOLDER'], f"filtered_{filename}")
    util.write_to_csv(result_df, output_path)
    return render_template('result.html', table=result_df.to_html(index=False), file=os.path.basename(output_path), filename=filename, result_sentence=f"Filtered Data({column}{op}{value})")

@app.route('/sort', methods=['POST'])
def sort_csv():
    filename = request.form['filename']
    column = request.form['column']
    order = request.form['order'] == 'asc'
    util = CSVUtility(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    result_df = util.sort_rows(column, ascending=order)
    output_path = os.path.join(app.config['OUTPUT_FOLDER'], f"sorted_{filename}")
    util.write_to_csv(result_df, output_path)
    return render_template('result.html', table=result_df.to_html(index=False), file=os.path.basename(output_path), filename=filename, result_sentence=f"Sorted Data({column} {request.form['order'].capitalize()})")

@app.route('/aggregate', methods=['POST'])
def aggregate_csv():
    filename = request.form['filename']
    column = request.form['column']
    operation = request.form['operation']
    util = CSVUtility(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    result = util.aggregate_column(column, operation)
    return f"{operation.capitalize()} of {column}: {result}"

@app.route('/palindromes', methods=['POST'])
def palindrome_csv():
    filename = request.form['filename']
    column = request.form['column']
    util = CSVUtility(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    count = util.count_palindromes(column)
    return f"Palindrome count in '{column}': {count}"

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)