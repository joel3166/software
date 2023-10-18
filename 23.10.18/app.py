from flask import Flask, request, jsonify, render_template
from PIL import Image
import base64
import io
import humanize

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_image():
    if 'image' not in request.files and 'text' not in request.files:
        return jsonify({'error': 'No image or text file provided'}), 400

    image = request.files.get('image')
    text = request.files.get('text')

    image_data_url = ""
    image_width = 0
    image_height = 0
    image_size = 0
    text_content = ""

    if image:
        # 이미지 처리
        img = Image.open(image)
        width, height = img.size
        img_bytes = image.read()
        image_size = humanize.naturalsize(len(img_bytes))
        buffered = io.BytesIO()
        img.save(buffered, format="JPEG")
        img_data = base64.b64encode(buffered.getvalue()).decode()
        image_data_url = f"data:image/jpeg;base64,{img_data}"
        image_width = width
        image_height = height

    if text:
        # 텍스트 파일 내용 읽기
        text_content = text.read().decode('euc-kr', 'utf-8')

    result = {
        'image_data_url': image_data_url,
        'image_width': image_width,
        'image_height': image_height,
        'image_size': image_size,
        'text_content': text_content
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)