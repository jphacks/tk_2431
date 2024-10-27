from openai import OpenAI
client = OpenAI()

# 学習データのアップロード
client.files.create(
  file=open("emotion.jsonl", "rb"),
  purpose="fine-tune"
)

# テストデータのアップロード(なくても良い)
#client.files.create(
#  file=open("../dataset/test.jsonl", "rb"),
#  purpose="fine-tune"
#)