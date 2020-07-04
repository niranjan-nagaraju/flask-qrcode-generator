from flask import Flask, render_template, request
import pyqrcode
from pyqrcode import QRCode
import io

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    text_content = None
    svg = None
    if request.method == 'POST':
        text_content = request.form['text_content']

        # Generate QR code
        url = pyqrcode.create(text_content)

        svg = io.BytesIO()
        url.svg(svg, scale = 8)

    svg_content = svg.getvalue().decode("utf-8") if svg else None
    return render_template('index.html', text_content=text_content, svg_content=svg_content)



if __name__ == '__main__':
    app.run(debug=True)
