# 1. Python 3.10 기반 이미지 사용
FROM python:3.10

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. requirements.txt 파일 복사 후 패키지 설치
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 전체 소스 코드 복사
COPY app/ .

# 5. FastAPI 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
