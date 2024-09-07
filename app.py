from flask import Flask, render_template
from flask import request, jsonify
from text_labeling import TextLabelingWrapper

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tool')
def tool():
    return render_template('tool.html')

@app.route('/about')
def about():
    return render_template('about.html')

labeler = TextLabelingWrapper()

@app.route('/api/label_text', methods = ['POST'])
def label_text():
    try:
        data = request.get_json()
        html = labeler.label_text(data["text"], data["label_type"])
        return jsonify({"labeled_text": html}), 200
    except Exception as e:
        return jsonify({"error", str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
