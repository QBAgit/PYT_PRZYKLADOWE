"""
Zapoznaj się z modułem `my_phonebook` umieszczonym w pliku dołączonym do tego egzaminu. 
Znajdziesz tam listę zawierającą słowniki będące, książkom telefoniczną pewnego programisty.

 Używając Flaska, utwórz stronę, którą udostępnisz pod adresem `/pbk`:
 
 * jeśli użytkownik wejdzie na stronę metodą GET, wyświetl formularz, który:
    * będzie miał pole tekstowe o nazwie `nickname`,
    * będzie miał pole tekstowe o nazwie `number`
    * pola będą odpowiednio opisane

* jeśli użytkownik wejdzie na stronę metodą POST:
    * sprawdź, czy przynajmniej jedno z kryteriów zostało podane 
    * jeśli tak to wyświetl rekordy spełniające odpowiednie kryteria zakładając, 
      że podane napisy mogą być tylko elementem (np. nickname `al` powinien 
      wyświetlić zarówno rekordy dla `Ala Kowalska`, `Al` oraz `Jan Góralski`)
    * jeśli nie lub w przypadku gdy nie uda się nic znaleść, wyświetli napis "No record."
    
**Ważne:** Powołując aplikację Flaska, użyj zmiennej `app`!
"""

from my_phonebook import pb
from my_module import buildwebpage
from flask import Flask
from flask import request

app = Flask(__name__)

def myFilter(pb,name,num):
        
    if name=="" and num=="":
        return "No record"
    else:
        response = ""
        for item in pb:
            nick = item["nickname"]
            ph = item["number"]
            
            if name != "" and name.lower() in nick.lower():
                response += "{} : {}<br>".format(nick,ph)
            if num != "" and num.lower() in ph.lower():
                response += "{} : {}<br>".format(nick,ph)
        
        if response == "":
            response = "No record"
        
        return response

@app.route("/pbk", methods=['GET','POST'])
def PhoneBook():
    
    userresp = ""
    search_key = ""
    formbase = '''
        <h3>PhoneBook:</h3>
        <p>Search by Nick or Phone number:</p>
        <form method="POST">
            <label>
                Nick:
                <input type="input" name="nickname"/>
            </label>
                Phone number:
            <label>
                <input type="phone number" name="number"/>
            </label>
            <button type="sumbit">Submit</button>
        </form>'''
    if request.method == 'POST':
        try:
            nickname = request.form['nickname']
            number = request.form['number']
            search_key = "<p>Search Criteria: <i>Nick:</i> \"<b>{}</b>\"  <i>Name:</i> \"<b>{}</b>\"</p>".format(nickname,number)
            userresp = myFilter(pb,nickname,number)

        except Exception:
            userresp = "<h3>Nieznany Błąd/h3>"

    return buildwebpage(formbase + search_key + userresp)


def main():
    global app
    app.run()
    #Na wypadek problemów z portem 5000
    #app.run(port=4000)

if __name__ == "__main__":
    main()

