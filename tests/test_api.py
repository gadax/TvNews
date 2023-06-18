from fastapi import FastAPI
from fastapi.testclient import TestClient

from main import app


client = TestClient(app)

def test_ping_return_status():
	response = client.get("/ping")
	assert response.status_code == 200

def test_ping_return_body():
	response = client.get("/ping")
	assert response.json() == {"msg": "pong"}

def test_news_one():
	response = client.get("/news/1")
	assert response.json() == [[1,"2023-04-30 12:26:00",
	"VIDÉO - Sécheresse : la pluie peut-elle encore régler le problème ?",
	"https://www.tf1info.fr/environnement-ecologie/video-secheresse-la-pluie-peut-elle-encore-regler-le-probleme-2255634.html","TF1"
	]]