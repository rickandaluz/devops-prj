
from flask import Flask, request, redirect, url_for
import jinja2

# Open template file
f = open("contact_page.html.j2", "r")
env = jinja2.Environment( loader=jinja2.FileSystemLoader('.'))

# Define Contact List file
filename = "data.txt"

app = Flask(__name__)

@app.route('/')
def getContacts():
    data = loadContacts()
    tmp = env.get_template("contact_page.html.j2")
    out = tmp.render(data=data)
    return out

@app.route('/new_contact', methods=['GET','POST'])
def newContact():
    if request.method == 'POST':
        print("new_contact called for", list(request.form.values()))
        addContact(**request.form)
    return redirect(url_for('getContacts'))

def loadContacts():
    data = []
    f = open(filename, "r")
    for line in f:
        line.strip()
        data.append(line.split(","))
    f.close()
    return data

def addContact(firstName="", lastName="", age=0, city="", email=""):
    print("addContact", firstName)
    f = open(filename, "a")
    newLine = f"{firstName},{lastName},{age},{city},{email}\n"
    f.write(newLine)

if __name__ =='__main__':
    app.run(host="0.0.0.0")
