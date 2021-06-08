from flask import Flask, render_template, request

##
# This program enables user to purchase desired product 
# utilizing automation.
#

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def userInterface():
  return render_template("myDate.html")

@app.route('/results', methods=["POST"])
def results():
   purchaseDate = request.form['purchasetime']
   return render_template('pressStart.html', purchasetime = purchaseDate)

@app.route('/yes', methods=["GET"])
def yes():
   return render_template("success.html")

@app.route('/no', methods=["GET"])
def no():
   return render_template("betterLuckNextTime.html")

if __name__ == '__main__':
   app.run()