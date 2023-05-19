import schedule

class Schaduling():
    
    def configureSchedule(self, agendar):
        # Terá que receber m = minuto, h = hora, d = dia
        if agendar == 'm':
            schedule.every(1).minute.do() # Aqui dentro do parênteses de do() fica a tarefa que será executada
        if agendar == 'h':
            schedule.every(60).minute.do() # Mesmo jeito do de cima
        if agendar == 'd':
            schedule.every(1440).minute.do() # Este é o horário em que o script será executado
        else:
            print("Houve um erro ao escolher a frequência de verificação de preços!")
            