#styl imperatywny
arr = [1, 43, -35, 3, -1, 123, 0]

max_value = arr[0]
idx = 0
while idx <len(arr):
    if arr[idx] > max_value:
        max_value = arr[idx]
    idx +=1

print(max_value)

#styl deklaratywny
print(max(arr))

#SQL w dominującej części jest językiem deklaratywnym
#mówimy " zrób to" - ty wiesz jak najlepiej

#CRUD - 4 podstawowe operacje, które możemy chcieć wykonać na danych
#Create, Read, Update, Delete

"""

Deklaratywny SQL - komendy

DDL - Data Definition Language - nie na danych, ale na strukturach bazodanowych (baza danych, tabelki itp)
    CREATE | DROP | ALTER | TRUNCATE
    
DML - Data Modification Language - instrukcje na danych - zmienia stan bazy, po ich wykonaniu dane 
        w bazie się nie zmieniają
    INSERT (C) | UPDATE (U) | DELETE (D)
    
DQL - Data Query Language - wydzielony
    SELECT (R)
    
DCL - Data Control Language
    GRANT | REVOKE
    
TCL - Transaction Control Language
    COMMIT | ROLLBACK | SAVE POINT
    
"""
