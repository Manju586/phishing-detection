<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for
import pickle
import pandas as pd
import myutils

# Initialize Flask app
app = Flask(__name__)

# Load trained model
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

print("Model loaded successfully")

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")

        if url:
            try:
                features = myutils.extract_features(url)
                df = pd.DataFrame([features], columns=[f'f{i}' for i in range(6)])
                pred = model.predict(df)[0]
                prob = model.predict_proba(df)[0]
                confidence = max(prob) * 100

                result = f"Phishing Website ⚠️ ({confidence:.0f}% confidence)" if pred == 1 else f"Safe Website ✅ ({confidence:.0f}% confidence)"

                return redirect(url_for('index', result=result))

            except Exception as e:
                return redirect(url_for('index', result=f"Error: {str(e)}"))

        else:
            return redirect(url_for('index', result="Please enter a URL"))

    result = request.args.get("result")
    return render_template("index.html", result=result)

if __name__ == "__main__":
    print("🚀 Starting Flask App...")
    app.run(debug=True)

=======
from flask import Flask, render_template, request, redirect, url_for
import pickle
import pandas as pd
import myutils

# Initialize Flask app
app = Flask(__name__)

# Load trained model
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

print("Model loaded successfully")

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url")

        if url:
            try:
                features = myutils.extract_features(url)
                df = pd.DataFrame([features], columns=[f'f{i}' for i in range(6)])
                pred = model.predict(df)[0]
                prob = model.predict_proba(df)[0]
                confidence = max(prob) * 100

                result = f"Phishing Website ⚠️ ({confidence:.0f}% confidence)" if pred == 1 else f"Safe Website ✅ ({confidence:.0f}% confidence)"

                return redirect(url_for('index', result=result))

            except Exception as e:
                return redirect(url_for('index', result=f"Error: {str(e)}"))

        else:
            return redirect(url_for('index', result="Please enter a URL"))

    result = request.args.get("result")
    return render_template("index.html", result=result)

if __name__ == "__main__":
    print("🚀 Starting Flask App...")
    app.run(debug=True)

>>>>>>> 08fecdd54fbe2dc6ac947359e85d0c18a11c5aea
