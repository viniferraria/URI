def _bino_atraso_(horas, minutos):
    atraso = 0
    if horas < 7 or horas > 9:
      atraso = 0

    elif horas == 7 and minutos > 0:
      atraso = minutos

    elif 7 < horas <= 9:
      atraso = minutos+60*(horas-7)

    return ("Atraso maximo: %d" % atraso)


while True:
  try:
    hora, minu = map(int, input().split(":")[:2])
    print(_bino_atraso_(hora, minu))
  except EOFError:
    break
