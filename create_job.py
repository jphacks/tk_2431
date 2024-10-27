from openai import OpenAI
client = OpenAI()

client.fine_tuning.jobs.create(
  training_file="FILEID",
  model="gpt-3.5-turbo-0125",
  suffix="emotion0_prediction",
  #validation_file="file-N3tJrLJW9bDwxB5YWnQCWVpz"
)