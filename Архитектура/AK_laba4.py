import pymongo

# Create the client
client = pymongo.MongoClient('localhost', 27017)

# Connect to our database
db = client['SeriesDB']

# Fetch our series collection
film_collection = db['series']

def insert_document(collection, data):
    """ Функция для вставки документа в коллекцию и
возврата идентификатора документа.
    """
    return collection.insert_one(data).inserted_id

def find_document(collection, elements = None, multiple=False):
    """ Функция для извлечения одного или нескольких документов из предоставленной коллекции
 с использованием словаря, содержащего элементы документа.
    """
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)
    
def update_document(collection, query_elements, new_values):
    """ Function to update a single document in a collection.
    """
    collection.update_one(query_elements, {'$set': new_values})

def delete_document(collection, query):
    """ Function to delete a single document from a collection.
    """
    collection.delete_one(query)


inp = ""
while inp != "0":
    print("1. Посмотреть \n2. Добавить \n3. Изменить \n4. Удалить")
    inp = input("Введите цифру: ")
    print("\n")

    match inp:
        case "1":
            f = find_document(film_collection, multiple=True)
            id = 0
            for dick in f:
                print("id =",id)
                for key in list(dick)[1:]:
                    print(key, ":",dick[key])
                print("\n")
                id += 1

        case "2":
            inp1 = input("Введите название: ")
            inp2 = input("Введите холл: ")
            inp3 = input("Введите сеанс: ")

            data = {
                "name": inp1,
                "hall": inp2,
                "session": inp3
            }

            insert_document(film_collection, data)

        case "3":
            film_id = input("Какой фильм вы хотите изменить? Введите id: ")
            result = film_collection.find()[int(film_id)]
            inp1 = input("Что вы хотите изменить? \n1. Название\n2. Холл\n3. Сеанс\n4. Все/n Номер: ")           
            match inp1:
                case "1":
                    inp2 = input("Введите новое название: ")
                    data = {
                        "name": inp2,
                        "hall": result["hall"],
                        "session": result["session"]
                    }
                    update_document(film_collection, result, data)
                case "2":
                    inp2 = input("Введите новый холл: ")
                    data = {
                        "name": result["name"],
                        "hall": inp2,
                        "session": result["session"]
                    }
                    update_document(film_collection, result, data)
                case "3":
                    inp2 = input("Введите новый сеанс: ")
                    data = {
                        "name": result["name"],
                        "hall": result["hall"],
                        "session": inp2
                    }
                    update_document(film_collection, result, data)
                case "4":
                    inp2 = input("Введите новое название: ")
                    inp3 = input("Введите новый холл: ")
                    inp4 = input("Введите новый сеанс: ")
                    data = {
                        "name": inp2,
                        "hall": inp3,
                        "session": inp4
                    }
                    update_document(film_collection, result, data)

        case "4":
            film_id = input("Какой фильм вы хотите удалить? Введите id: ")
            result = film_collection.find()[int(film_id)]
            delete_document(film_collection, result)
            

                    

            