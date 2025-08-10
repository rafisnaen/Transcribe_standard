from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-pro" ,
    contents="what is data scientist ?"
)

print(response.text)