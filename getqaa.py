import time
import os
import sys

import pyautogui
import pyperclip
from playsound import playsound

import llmf
import notificationf



def resource_path(relative_path):
    """ 获取资源文件绝对路径 """
    try:
        # PyInstaller 创建临时文件夹，并将路径存储在 _MEIPASS 中
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

sound = resource_path('./sound/alarm.mp3')
def get_question_and_answer(APIkey,base_url,model, prompt):
    # 将选中的文本复制到剪贴板
    pyautogui.hotkey('ctrl', 'c')
    playsound(sound)
    time.sleep(0.5)  # 等待复制操作完成
    copied_text = pyperclip.paste()
    # print("选中的文本：" + copied_text)
    #在这判定是否有apikey
    if llmf.verify_APIkey(APIkey,base_url):
        message = llmf.answer_question(APIkey,base_url,model,prompt,copied_text)
        return copied_text, message
    else:
        notificationf.show_notification('error', '身份验证错误，请检查APIkey',url='http://127.0.0.1:1234/settings')

# 你叫啥