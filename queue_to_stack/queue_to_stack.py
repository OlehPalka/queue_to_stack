"""
Queue to stack converter.
"""

import copy
from arraystack import ArrayStack    # or from linkedstack import LinkedStack


def queue_to_stack(queue):
    """
    This function converts queue to stack.
    """
    queue_copy = copy.deepcopy(queue)
    convert_stack = ArrayStack()
    stack = ArrayStack()

    for _ in range(len(queue_copy)):
        stack.add(queue_copy.pop())

    for _ in range(len(stack)):
        convert_stack.add(stack.pop())

    return convert_stack
