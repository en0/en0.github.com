Title: Data Structures: The Linked List
Date: 2017-08-30 19:58
Tags: DataStructures,LinkedList,C
Category: Programming
Slug: data-structures-the-linked-list
Author: Ian Laird
Summary: Exploring the characteristics and uses of linked lists.

<div class="banner">Data Structures: Linked Lists</div>

If someone where to ask you, "What is a linked list good for?" What would you
say? If you are like many developers, your response might be, "not much." We
would probably struggle to think of a situation in our career when we needed to
use one.

However, a linked list is not only a useful data structure, it is so often used
that we do not even notice it. From Deques to Stacks, it is used in situations
where fast insertion and removal is required. 

Let's take a brief look at the basic structure of a linked list to understand
how it works.

# The Basics

A linked list is a structure used to store an ordered set of data. Similar to
an array, the linked list can be used to store and access individual members of
a collection.

![image](/images/linked-list-visual-0.png){.full-line}

Each item, or node, in a linked list points the next node. If needed, a node
can also point to its predicessor. This is known as a doubly linked list. A
node will also contain some sort of data. This can be as simple as an integer,
something as complex as another structure, or pointers to other structures.
Really, the sky is the limit and the details depend on what problem you are
trying to solve.

# Characteristics of the Linked list

As with any other data structure, linked lists are good at some things and bad
at others. The characteristics of any data structure dictate the optimal use
cases. So, what are the characteristics of a linked list? We will go through
them one at a time.

## Dynamic Sizing

The most obvious advantage of a linked list (over an array) is that, unlike an
array, the members of a collection do not need to be stored next to each other
in memory.  An array requires blocks of contiguous memory. A linked list only
needs a reference to the next (and possibly the previous) node. This design
gives linked lists a characteristic of being dynamic. In other words, the size
of the collection can be easily altered during run-time.

__Let me explain__

Using a standard array, we (or the compiler) must define a contiguous block of
memory to store our data. As an example, we could use an array to store 100
integers. That is 400 bytes (assuming x86) of contiguous memory. There is no
issue with this. We have an insane amount of virtual address space available to
us (128 TB in windows 10). Finding 400 contiguous bytes, or even 4 billion
contiguous bytes is not a problem. But what happens when we fill up this array
and still have more values to store?

Now, I know what you are thinking: "In my language I cannot fill up an array.
It just gets bigger." You are right. Let's take it to the next step though and
ask the question, how does the array get bigger?

Many languages like Node, Python, and C#, can define an array of any size using
something called dynamic array. Dynamic arrays have their advantages, but their
use comes at a cost. When the data of a dynamic array exceeds its pre-allocated
space, it is resized. This is most often done by duplicating the entire array,
including addtional space for new values.

In our example, a system using dynamic arrays would lock a minimum of 804 bytes
of memory and ask the processor to copy all 400 bytes to the new memory
location. With 400 bytes this is not an issue. With 4 Billion bytes, though,
you can see where this is heading. While it might be easy to find 4G of
consecutive address space, it is no trivial task activly read and write over 8G
of memory on a system that might have only 4G of physical RAM.

In this situation, using a linked list would use more memory (overhead for
pointers to the next node) but would not require it all be mapped
simultaneously. Nor would it require the processor copy large blocks of memory.
It would simply allocate an additional 12 bytes of storage: 8 bytes for the
next pointer, and 4 bytes for the value, then put the location of this new node
in the next field of the last entry. Insertion time is constant.

## Fast Insertion and Deletion

As we just learned from the above section, insertion time is constant. It is
probably no surprise that deletion time is also constant. Just as adding a new
integer to our collection required an allocation and a pointer reference
update, a deletion only requires a pointer reference update and a
de-allocation. But this is not only true at the ends of a list. It is true
anywhere in the list.

```c
void insert_after(node *member, int value) {
    node *new_member = malloc(sizeof(node));
    new_member->value = value;
    new_member->next = member->next;
    member->next = new_member;
}
```

