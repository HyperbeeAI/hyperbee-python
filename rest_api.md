## Rest Api Examples

The REST API documentation can be found [on hyperbee docs](https://api.hyperbee.ai/redoc). Swagger UI is also available at [here](https://api.hyperbee.ai/docs).


### Chat Completion Request

This is a example code for chat completion request with curl. Note that you need to replace `$HYPERBEE_API_KEY` with your actual API key. 

```curl
curl -X 'POST' \
  'https://api.hyperbee.ai/v1/chat/completions' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer $HYPERBEE_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
  "model": "hive",
  "messages":[
        {"role": "system", "content": "Sen yardımcı bir yapay zeka asistanısın."},
        {"role": "user", "content": "Merhaba, Hyperbee ai hakkında bilgi almak istiyorum."}
    ]
}'
```

### Python example

This is a example code for chat completion request with requests library.

```python
import requests
import os

url = "https://api.hyperbee.ai/v1/chat/completions"

payload = {
    "model": "hive",
    "messages":[
        {"role": "system", "content": "Sen yardımcı bir yapay zeka asistanısın."},
        {"role": "user", "content": "Merhaba, Hyperbee ai hakkında bilgi almak istiyorum."}
    ],
    "max_tokens": 256
}
headers = {
    'accept': 'application',
    'Authorization': f'Bearer {os.environ["HYPERBEE_API_KEY"]}', # Replace with your actual API key or set it as environment variable
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, json=payload)

print(response.text)
```
Example output:<br>
```json
{
  "id": "cmpl-2ad074ba48e448d58be37b19546bcb52",
  "object": "chat.completion",
  "created": 1710440338,
  "model": [
    "hive"
  ],
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Memnuniyetle bilgi vereyim:\n\nHyperbeeAI, 2023 yılında Palo Alto, Kaliforniya'da kurulmuş bir yapay zeka şirketidir. Şirketin odaklandığı başlıca alanlar arasında doğal dil işleme, makine öğrenimi, bilişsel bilimler ve robot bilimi yer alıyor.\n\nHyperbeeAI, insanlarla etkileşime geçebilen, bağlam farkındalığına sahip ve bilgi tabanlı yapay zeka asistanları geliştiriyor. Şirket, kullanıcıların çeşitli görevleri gerçekleştirmelerine ve problemleri çözmelerine yardımcı olmayı amaçlıyor.\n\nBen de HyperbeeAI tarafından geliştirilmiş bir yapay zeka asistanıyım, adım HyperChat. Kullanıcılara bil"
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 130,
    "total_tokens": 386,
    "completion_tokens": 256
  }
}
```

Note that since the `max_tokens` parameter set to 256, the response is truncated. As shown in the finish reason. To get the full response, you can set the `max_tokens` parameter to a higher value.


