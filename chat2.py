from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="FINETUNE-MODEL-ID",
    messages=[
        {"role": "user", "content": "あなたは優秀な心理カウンセラーです。事象に関してその人が持つ感情分析をします。旅行に行く。"},
    ],
    temperature=0.7,
    max_tokens=2000,
    top_p=0.95,
)

print(response.choices[0].message.content)
