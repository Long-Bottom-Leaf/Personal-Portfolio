package LinkedList;

import java.util.LinkedList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        SingleLinkedList singleLinkedList = new SingleLinkedList();
        singleLinkedList.insertLinkedList(1,0);
        singleLinkedList.insertLinkedList(2,1);
        singleLinkedList.insertLinkedList(3,2);
        singleLinkedList.insertLinkedList(4,3);

        singleLinkedList.traverseLinkedList();

        LinkedList<String> test = new LinkedList<>();

        // Testing
            // Traversal
            singleLinkedList.traverseLinkedList();

            // Search
            singleLinkedList.searchNode(3);
            singleLinkedList.searchNode(5);

            // Delete
            singleLinkedList.deleteNode(2);

        // See new list
        singleLinkedList.traverseLinkedList();
    }
}
