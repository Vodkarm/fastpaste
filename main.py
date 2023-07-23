import json, string, random, os
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
	return redirect("https://github.com/vodkarm/fastpaste#documentation")

@app.route('/new', methods=["GET"])
def new():
	if request.args.get("content"):
		id = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(6))
		secret = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(16))
		with open(f"pastes/{id}.txt", "w") as f:
			f.write(request.args.get("content"))
		data = json.load(open("secrets.json"))
		data[id] = secret
		open("secrets.json", "w").write(json.dumps(data))
		return json.dumps({"success": True, "data": {"id": id, "url": request.base_url.replace("/new", "/paste?id=") + id, "secret": secret}})
	else:
		return json.dumps({"success": False, "error": "Unreachable content"})
	
@app.route('/paste', methods=["GET"])
def paste():
	if request.args.get("id"):
		try:
		    return open(f"pastes/{request.args.get('id')}.txt", "r").read()
		except:
			return json.dumps({"success": False, "error": "Unreachable content"})
	else:
		return redirect(request.base_url.replace("/paste", "/"))
	
@app.route("/delete", methods=["GET"])
def delete():
	if request.args.get("id") and request.args.get("secret"):
		if json.load(open("secrets.json"))[request.args.get("id")] == request.args.get("secret"):
			try:
			    os.remove(f"pastes/{request.args.get('id')}.txt")
			    data = json.load(open("secrets.json"))
			    del data[request.args.get("id")]
			    open("secrets.json", "w").write(json.dumps(data))
			    return json.dumps({"success": True})
			except:
				return json.dumps({"success": False, "error": "Unreachable content"})
		else:
			return json.dumps({"success": False, "error": "Invalid secret id"})
	else:
		return redirect(request.base_url.replace("/paste", "/"))

if __name__ == "__main__":
	app.run("0.0.0.0", 6536, debug=False)