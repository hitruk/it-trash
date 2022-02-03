
Удалить файл/директорию:

Удалить
1) все не скрытые файлы:
rm -f /path/directory/*
2) все файлы с расширением txt:
rm -f /path/directory/.txt
3) все нескрытые файлы и подкаталоги вместе со всем их содержимым:
rm -rf /path/directory/*
4) все скрытые файлы и каталоги из папки:
rm -rf /path/to/directory/{*,.*}
5) все файлы из папки, но не удалять ее подкаталоги:
rm -f /path/directory/{*,.*}

Добавить:
    https://itisgood.ru/2021/04/12/kak-udalit-vse-fajly-iz-kataloga-na-linux/