As you can see, a node can be added between two other nodes just as easily no
mater where it is in the list. This is different from an array where each
member below the point of insertion will need to be moved to make room for the
new value. An operation like that could be expensive.

```c
void array_insert_at(int value, int index, int *array, int length) {
    for(int i = length - 1; i > index; i--)
        array[i] = array[i - 1];
    array[index] = value;
}
```

## Space Efficient

Another characteristic of a linked list is space efficiency. This does not mean
that a linked list takes up the least amount of memory to store a collection of
values (it does not). It means that it does not waist any space and has minimal
overhead. If you have a collection of 50 integers, you are only using the space
needed to store 50 integers. You do not need to reserve additional space
because you plan to store more values. That space can simply be allocated when
needed.

```
LinkedList : 1->2->3
Array : [ 1 | 2 | 3 |   |   ]
```

## Linear search

One characteristic of the linked list that is less then exciting is that it is
not well suited for random access. A linked list has no way to directly access
a specific node at a random offset in a collection. The only option it has is
to do a linear search through the list and find the node being requested.

In addition, the linked list has no special facility to check membership of a
specific value. Once again, the list must be searched to find the answer.

As an example, if we want to get the 5th node in the list, we would have to
start at the head of the list and follow to the next node, and the next until
we have reached the 5th node. If we wanted to know if the value 400 was
contained in the list, we would have to start at the head and test each value
in turn until we find it.  Once again, the 4 billion members because
problematic.

This is NOT an issue in standard arrays. We can simply go to the offset of
a member in a constant time. If the array is sorted, we can use a binary search
to expedite membership tests. An array is also capable of performing a linear
search so linked lists hold no advantage in this area.


# Use Case

So, linked lists are good at fast insertion and fast removal of members, They
are space efficient and they are terrible at random access and membership
checks. With these characteristics in mind, what problems are linked lists
suited to solve?

## Stacks

A stack is an abstract data structure that can be used in a variety of
situations. From undo/redo tracking to syntax checking to returning to a
preempted workload, a stack is powerful. It is also quite simple - but why are
we talking about stacks?

There is more then one way to implement a stack but using a linked list is
simple, especially if your programming language already supplies a linked list.
If you insert and remove from only one end of a linked list, you effectively
have a stack. All that is missing is handing of exceptional cases such as
empty.

```c
node *head;

void push(int i) {
    node *n = malloc(sizeof(node));
    n->value = i;
    n->next = head
    head = n;
}

int pop() {
    int value = head->value;
    void *n = head;
    head = head->next
    free(n);
    return value;
}

int peek() {
    return head->value;
}
```

## Queues

A queue is another abstract data structure that is very similar to a stack. And
just like a stack, it offers solutions to many problems. Workload management,
rate limiting, turn based problems are just a few things that queues are good
at.

To implement a queue with a doubly linked list, simply write to one end and
remove from the other end. Once again, some exceptional condition handing would
be required.

```c
// Assume that head->next points to tail and tail->prev points to head.
node *head;
node *tail;

void enqueue(int i) {
    node *n = malloc(sizeof(node));
    n->value = i;
    n->next = head
    head->prev = n;
    head = n;
}

int dequeue() {
    int value = tail->value;
    node *n = tail->prev;
    free(tail);
    tail = n;
    return value;
}
```

# Conclusion

Linked lists are often overlooked. Although they solve similar problems as
arrays, they have strengths that arrays do not. Linked lists are well suited
to tasks that require quick add and remove where sequence is important but
would be a poor choice if you need to query or check membership of a large
collection.

As with any other data structure, it is useful to consider the positives and
the negative characteristics and how they might relate to your specific
problem.

# Other Thoughts

One more consideration regarding linked lists that I find intriguing: They are
the basis of understanding for many of the more complex data structures such as
Binary Search Trees, Heaps, and Graphs. Each of these structures keep a
reference to its neighbors the same way and it is simply how the data is
organized within the structure that gives it unique characteristics. A linked
list is nothing more then a simple tree in the say way a tree is a simple
graph.
