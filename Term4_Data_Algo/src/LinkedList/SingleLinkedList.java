package LinkedList;

public class SingleLinkedList {
    public Node head;
    public Node tail;
    public int size;

    public Node createSingleLinkedList(int nodeValue) {
        Node node = new Node();
        node.next = null;
        node.value = nodeValue;

        head = node;
        tail = node;
        size = 1;

        return head;
    }

    // Insert Method
    public void insertLinkedList(int nodeValue, int location) {
        Node node = new Node();
        node.value = nodeValue;

        if (head == null) {
            createSingleLinkedList(nodeValue);
            return;

        } else if (location == 0) {
            node.next = head;
            head = node;

        } else if (location >= size) {
            node.next = null;
            tail.next = node;
            tail = node;

        } else {
            Node tempNode = head;
            int index = 0;

            while (index < location -1) {
                tempNode = tempNode.next;
                index++;
            }
            Node nextNode = tempNode.next;
            tempNode.next = node;
            node.next = nextNode;
        }

        size++;
    }

    // Traversing through a linked list
    public void traverseLinkedList() {
        if (head == null) {
            System.out.println("Linked list does not exist!");

        } else {
            Node tempNode = head;

            for (int i = 0; i < size; i++) {
                System.out.println(tempNode.value);

                if (i != size -1) {
                    System.out.println("->");
                }

                tempNode = tempNode.next;
            }
            System.out.println("\n");
        }
    }

    // Exercise 1: search for element and return boolean if exists, given a value
        public boolean searchNode(int nodeValue) {
            if (head == null) {
                System.out.println("The list does not exist!");
                return false;
            }

            Node tempNode = head;

            for (int i = 0; i < size; i++) {
                if (tempNode.value == nodeValue) {
                    System.out.println("Value " + nodeValue + " found at index " + i + ".");
                    return true;
                }

                tempNode = tempNode.next;
            }

            System.out.println("Value " + nodeValue + " not found in list!");
            return false;
        }

    // Exercise 2: Given a location, implement delete method
        public void deleteNode(int location) {
            if (head == null) {
                System.out.println("This list does not exist!");
                return;
            }

            // Delete first node
                if (location == 0) {
                    head = head.next;
                    size--;

                    // If list is then empty, ensure tail is null
                    if (size == 0) {
                        tail = null;
                    }

                    System.out.println("First node has been deleted!");
                    return;
                }

            // Delete tail or middle, both need to walk through list so they are grouped to avoid duplicate coding
                Node tempNode = head;
                int index = 0;

                while (index < location - 1) {
                    tempNode = tempNode.next;
                    index++;
                }

                // Delete last node, or in middle
                if (tempNode.next == tail) {
                    tempNode.next = null;
                    tail = tempNode;
                    size--;

                } else {
                    tempNode.next = tempNode.next.next;
                    size--;

                    System.out.println("Node at location " + location + " has been deleted!");
                }

        }
}
