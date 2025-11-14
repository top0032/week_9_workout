import os
import json
from flask import Flask, jsonify, render_template

app = Flask(__name__)
# 현재 파일(app.py)이 있는 디렉토리를 기준으로 'data' 폴더의 절대 경로 설정

app.json.ensure_ascii = False

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

def get_json_data(page_name):
    """페이지 이름(예: subject)에 해당하는 JSON 파일을 로드합니다."""
    file_path = os.path.join(DATA_DIR, f'{page_name}.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

# --- API 라우팅 (수정 불필요) ---
@app.route('/api/<page_name>', methods=['GET'])
def api_data(page_name):
    data = get_json_data(page_name)
    if data:
        return jsonify(data)
    return jsonify({'error': f'데이터 파일 ({page_name}.json)을 찾을 수 없습니다.'}), 404

# --- 페이지 라우팅 (⚠️ 이 부분을 수정/확인하세요) ---
PAGE_LIST = ['subject', 'rationale', 'features', 'environment', 'team']

@app.route('/')
@app.route('/main')
def main_page():
    """메인 페이지 (index.html)를 렌더링합니다."""
    return render_template('index.html')

# 1. 'subject.html', 'rationale.html' 등 .html이 붙은 경로 처리
@app.route('/<page_name>.html')
def content_page_html(page_name):
    if page_name in PAGE_LIST:
        return render_template(f'{page_name}.html')
    return "Page not found", 404

# 2. (선택적) 'subject', 'rationale' 등 .html이 없는 경로도 처리
@app.route('/<page_name>')
def content_page(page_name):
    if page_name in PAGE_LIST:
        return render_template(f'{page_name}.html')
    # '/api' 경로가 아닌데 PAGE_LIST에도 없으면 404 반환
    if page_name.startswith('api'):
        return "Page not found (Did you mean /api/...?)", 404
    return "Page not found", 404

# --- 서버 실행 ---
if __name__ == '__main__':
    # Docker 환경을 고려하여 호스트를 0.0.0.0으로 설정
    app.run(host='0.0.0.0', port=5000, debug=True)