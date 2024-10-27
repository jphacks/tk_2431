from openai import OpenAI
client = OpenAI()

# List 10 fine-tuning jobs
for job in client.fine_tuning.jobs.list(limit=10):
    print(job)
    print("---")