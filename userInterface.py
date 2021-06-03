from flask import Flask, render_template, request

##
# This program enables user to purchase desired product 
# utilizing automation.
#

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/form')
def userInterface():
  return render_template("myDate.html")

@app.route('/results', methods=["POST"])
def results():
   purchaseDate = request.form['purchasetime']
   return render_template('pressStart.html', purchasetime = purchaseDate)

if __name__ == '__main__':
   app.run()