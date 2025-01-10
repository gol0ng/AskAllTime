# AskAllTime
一个类似于划词翻译的实时AI问答软件
# 项目展示
在运行项目以后，即可选中文本并按下`ctrl+q`去运用AI搜索，如果您是第一次运行项目会要求填写AI的APIkey等信息，正确填写后方可开始问答。
问答结果会以弹窗形式出现，点击弹窗可以跳转到浏览器更好的观看你的搜索记录
按下`ctrl+q`时会有提示音，提醒你已经开始搜索
# 打包方式
安装`pyinstaller`并运行`pyinstaller --add-data "templates/index.html;templates" --add-data "templates/detail.html;templates" --add-data "templates/settings.html;templates" --add-data "templates/addmodel.html;templates" --add-data "static/style.css;static" --add-data "templates/updatemodel.html;templates" --add-data "sound/alarm.mp3;sound" --onefile --noconsole .\askalltime.py`
