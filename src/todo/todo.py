class Todo:
    def __init__(self, id: int, name: str, status: str) -> None:
        self.id = id
        self.name = name
        self.status = status


# id - 1
# uuid
# cuid2


class TodoList:
    def __init__(self):
        self.todos: list[Todo] = []

    def add(self, name: str, status: str = "in_progress") -> Todo:
        new_todo = Todo(len(self.todos) + 1, name, status)
        self.todos.append(new_todo)

        return new_todo

    def done(self, id: int) -> Todo | None:
        for todo in self.todos:
            if todo.id == id:
                todo.status = "done"
                return todo

        return None

    def change_status(self, id: int, status: str) -> None:
        change_todo = None

        for todo in self.todos:
            if todo.id == id:
                change_todo = todo
                break

        if not change_todo:
            raise Exception(f"Todo not found: {id}")

        change_todo.status = status

    def remove(self, id: int) -> bool:
        for index, todo in enumerate(self.todos):
            if todo.id == id:
                del self.todos[index]
                return True

        return False


class UserService:
    def login(self):
        pass


class InvoiceService:
    def get_user_invoice(self, user_id: int):
        pass


class UserController:
    def __init__(self, user_service: UserService, invoice_service: InvoiceService):
        self.user_service = user_service
        self.invoice_service = invoice_service

    def login_endpoint(self, user_data):
        result = self.user_service.login(user_data["id"])

        if result:
            print("Odesli zpet html")
        else:
            raise Exception("Spatne heslo nebo email")
