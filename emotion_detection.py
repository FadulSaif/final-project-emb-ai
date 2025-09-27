import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    # Make POST request
    response = requests.post(url, json=myobj, headers=headers)

    # Convert response to dictionary
    # Convert response to dictionary
    response_dict = json.loads(response.text)

    # Debug: print full response
    print(json.dumps(response_dict, indent=2))

    # Access the emotions from response (check exact structure of JSON)
    emotions = response_dict['emotionPredictions'][0]['emotion']

    # Grab only the required emotions
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    # Find the dominant emotion
    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Return in required format
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
