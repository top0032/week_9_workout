import json
from fastapi import FastAPI, HTTPException
from pathlib import Path

app = FastAPI(title="캡스톤 프로젝트 API (JSON)")

# --- JSON 파일을 읽어오기 위한 설정 ---

# 현재 파일(app.py)의 위치를 기준으로 /app/ 폴더 경로를 찾습니다.
BASE_DIR = Path(__file__).resolve().parent 

# 데이터 폴더의 경로를 /app/data 로 설정합니다.
DATA_DIR = BASE_DIR / "data"

def read_json_data(filename: str):
    """
    data 폴더에서 파일 이름(예: 'subject')을 받아
    'subject.json' 파일의 내용을 읽어옵니다.
    """
    # 읽어올 파일의 전체 경로를 조합합니다.
    file_path = DATA_DIR / f"{filename}.json"
    
    # 파일이 존재하는지 확인합니다.
    if not file_path.exists():
        # 파일이 없으면 404 에러를 발생시킵니다.
        raise HTTPException(status_code=404, detail=f"Data file '{filename}.json' not found.")
    
    try:
        # UTF-8 인코딩으로 JSON 파일을 엽니다.
        with open(file_path, 'r', encoding='utf-8') as f:
            # JSON 데이터를 파이썬 딕셔너리/리스트로 변환하여 반환합니다.
            data = json.load(f)
        return data
    except Exception as e:
        # 파일을 읽는 중 오류가 발생하면 500 에러를 발생시킵니다.
        raise HTTPException(status_code=500, detail=f"Error reading data file: {e}")

# --- API 엔드포인트 정의 ---

# 1. /api/subject
@app.get('/api/subject')
def get_subject():
    # 'subject.json' 파일의 내용을 반환합니다.
    return read_json_data("subject")

# 2. /api/rationale
@app.get('/api/rationale')
def get_rationale():
    # 'rationale.json' 파일의 내용을 반환합니다.
    return read_json_data("rationale")

# 3. /api/features
@app.get('/api/features')
def get_features():
    # 'features.json' 파일의 내용을 반환합니다.
    return read_json_data("features")

# 4. /api/environment
@app.get('/api/environment')
def get_environment():
    # 'environment.json' 파일의 내용을 반환합니다.
    return read_json_data("environment")

# 5. /api/team
@app.get('/api/team')
def get_team():
    # 'team.json' 파일의 내용을 반환합니다.
    return read_json_data("team")