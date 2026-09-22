<<<<<<< HEAD
# step1:setup ollama medgamma
# step2:setup twilio calling api
# step3 :setup location
import ollama
import requests






def query_medgemma(prompt: str) -> str:
    """
    Calls MedGemma model with a therapist personality profile.
    Returns responses as an empathic mental health professional.
    """
    system_prompt = """You are Dr. Emily Hartman, a warm and experienced clinical psychologist. 
    Respond to patients with:

    1. Emotional attunement ("I can sense how difficult this must be...")
    2. Gentle normalization ("Many people feel this way when...")
    3. Practical guidance ("What sometimes helps is...")
    4. Strengths-focused support ("I notice how you're...")

    Key principles:
    - Never use brackets or labels
    - Blend elements seamlessly
    - Vary sentence structure
    - Use natural transitions
    - Mirror the user's language level
    - Always keep the conversation going by asking open ended questions to dive into the root cause of patients problem
    """
    
    try:
        response = ollama.chat(
            model='alibayram/medgemma:4b',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            options={
                'num_predict': 350,  # Slightly higher for structured responses
                'temperature': 0.7,  # Balanced creativity/accuracy
                'top_p': 0.9        # For diverse but relevant responses
            }
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"I'm having technical difficulties, but I want you to know your feelings matter. Please try again shortly."


#a = query_medgemma("i feel anxious all the time")
#print(a)







import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXOTEL_API_KEY")
API_TOKEN = os.getenv("EXOTEL_API_TOKEN")
SID = os.getenv("EXOTEL_SID")
EXOTEL_NUMBER = os.getenv("EXOTEL_NUMBER")


# print("SID:", SID)
# print("API KEY:", API_KEY)
# print("TOKEN EXISTS:", bool(API_TOKEN))
# print("EXOTEL NUMBER:", EXOTEL_NUMBER)


def make_call(emergency_number):

    url = f"https://api.in.exotel.com/v1/Accounts/{SID}/Calls/connect"
    data = {
        "From": emergency_number,
        "CallerId": EXOTEL_NUMBER,
        "CallType": "trans",
        "Url": "YOUR_EXOTEL_FLOW_URL"
    }

    response = requests.post(
        url,
        data=data,
        auth=(API_KEY, API_TOKEN)
    )

    print(response.status_code)
    print(response.text)

    return response


=======
# step1:setup ollama medgamma
# step2:setup twilio calling api
# step3 :setup location
import ollama
import requests






def query_medgemma(prompt: str) -> str:
    """
    Calls MedGemma model with a therapist personality profile.
    Returns responses as an empathic mental health professional.
    """
    system_prompt = """You are Dr. Emily Hartman, a warm and experienced clinical psychologist. 
    Respond to patients with:

    1. Emotional attunement ("I can sense how difficult this must be...")
    2. Gentle normalization ("Many people feel this way when...")
    3. Practical guidance ("What sometimes helps is...")
    4. Strengths-focused support ("I notice how you're...")

    Key principles:
    - Never use brackets or labels
    - Blend elements seamlessly
    - Vary sentence structure
    - Use natural transitions
    - Mirror the user's language level
    - Always keep the conversation going by asking open ended questions to dive into the root cause of patients problem
    """
    
    try:
        response = ollama.chat(
            model='alibayram/medgemma:4b',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            options={
                'num_predict': 350,  # Slightly higher for structured responses
                'temperature': 0.7,  # Balanced creativity/accuracy
                'top_p': 0.9        # For diverse but relevant responses
            }
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"I'm having technical difficulties, but I want you to know your feelings matter. Please try again shortly."


#a = query_medgemma("i feel anxious all the time")
#print(a)







import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXOTEL_API_KEY")
API_TOKEN = os.getenv("EXOTEL_API_TOKEN")
SID = os.getenv("EXOTEL_SID")
EXOTEL_NUMBER = os.getenv("EXOTEL_NUMBER")


# print("SID:", SID)
# print("API KEY:", API_KEY)
# print("TOKEN EXISTS:", bool(API_TOKEN))
# print("EXOTEL NUMBER:", EXOTEL_NUMBER)


def make_call(emergency_number):

    url = f"https://api.in.exotel.com/v1/Accounts/{SID}/Calls/connect"
    data = {
        "From": emergency_number,
        "CallerId": EXOTEL_NUMBER,
        "CallType": "trans",
        "Url": "YOUR_EXOTEL_FLOW_URL"
    }

    response = requests.post(
        url,
        data=data,
        auth=(API_KEY, API_TOKEN)
    )

    print(response.status_code)
    print(response.text)

    return response


>>>>>>> 4e9915bfae2b9f3ca08054dd55fe9501f91e5ff3
