import requests
import json

def emotion_detector(text_to_analyze):
    # Handle blank input first
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Make POST request
    response = requests.post(url, json=myobj, headers=headers)

    # Handle Watson error response
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Convert response to dictionary
    response_dict = json.loads(response.text)

    # Access emotions safely
    emotions = response_dict.get('emotionPredictions', [])[0].get('emotion', {})

    anger = emotions.get('anger')
    disgust = emotions.get('disgust')
    fear = emotions.get('fear')
    joy = emotions.get('joy')
    sadness = emotions.get('sadness')

    # Find dominant emotion
    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Return structured dictionary
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
