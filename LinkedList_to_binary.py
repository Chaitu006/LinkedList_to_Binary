# You can implement this function in Python by traversing the linked list from the head to the end, updating the decimal sum at each step.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def getNumber(head):
    decimal_sum = 0
    current_node = head
    while current_node:
        print(f"Current node data: {current_node.data}")

        decimal_sum = decimal_sum * 2 + current_node.data
        print(f"Updated decimal sum: {decimal_sum}")

        current_node = current_node.next

    return decimal_sum


# Sample input: 0 0 1 1 0 1 0
# Creating the linked list
head = Node(0)
head.next = Node(0)
head.next.next = Node(1)
head.next.next.next = Node(1)
head.next.next.next.next = Node(0)
head.next.next.next.next.next = Node(1)
head.next.next.next.next.next.next = Node(0)

# Call the function and print the result
final_result = getNumber(head)
print(f"The decimal equivalent of the binary number is: {final_result}")


# Complexity Analysis

# Time Complexity: O(n) -  The function traverses the linked list once, where n is the number of nodes

# Space Complexity: O(1) - Constant extra space is used.
