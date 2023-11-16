from dotenv import load_dotenv
import openai
import os

def generate_content_info_prompt(content_type, content_genre, content_summary, target_audience, highlight):
    # Construct a message for the conversation with ChatGPT
    message = f"Generate content information for a {content_type} in the {content_genre} genre. Provide a one-sentence summary of the {content_type}, identify the target audience, and highlight {highlight} in the {content_type}."
    return message

def get_content_info(content_type, content_genre, content_summary, target_audience, highlight):
    # Load OpenAI API key from .env file
    load_dotenv()
    openai.api_key = os.environ["OPENAI_API_KEY"]

    # Construct a message for the conversation with OpenAI
    message = generate_content_info_prompt(content_type, content_genre, content_summary, target_audience, highlight)

    # Set up ChatCompletion request parameters
    chat_request_kwargs = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "I want you to generate the following content information:"},
            {"role": "user", "content": message}
        ],
        "temperature": 0.5,
        "max_tokens": 1500  # Adjust max_tokens as needed
    }

    # Request information generation from OpenAI
    try:
        response = openai.ChatCompletion.create(**chat_request_kwargs)
    except openai.error.RateLimitError as e:
        return f"Error from OpenAI: {e}"

    # Extract and return the generated content information
    generated_info = response.choices[0].message["content"]

    # Extract keywords from the generated information
    keywords = extract_keywords(generated_info)

    return keywords

def extract_keywords(generated_info):
    # Implement your logic to extract keywords from the generated information
    # For simplicity, let's assume keywords are space-separated in the generated info
    return generated_info.split()

if __name__ == "__main__":
    content_type = input("1) What kind of content is this? (Inputs like video, photo, text, book): ")
    content_genre = input(f"2) What genre is your {content_type}? ")
    content_summary = input(f"3) Give a one-sentence summary of what your {content_type} has: ")
    target_audience = input("4) What is the target audience? ")
    highlight = input("5) What is one thing you want to highlight in this content? ")

    generated_keywords = get_content_info(content_type, content_genre, content_summary, target_audience, highlight)

    print("Generated Keywords:", generated_keywords)
