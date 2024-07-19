##  Chat Demo

This is a example code for chat demo with gradio.

Install necessary packages:
```pip install gradio hyperbee```

demo.py file:
```python
from hyperbee import HyperBee
import gradio as gr
import os


client = HyperBee(
    api_key=os.environ["HYPERBEE_API_KEY"],
)


def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human})
        history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="hive", messages=history_openai_format, temperature=0.4, stream=True
    )

    partial_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            partial_message = partial_message + chunk.choices[0].delta.content
            yield partial_message

gr.ChatInterface(predict).launch(server_name="0.0.0.0", server_port=8080, share=True)
```

Run the demo.py file and open the browser with the link provided in the terminal.

`python demo.py`
