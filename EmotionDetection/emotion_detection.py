import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json=myobj, headers=header)

    # Si la respuesta no es exitosa, devuelve valores nulos
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    try:
        # Extrae las emociones del primer resultado
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        # Encuentra la emoción dominante
        dominant_emotion = max(emotions, key=emotions.get)

        # Agrega la emoción dominante al diccionario
        emotions['dominant_emotion'] = dominant_emotion

        return emotions
    except (KeyError, IndexError):
        # En caso de error, puedes retornar un diccionario vacío o con valores nulos
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }


