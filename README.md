# Drawry Backend 🖥️

🚀 **Drawry Backend**는 FastAPI 기반의 백엔드 서버로, AI 기반 이미지 생성 및 데이터 처리를 수행하는 RESTful API를 제공합니다.

---

## 📂 프로젝트 개요

**Drawry Backend**는 다음과 같은 기능을 제공합니다:

- 🔐 **사용자 인증 및 관리**: JWT 기반 인증 시스템
- 📦 **데이터 저장 및 관리**: MongoDB 및 Redis 활용
- ⚡ **비동기 처리 지원**: FastAPI + asyncio 기반 비동기 API

프론트엔드 레포지토리는 [Drawry Frontend](https://github.com/msai-project3-team4/Drawry-FrontEnd)에서 확인할 수 있습니다.

---

## 🛠 기술 스택

- **Framework**: FastAPI, Uvicorn
- **Database**: MongoDB, Redis
- **Auth**: JWT, OAuth2
- **Containerization**: Docker, Docker Compose
- **Task Queue**: Celery (Redis 사용 예정)
- **Testing**: Pytest

---

## 🚀 설치 및 실행 방법

### 1️⃣ 프로젝트 클론
```sh
git clone https://github.com/msai-project3-team4/Drawry-BackEnd.git
cd Drawry-BackEnd
```

### 2️⃣ 가상환경 생성 및 패키지 설치
```sh
python -m venv venv  # (Windows) python -m venv venv
source venv/bin/activate  # (Windows) venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ 서버 실행
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 📁 프로젝트 구조
[작성예정]

---

## 🐳 Docker 실행 방법
```sh
docker-compose up -d
```

```sh
docker build -t drawry-backend .
docker run -p 8000:8000 drawry-backend
```