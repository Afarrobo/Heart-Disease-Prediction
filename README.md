# Heart Disease Prediction API

FastAPI service serving a Random Forest classifier trained on the
[Kaggle Heart Disease dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset).
Dockerized and deployed on Render.

Seee Here What I build --  :)


**Live URL:** [https://MY-APP.onrender.com  ](https://heart-disease-api-53hv.onrender.com/)
**Swagger UI:** [https://MY-APP.onrender.com/docs](https://heart-disease-api-53hv.onrender.com/docs) 

## Project structure
```
app/            FastAPI code (main.py, schemas.py)
model/          heart_model.joblib
data/           heart.csv (not used at runtime)
train.py        training script
Dockerfile
docker-compose.yml
requirements.txt
```

## Train the model (optional, model is already included)
```bash
pip install -r requirements.txt
# place heart.csv in data/
python train.py
```

## Run with Docker
```bash
docker-compose build
docker-compose up
```
Open http://localhost:8000/docs

## Endpoints
- `GET /health` - service status
- `GET /info` - model type and feature list
- `POST /predict` - returns `heart_disease: true/false`

### Example
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"age":52,"sex":1,"cp":0,"trestbps":125,"chol":212,"fbs":0,"restecg":1,"thalach":168,"exang":0,"oldpeak":1.0,"slope":2,"ca":2,"thal":3}'
```

## Deploy on Render
New > Web Service > connect GitHub repo > Language: Docker > Root directory: repo root > Create.
