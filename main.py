title = input('enter your title: ')
description = input('enter a description: ')
todolist = []
todo = {
	"title": title,
	"description": description,
	'isCompleted': False
}
todolist.append(todo)
print('This is my daily accomplishment')
print(todolist)