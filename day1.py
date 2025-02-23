import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
from openai import OpenAI

load_dotenv()
openai = OpenAI()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Check the key

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")


def get_summary(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text()
    summary = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Summarize the following text: {text}",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return summary.choices[0].text