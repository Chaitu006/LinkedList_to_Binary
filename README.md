# LinkedList_to_Binary
LinkedList_to_Binary


You have to complete a function getNumber which receives a single argument , where  is the head of a linked list. Each node of the linked list contains an integer which is either  or . Placing all the integers present in the linked list in a order from left to right, forms a binary number. Return the decimal representation of the binary number to the base 10.

You have to add a function with the following definition

```
long long getNumber(Node *head) {
    // Complete this function
}
Input Format
```

First line of input will contain the length of linked list, .
In second line, there are  space separated integers, where each integer is either  or . The  value represents the data at the corresponding node.

Output Format

Print the decimal format of integer represented by list.

Constraints

Data at each node will be either  or 
The input can have preceding zeros.
Input/output will be handled by us. Don't print anything in the code.

Sample Input

```
7
0 0 1 1 0 1 0
``
`
Sample Output

```
26
```

Explanation

The given linked list is . The binary number formed is  and its decimal representation will be .