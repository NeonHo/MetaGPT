import os
 
os.environ["http_proxy"] = "http://localhost:7897"
os.environ["https_proxy"] = "http://localhost:7897"

from openai import OpenAI

proxies = {
	"http://": "http://127.0.0.1:7897",
	"https://": "http://127.0.0.1:7897",
}
        
client = OpenAI(
    # base_url="https://72e61556c7234ec82638e469141589ba.api-forwards.com",
    api_key="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"
)

completion = client.chat.completions.create(
	model="gpt-3.5-turbo",
	messages=[
		{"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
		{"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
	]
)

print(completion.choices[0].message)