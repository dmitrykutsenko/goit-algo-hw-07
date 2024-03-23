# Максимальне та Мінімальне значення в ДДП
from collections import namedtuple

# Опис вузла двійкового дерева
Node = namedtuple("Node", ["data", "left", "right"])

# Перетворення словника в двійкове дерево
def to_tree(data):
    if data is None:
        return None
    else:
        return Node(data["data"], to_tree(data["left"]), to_tree(data["right"]))


# Функція для знаходження максимального значення
def find_max(root):
    # Якщо дерево порожнє, повертаємо None
    if root is None:
        return None

    # Переходимо праворуч, поки не знайдемо вузол без правого дочірнього
    while root.right is not None:
        root = root.right

    # Максимальне значення - це значення в цьому вузлі
    return root.data


def find_min(root):
    # Якщо дерево порожнє, повертаємо None
    if root is None:
        return None

    # Переходимо ліворуч, поки не знайдемо вузол без лівого дочірнього
    while root.left is not None:
        root = root.left

    # Мінімальне значення - це значення в цьому вузлі
    return root.data


def calc_sum(root):
    # Якщо дерево порожнє, повертаємо None
    if root is None:
        return 0
  
    # тут нам згодиться рекурсія
    return root.data + calc_sum(root.left) + calc_sum(root.right)


# Приклад двійкового дерева
tree_data = {
  "data": 15,
  "left": {
    "data": 10,
    "left": {
      "data": 5,
      "left": {
        "data": 2,
        "left": None,
        "right": None
      },
      "right": {
        "data": 7,
        "left": None,
        "right": None
      }
    },
    "right": {
      "data": 12,
      "left": None,
      "right": None
    }
  },
  "right": {
    "data": 20,
    "left": {
      "data": 17,
      "left": None,
      "right": None
    },
    "right": {
      "data": 25,
      "left": {
        "data": 22,
        "left": None,
        "right": None
      },
      "right": {
        "data": 30,
        "left": None,
        "right": None
      }
    }
  }
}


# Створення дерева
tree = to_tree(tree_data)

# Знаходження максимального значення
max_value = find_max(tree)
print(f"Максимальне значення: {max_value}")

# Знаходження мінімального значення
min_value = find_min(tree)
print(f"Мінімальне значення: {min_value}")

# Знаходження суми всіх значень
sum_of_values = calc_sum(tree)
print(f"Сума всіх значень: {sum_of_values}")

