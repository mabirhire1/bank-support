import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")
BASE_API_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

# ── Validate environment variables ──
if not API_KEY:
    print("ERROR: OPENROUTER_API_KEY is not set. Please add it to your .env file.")
    sys.exit(1)

if not MODEL_NAME:
    print("ERROR: MODEL_NAME is not set. Please add it to your .env file.")
    sys.exit(1)


def call_api(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
    }

    response = requests.post(BASE_API_URL, headers=HEADERS, json=payload)
    result = response.json()

    if response.status_code != 200:
        print("Error Response:", result)
        raise ValueError(result.get("error", {}).get("message", "Unknown error"))

    return result["choices"][0]["message"]["content"].strip()


def prompt_chain(customer_complaint: str):
    # Step 1: Extract intent
    step1_prompt = f"""
    You are a customer care agent for a bank. Determine the intent of this complaint in a maximum of 3 or 4 words.
    Complaint: {customer_complaint}
    """
    step1_response = call_api(step1_prompt)
    print("Customer intent: ", step1_response)

    # Step 2: Suggest categories
    step2_prompt = f"""
    Suggest one or more categories that might apply to this complaint and return in JSON format.
    Complaint: {customer_complaint}
    """
    step2_response = call_api(step2_prompt)
    print("Suggested categories: ", step2_response)

    # Step 3: Determine final category
    categories = ["account opening", "billing issue", "account access", "transaction inquiry", "card services", "account statement", "loan inquiry", "general information"]

    step3_prompt = f"""
    Based on these categories: {", ".join(categories)},
    determine which category best handles this complaint.
    Complaint: {customer_complaint}
    """
    step3_response = call_api(step3_prompt)
    print("Category: ", step3_response)

    # Step 4: Extract key information
    step4_prompt = f"""
    Extract useful details from the complaint (e.g., amount, date, transaction ID, etc.) and return in JSON format.
    Complaint: {customer_complaint}
    """
    step4_response = call_api(step4_prompt)
    print("Extracted information: ", step4_response)

    # Step 5: Compose friendly response
    step5_prompt = f"""
    Compose a short, friendly, and professional response to the customer.
    Extracted information: {step4_response}
    Category: {step3_response}
    Original complaint: {customer_complaint}
    """
    step5_response = call_api(step5_prompt)
    print("Final response: ", step5_response)

    return step5_response


# Run
if __name__ == "__main__":
    print("Customer Support AI Agent")
    complaint = input("Enter customer complaint: ").strip()
    if not complaint:
        print("Error: Complaint cannot be empty.")
        sys.exit(1)

    prompt_chain(complaint)
