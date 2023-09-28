

import wikipedia

# Поиск с учетом ошибок и возврат первой статьи
def search(name):
    return wikipedia.search(wikipedia.suggest(name))

# Извлечение резюме
def getSummary(name):
    return wikipedia.summary(search(name))

# Получение статьи как объекта
def getPage(name):
    return wikipedia.page(search(name))

# Получение названия статьи
def getTitle(name):
    return getPage(name).title

# Получение содержания статьи
def getContent(name):
    return getPage(name).content

# Получение ссылки на статью
def getUrl(name):
    return getPage(name).url

