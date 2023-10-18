document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const resultDiv = document.getElementById('result');
    const analyzedImage = document.getElementById('analyzed-image');
    const analysisResult = document.getElementById('analysis-result');
    const imageSizeElement = document.getElementById('image-size');
    const textContentElement = document.getElementById('text-content'); // 텍스트 내용을 표시할 요소

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(form);

        fetch('/analyze', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // 이미지 표시
            analyzedImage.src = data.image_data_url;

            // 분석 결과 표시
            analysisResult.textContent = `이미지 크기: ${data.image_width} x ${data.image_height}`;

            // 이미지 바이트 크기 표시
            imageSizeElement.textContent = `이미지 크기: ${data.image_size}`;

            // 텍스트 파일 내용 표시
            textContentElement.textContent = `텍스트 내용: ${data.text_content}`;
        });
    });
});