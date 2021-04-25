"""
Stack to queue converter.
git repo - https://github.com/OlehPalka/queue_to_stack
"""
import copy
from arrayqueue import ArrayQueue   # or from linkedqueue import LinkedQueue


def stack_to_queue(stack):
    """
    This function returns queue from stack.
    """
    stack_copy = copy.deepcopy(stack)
    queue = ArrayQueue()
    stack_lenth = len(stack_copy)

    for _ in range(stack_lenth):
        queue.add(stack_copy.pop())

    return queue
