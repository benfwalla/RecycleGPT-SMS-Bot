import os
from flask import Flask, request
from replit import db
from twilio.rest import Client
from scripts.prompt_builder import answer_with_gpt_4

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():

  incoming_dict = {
    "from": request.values.get('From'),
    "to": request.values.get('To'),
    "body": request.values.get('Body'),
    "message_id": request.values.get('MessageSid')
  }
  
  user_num = str(incoming_dict['from'])
  client_num = str(incoming_dict['to'])

  # Curate GPT's response
  client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
  
  gpt_resp = answer_with_gpt_4(incoming_dict['body'], "data/co_recycling_data_with_embeddings.csv", user_num, os.getenv("OPENAI_API_KEY"))

  message = client.messages.create(
                              from_ = client_num,
                              body = gpt_resp,
                              to = user_num
                          )

  # LOGGING
  # Log user message in the DB. Check if the key (from number) exists
  if user_num in db.keys():
    # Append user and assistant message to the extend thread
    temp = db[user_num]
    temp.extend([{"role": "user", "content": incoming_dict['body']},
                 {"role": "assistant", "content": gpt_resp}])
    db[user_num] = temp
  else:
    # Instantiate new thread with the user and assistant message
    db[user_num] = [{"role": "user", "content": incoming_dict['body']},
                    {"role": "assistant", "content": gpt_resp}]
  
  print("Success!\nMessage SID: " + message.sid + " \nResponse: \n" + gpt_resp)
  return message.sid




if __name__ == '__main__':
  app.run(host='0.0.0.0')
