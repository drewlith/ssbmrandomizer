from flask import (Flask, redirect, url_for, render_template,
                   flash, request, send_from_directory, send_file)
#from werkzeug.utils import secure_filename
import randomizer, base64, random, string, json, util
#from os.path import join, dirname, realpath

app = Flask(__name__)
app.secret_key = "its a secret to everyone"

def create_seed_code(flags): # Seed code is a unique identifier for the URL
    random.seed(flags)
    code = ""
    while True:
        code += random.choice(string.ascii_letters)
        if len(code) >= 20:
            return code

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin", methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        password = request.form["Password"]
        na_sotw = request.form["NA"]
        eu_sotw = request.form["EU"]
        sotw_dict = {
                "NA":na_sotw,
                "EU":eu_sotw
            }
        if "S$BMR1STHEB3$T" in password:
            with open('sotw.json', 'w') as output:
                json.dump(sotw_dict, output, indent=2)
    return render_template("admin.html")

@app.route("/simple", methods=['GET','POST'])
def simple():
    if request.method == 'POST':
        flags = request.form["flags"]
        if "-seed" not in flags:
            seed = ''.join(random.choices(string.digits + string.ascii_lowercase, k=8))
            flags = "-seed " + seed +  " " + flags
        code = create_seed_code(flags)
        randomizer.start(flags, code)
        return redirect(url_for('seed', seed=code))
    return render_template("simple.html")

@app.route("/advanced", methods=['GET','POST'])
def advanced():
    if request.method == 'POST':
        flags = request.form["flags"]
        if "-seed" not in flags:
            seed = ''.join(random.choices(string.digits + string.ascii_lowercase, k=8))
            flags = "-seed " + seed +  " " + flags
        code = create_seed_code(flags)
        randomizer.start(flags, code)
        return redirect(url_for('seed', seed=code))
    data = open("adv.json")
    adv_dict = data.read()
    data.close()
    return render_template("advanced.html", content=adv_dict)

@app.route("/<seed>")
def seed(seed):
    # Find xdelta and include it in content
    try:
        xdelta = open("seeds/" + seed + ".xdelta", "rb").read()
    except:
        return "<h1>No seed found!</h1>"
    seed_json_data = open("json/" + seed + ".json")
    seed_data = seed_json_data.read()
    seed_json_data.close()
    patch_data = base64.b64encode(xdelta).decode('ascii')
    return render_template("seed.html", content=[patch_data, seed_data])

@app.route("/sotw_na")
def sotw_na():
    data = open("sotw.json")
    sotw_dict = json.load(data)
    data.close()
    return redirect("/" + sotw_dict["NA"])

@app.route("/sotw_eu")
def sotw_eu():
    data = open("sotw.json")
    sotw_dict = json.load(data)
    data.close()
    return redirect("/" + sotw_dict["EU"])

if __name__ == "__main__":
    app.run(debug=True)
