# 1. Python 3.10 이미지를 기반으로 시작
FROM python:3.10-slim

# 2. 작업 디렉토리 설정 (컨테이너 내부의 경로)
WORKDIR /code/api

# 3. requirements.txt 파일 먼저 복사
# (로컬의 api/requirements.txt 를 /code/api/requirements.txt 로 복사)
COPY ./requirements.txt /code/api/requirements.txt

# 4. 의존성 설치 (SSL 오류 해결 옵션 포함)
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# 5. app 폴더 전체 복사
# (로컬의 api/app/ 폴더를 /code/api/app/ 으로 복사)
# (app 폴더 안의 data 폴더도 이 명령어 하나로 함께 복사됩니다.)
COPY ./app /code/api/app

# 6. uvicorn 서버 실행
#    "app.main:app" -> app 폴더의 main.py 파일 안에 있는 app 변수를 실행
#    "--host", "0.0.0.0" -> 컨테이너 외부에서 접근 허용
#    "--port", "8000" -> 컨테이너 내부 8000번 포트에서 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]