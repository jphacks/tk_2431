from openai import OpenAI
client = OpenAI()

for f in client.files.list():
    print("ファイル名： ", f.filename)
    print("ファイルID: ",f.id)
    print()