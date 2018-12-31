# MODUŁY TIMIE I DATE_TIME

import time
import datetime

# print("START")
#
# czas = time.time()
# czas2 = time.time()
# czas3 = time.time()
# print(czas)
# time.sleep(2)
# time.time()-czas
# elapsed = time.time()-czas
# print(elapsed)
# print("STOP")
#
# while True:         #PETLA, KTORA CO 2 SEKUNDY WYSWIETLA KOMUNIKAT
#     if time.time()-czas>2:
#         print("2 sekundy")
#         czas=time.time()
#
#     if time.time()-czas2 >1: #druga petla WYSWIETLA KOMUNIKAT CO 1 SEKUNDE
#         print("1 sekunda")
#         czas2=time.time()
#
#     if time.time()-czas3>5:
#         break


# PODAWANIE AKTUALNEJ GODZINY

teraz = datetime.datetime.now()
print(str(teraz.hour)+":"+str(teraz.date()))
print(teraz.strftime("%H:%M %d/%m/%Y"))
