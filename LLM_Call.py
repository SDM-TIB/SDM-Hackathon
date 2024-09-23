import os
import requests

def call(prompt):
    """
    Sends the input prompt to the GPT-4 model via a direct HTTP POST request and returns the assistant's response.

    Parameters:
    - prompt (str): The user's input prompt.

    Returns:
    - str: The assistant's response generated by GPT-4.
    """
    # Retrieve the API key from an environment variable
    api_key = "API_KEY"
    if not api_key:
        raise ValueError("Error: The OpenAI API key is not set. Please set it as an environment variable 'OPENAI_API_KEY'.")

    # Set the request headers including the Authorization header with the API key
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    # Prepare the data payload
    data = {
        "model": "gpt-4",
        "temperature": 0,
        "messages": [
            {"role": "user", "content": prompt },
        ]
    }

    # Make the POST request to the OpenAI API endpoint
    try:
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the response JSON and extract the assistant's reply
        content = response.json()['choices'][0]['message']['content']
        return content

    except requests.exceptions.HTTPError as http_err:
        raise RuntimeError(f"HTTP error occurred: {http_err} - {response.text}")
    except Exception as err:
        raise RuntimeError(f"An error occurred: {err}")

# Example usage
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    try:
        reply = call(user_prompt)
        print("\nAssistant's response:")
        print(reply)
    except Exception as e:
        print(str(e))
