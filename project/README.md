# Приложение Mountain

Данное приложение предназначено для ведения базы горных перевалов, которая пополняется туристами.

Этап разработки REST API:

1. Создание базы данных, разработка класса по работе с БД и один метод для REST API;
2. Разработать еще трех методов для REST API;
3. Тестирование кода, подготовка документации.

	
Example Value
Model
[Mountain{
beauty_title	Beauty titlestring
title: Beauty title
maxLength: 64
minLength: 1
x-nullable: true
title	Titlestring
title: Title
maxLength: 255
minLength: 1
x-nullable: true
other_titles	Other titlesstring
title: Other titles
maxLength: 255
minLength: 1
x-nullable: true
connect	Connectstring
title: Connect
maxLength: 255
minLength: 1
x-nullable: true
add_time	Add timestring($date-time)
title: Add time
readOnly: true
user*	User{
email*	Email[...]
phone*	Phone[...]
fam*	Fam[...]
name*	Name[...]
otc*	Otc[...]
 
}
level*	Level{
winter	Winter[...]
spring	Spring[...]
summer	Summer[...]
autumn	Autumn[...]
 
}
coords*	Coords{
latitude*	Latitude[...]
longitude*	Longitude[...]
height*	Height[...]
 
}
status	Statusstring
title: Status
Enum:
[ NEW, PEN, ACC, REJ ]
imagesofmountains*	[
uniqueItems: true
string($uri)]
 
}]