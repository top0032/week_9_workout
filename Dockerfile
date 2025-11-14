# 1. 기본이 될 파이썬 이미지를 가져옵니다.
FROM python:3.10-slim

# 2. 작업 디렉토리를 /app으로 설정합니다.
WORKDIR /app

# 3. requirements.txt 파일을 복사하고 설치합니다.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 현재 폴더(.)의 모든 파일을 컨테이너의 /app으로 복사합니다.
COPY . .

# 5. (선택) app.py가 5000번 포트를 사용한다고 명시합니다.
# (docker-compose.yml의 ports 설정이 더 중요하긴 합니다)
EXPOSE 5000

# 6. 컨테이너가 시작될 때 실행할 명령입니다.
# app.py에서 host='0.0.0.0'로 설정했으므로 python app.py로 바로 실행합니다.
CMD ["python", "app.py"]