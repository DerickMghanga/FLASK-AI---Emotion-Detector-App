import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    #print(response)
    formatedResponse = json.loads(response.text)
    #emotions dict
    emotions = formatedResponse['emotionPredictions'][0]['emotion']
    #emotions
    anger = formatedResponse['emotionPredictions'][0]['emotion']['anger']
    disgust = formatedResponse['emotionPredictions'][0]['emotion']['disgust']
    fear = formatedResponse['emotionPredictions'][0]['emotion']['fear']
    joy = formatedResponse['emotionPredictions'][0]['emotion']['joy']
    sadness = formatedResponse['emotionPredictions'][0]['emotion']['sadness']
    dominant = max([anger, disgust, fear, joy, sadness])

    dominant_emotion = ''
    for key, value in emotions.items():
        if emotions[key] == dominant:
            dominant_emotion = key

    return {'anger':anger, 'disgust':disgust, 'fear':fear, 'joy':joy, 
    'sadness':sadness, 'dominant_emotion': dominant_emotion}