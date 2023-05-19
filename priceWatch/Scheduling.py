import schedule
import time
from Notification import Notification

class Scheduling():
    
    def configureSchedule(self, toSchedule, name):
        # Terá que receber m = minuto, h = hora, d = dia
        notification = Notification()

        if toSchedule == 'm':
            schedule.every(5).seconds.do(notification.sendNotifications, name) # Aqui dentro do parênteses de do() fica a notificação
        elif toSchedule == 'h':
            schedule.every(60).minute.do(notification.sendNotifications, name) # Mesmo jeito do de cima
        elif toSchedule == 'd':
            schedule.every(1440).minute.do(notification.sendNotifications, name) # Este é o horário em que o script será executado
        else:
            print("Houve um erro ao escolher a frequência de verificação de preços!")

        while True:
            schedule.run_pending()
            time.sleep(1)
            