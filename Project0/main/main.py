from flask import Flask, request

app = Flask(__name__)

@app.route('/process_company_id', methods=['POST'])
def process_company_id():
    company_id = request.form.get('companyID')
    print("Received companyID:", company_id)
    return 'Received companyID: ' + company_id

if __name__ == '__main__':
    app.run(debug=True)
