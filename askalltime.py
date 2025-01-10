'''
1.实现热键AI问答功能
2.将历史记录通过网页可视化答功能
3.配置AI模型
'''
import threading

import keyboard

import getqaa
import notificationf
import modeldataf
import historydataf
import serverf

attserver = 'http://127.0.0.1:1234'
def t2():
    serverf.run()
thread2 = threading.Thread(target=t2)
thread2.start()

if not modeldataf.has_default_model():
    notificationf.show_notification('提示','请先配置AI模型',attserver+'/settings')
    while not modeldataf.has_default_model():
        continue



def main():
    default_model = modeldataf.get_default_model()
    apikey = default_model[4]
    model_name = default_model[2]
    base_url = default_model[3]
    prompt = default_model[5]
    question,answer = getqaa.get_question_and_answer(apikey,base_url,model_name,prompt)
    id = historydataf.add_history(question,answer)
    notificationf.show_notification(question,answer,url=attserver+'/history/'+str(id))



def t1():
    keyboard.add_hotkey('ctrl+q', main)
    keyboard.wait('esc')

thread1 = threading.Thread(target=t1)
thread1.start()


