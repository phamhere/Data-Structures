Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
   O(n) since `enqueue` addes to the beginning of a list, therefore requiring the shifting of other elements to the right.
2. What is the runtime complexity of `dequeue`?
   O(1) since accessing the end of the list and deleting are constant time.
3. What is the runtime complexity of `len`?
   O(1) since we're simply getting the size variable, which has been incrementing/decrementing each time `enqueue` and `dequeue` have been called.

## Binary Search Tree

1. What is the runtime complexity of `insert`?
   O(log n) since we're cutting the tree in half every step we're comparing the current node's value to see where to put the new value.
2. What is the runtime complexity of `contains`?
   O(log n) since we're doing a binary search through the tree, halving the search every time we compare at a node.
3. What is the runtime complexity of `get_max`?
   O(log n) since we're only looking at the right most braches of the tree, which is halving the number of nodes at each node.

## Heap

1. What is the runtime complexity of `_bubble_up`?
   O(log n) because we're essentially halving the index for every loop we go through.
2. What is the runtime complexity of `_sift_down`?
   O(log n), similar to `_bubble_up`.
3. What is the runtime complexity of `insert`?
   O(log n) since uses `_bubble_up`.
4. What is the runtime complexity of `delete`?
   O(n), even though it uses `_sift_down`, it deletes at the beginning of the list, requiring all elements in the list to shift over to the left.
5. What is the runtime complexity of `get_max`?
   O(1) since it's just accessing a list element.

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
   O(1)
2. What is the runtime complexity of `ListNode.insert_before`?
   O(1)
3. What is the runtime complexity of `ListNode.delete`?
   O(1)
4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
   O(1)
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
   O(1)
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
   O(1)
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
   O(1)
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
   O(1)
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
   O(1)
10. What is the runtime complexity of `DoublyLinkedList.delete`?
    O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    The JS `Array.splice` method will at worst have an O(n) runtime complexity due to having upper elements to update indexes for if it's deleting. A dll's `delete` method will always be O(1) since it just has to connect the previous and next node together in a constant time runtime complexity, performing better in almost all circumstances compared to JS `Array.splice`.
