Empresa Logística

Empresa Logística is a web application to manage shipments. Allows create new shipment orders, view history. Authentication is based in JWT and role separation.

📦 Technologies:

Frontend: React, Axios, HTML y CSS

Backend: Python, FastAPI, SQLAlchemy, Pydantic

Base de datos: MySQL (deployment in Railway)

Authentication: JWT (JSON Web Tokens)

Deployment:

Backend: Railway

Frontend: Vercel


Others: Docker (development), Postman (API testing)

Initially , the project was designed to deploy it in AWS using services such as EC2, RDS y S3, in order to optimize resources, another alternative was made, backend is in Railway and frontend in Vercel.


![AWS Architecture](./aws-architecture.png)


🚀 Installation and local deployment

1. Clone the repository
`cd EmpresaLogistica`

2. Backend:

`cd Backend`
```python
python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows
pip install -r requirements.txt
uvicorn main:app --reload
```
3. Frontend:

`cd ../frontend`
```js
npm install
npm start
```
swagger: https://empresalogistica-production.up.railway.app/docs
