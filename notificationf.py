from winotify import Notification


def show_notification(title, message,url=''):
    toast = Notification(
        app_id="askalltime",  # 应用程序名称
        title=title,
        msg=message,
        duration="short",  # 通知显示时间
        launch=url
    )
    toast.show()