import openai
from openai import OpenAI

def answer_question(APIkey,base_url,model, prompt,question):
    try:
        client = OpenAI(api_key=APIkey, base_url=base_url)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system",
                 "content": prompt},
                {"role": "user", "content":question},
            ],
            stream=False
        )
        message = response.choices[0].message.content

    except openai.APIConnectionError:
        message = "网络连接错误，请检查网络连接"
    except openai.AuthenticationError:
        message = "身份验证错误，请检查APIkey"
    return message

#验证APIkey是否有效
def verify_APIkey(APIkey,base_url):
    try:
        client = OpenAI(api_key=APIkey, base_url=base_url)
        client.models.list()
        return True
    except openai.APIConnectionError:
        return False
    except openai.AuthenticationError:
        return False

# print(verify_APIkey('sk-e9e39a45d57645478f75c6be912e7743','https://api.deepseek.com'))
# print(verify_APIkey('sk-hhGBWOa1io','https://dashscope.aliyuncs.com/compatible-mode/v1'))
# print(answer_question('sk-hhGBWOa1io','https://dashscope.aliyuncs.com/compatible-mode/v1','qwen2.5-7b-instruct','','你是谁'))