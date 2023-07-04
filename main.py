from app.utils import get_operations, get_sorted_operations, get_user_dats, get_execute_operation
from settings import OPERATION_PATH

operations = get_operations(OPERATION_PATH)
execute_operations = get_execute_operation(operations)
executed_sort_operations = get_sorted_operations(execute_operations)
print(get_user_dats(executed_sort_operations))
