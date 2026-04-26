from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return """
<html>
<body style="text-align:
center; margin-top:50px;">
<h1>Welcome to
MrFactz!</h1>
<p>Yeh meri pehli local
Python website hai.</p>
</body>
</html>
"""
if __name__ == "__main__":
    app.run(debug=True)


