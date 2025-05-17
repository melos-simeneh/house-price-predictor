# 🏡 House Price Prediction API

This is a RESTful API built using **FastAPI** that predicts house prices based on input features such as number of rooms, square footage, age of the house, and location score. The prediction is powered by a simple machine learning model trained using `scikit-learn`.

## 🛠️ Tech Stack

- **FastAPI** – Web framework
- **Uvicorn** – ASGI server
- **Scikit-learn** – ML model
- **Joblib** – Model serialization
- **NumPy** – Data handling
- **SlowAPI** – Rate limiting
- **Pydantic** – Data validation

## 📦 Features

- Predict prices with `/api/predict`
- Health check via `/api/`
- Rate limiting & custom error handling
- Loads pre-trained model at startup

## 🧩 Project Structure

```css
house-price-predictor
 ├── controllers/ 
 ├── data/ 
 ├── lib/ 
 ├── routes/ 
 ├── schemas/ 
 ├── scripts/ 
 ├── main.py
 └── requirements.txt

```

## 🧠 Model Details

A `LinearRegression` model from `scikit-learn` is trained using synthetic data and saved as a pickle file. Input features for the model:

1. Number of rooms (int)
2. Square footage (float)
3. Age of the house (float)
4. Location score (float, scale of 1-10)

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/melos-simeneh/house-price-api.git
cd house-price-api
```

### 2. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Train and Save the Model

```bash
python scripts/train_model.py
```

### 4. Run the API

```bash
uvicorn main:app --reload
```

Access the API at:

- [http://127.0.0.1:8000](http://127.0.0.1:8000) (API)
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Interactive Docs)
- [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) (Alternative Docs)

## 🚀 Deployment

### 🐳 Docker

You can containerize and run the API using Docker.

**1. Build the Docker image:**

```bash
docker build -t house-price-api .
```

This will build the Docker image and tag it as house-price-api.

**2. Run the container:**

```bash
docker run -d -p 8000:8000 house-price-api
```

This runs the container in detached mode (`-d`) and maps port 8000 on your local machine to port 8000 inside the container. The API will be accessible at [http://localhost:8000](http://localhost:8000).

### ☁️ Cloud Deployment

Easily deploy the House Price Prediction API to popular cloud platforms with just a few clicks! Select one of the following deployment options:

[![Deploy to Heroku](https://img.shields.io/badge/Deploy_to-Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://heroku.com/deploy?template=https://github.com/yourusername/house-price-api)
[![Deploy on Railway](https://img.shields.io/badge/Deploy_to-Railway-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)](https://railway.app/new/template?template=https://github.com/yourusername/house-price-api)
[![Deploy to Render](https://img.shields.io/badge/Deploy_to-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com/deploy?repo=https://github.com/yourusername/house-price-api)

## 📮 API Endpoints

### Health Check

```http
GET /api/
```

**Response:**

```json
{
  "success": true,
  "message": "House Price Prediction API is ready"
}
```

### Predict Price

```http
POST /api/predict
```

**Request Body:**

```json
{
  "rooms": 3,
  "square_footage": 1500,
  "age": 10,
  "location_score": 8
}
```

**Response:**

```json
{
  "success": true,
  "currency": "USD",
  "predicted_price": "$452,000.00"
}
```

## 🛡️ Error Handling

- Custom handlers for:
- Rate limit exceeded
- Request validation errors
- HTTP exceptions
- General server errors

## ⏱️ Rate Limiting

The `/predict` endpoint is rate-limited using middleware in `lib/rate_limiter.py` to prevent abuse.

## 📬 Contact

Made with 💚 by **MELOS**

For questions or suggestions, open an issue or contact [melos.simeneh@gmail.com](mailto:melos.simeneh@gmail.com).
.
