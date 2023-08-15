import pytest
from _pytest.fixtures import SubRequest

from todo import TodoList


@pytest.fixture()
def data_with_auth(request: SubRequest) -> tuple[float, float]:
    todo = request.param

    print("Prihlasuji se")

    yield todo

    print("Odhlasuji se")


@pytest.mark.parametrize(
    "data_with_auth",
    [
        ("Walk a dog", "idle"),
        pytest.param(("Go shopping", "in_progress"), id="Tohle bude jine"),
        ("Clean house", "done"),
    ],
    ids=str,
    indirect=["data_with_auth"],
)
def test_finished_todo_is_always_done(data_with_auth: tuple[str, str]):
    name, status = data_with_auth
    todo_list = TodoList()
    new_todo = todo_list.add(name, status)
    todo_list.done(new_todo.id)

    assert todo_list.todos[0].status == "done"
