import os
from transliterate import translit, get_available_language_codes
a=(os.listdir())
for i in a:                      # Проходимся по списку файлов
    b=(i[0:i.rindex('.')])       # строка до точки
    c=(i[i.rindex('.'):])        # строка после точки
    b=translit(b,'ru')+c         # объединяем транслитеральную строку с расширением
    os.rename(i,b)               # переименовываем файл
    
    

    

    


