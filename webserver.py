from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)
#app.config["IMAGE"] = "static/"

@app.route('/')
def myprofile():
    return render_template('index.html')

@app.route('/index.html')
def myprofile2():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')
    

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

#instead of create more route, use below method
@app.route("/<string:page_name>")
def page_route(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('databases/database.txt', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		database.write(f'\n{email},{subject},{message}')
		database.close()

def write_to_csv(data):
	with open('databases/database.csv', newline='', mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer=csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		print([email, subject, message])
		print(type([email, subject, message]))
		csv_writer.writerow([email,subject,message])
		
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():	
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'did not save to database'
	else:
		return 'oppss! something went wrong, please try again!'
           
    # the code below is executed if the request method
    # was GET or the credentials were invalid		