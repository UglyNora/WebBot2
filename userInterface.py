from flask import Flask

##
# This program enables user to purchase desired product 
# utilizing automation.
#

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def userInterface():
   page = """
     <h1>Choose a date and time then press start. Good luck! </h1>
        <form>
         <button id= "start" name = "start">START</button>
         <br><br/>
         <label name="purchasetime">I want to purchase this item on (date and time):</label>
         <input type="datetime-local" id="purchasetime" name="purchasetime">
         <input type="submit" id = "submitbutton" name = "submitbutton">
         <h3>Results:</h3>
      
   
         </form>
   """
   ##resultOfPurchase = 
   return page

if __name__ == '__main__':
   app.run()