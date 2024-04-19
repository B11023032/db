from flask import Flask, request

app = Flask(__name__)

@app.route('/process_company_id', methods=['POST'])
def process_company_id():
    data = request.json
    company_id = data.get('companyID')
    print("Received companyID:", company_id)
    # 在此处执行您想要的任何操作，例如将公司ID存储到文件中
    return 'Received companyID: ' + company_id

if __name__ == '__main__':
    app.run(debug=True)
