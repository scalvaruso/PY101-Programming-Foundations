# Alyssa was asked to write an implementation of a rolling buffer.
# You can add and remove elements from a rolling buffer.
# However, once the buffer becomes full, any new elements will displace the oldest elements in the buffer.
# She wrote two implementations of the code for adding elements to the buffer:

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# My Solution

# The first function (add_to_rolling_buffer1) mutates the original list represented by buffer.
# The second function (add_to_rolling_buffer2) does not mutate the original list,
# but instead creates a new list and assigns it to buffer, whose value ultimately gets returned by the function.

# Launch School Solution
