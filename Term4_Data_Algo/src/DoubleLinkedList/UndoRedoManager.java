package DoubleLinkedList;

/**
 * Implement an application that supports undo/redo functionality.
 * Uses a doubly linked list to maintain a sequence of states.
 *
 * Example:
 * State1 <-> State2 <-> State3 <-> State4 <-> State5
 */

public class UndoRedoManager<T> {

    // inner node class
        private class Node {
            private T state;
            private Node next;
            private Node previous;

            private Node(T state) {
                this.state = state;
            }
        }

    private Node currentState;

    // undo operation
        public T undo() {
            if (currentState == null) {
                System.out.println("No state to undo!");
                return null;
            }

            // check if at first state
            Node previousState = currentState.previous;

            if (previousState == null) {
                System.out.println("Reached the initial state!");

            } else {
                currentState = previousState;
            }

            return currentState.state;
        }

    // Redo operation
        public T redo() {
            if (currentState == null) {
                System.out.println("No state to redo");
                return null;
            }

            if (currentState.next == null) {
                System.out.println("No further state to redo");
            } else {
                currentState = currentState.next;
            }

            return currentState.state;
        }

    // perform an operation
        public void addState(T newState) {
            Node newNode = new Node(newState);

            // clear redo history, when a new state is added, the timeline branches, so it's important to clear
            // history so the program can run properly
            if (currentState != null && currentState.next != null) {
                currentState.next.previous = null;
                currentState.next = null;
            }

            newNode.previous = currentState;
            newNode.next = null;

            if (currentState != null) {
                currentState.next = newNode;
            }

            currentState = newNode;
        }

    // main app
        public static void main(String[] args) {
            UndoRedoManager<String> undoRedoManager = new UndoRedoManager<>();

            undoRedoManager.addState("State 1");
            undoRedoManager.addState("State 2");
            undoRedoManager.addState("State 3");
            undoRedoManager.addState("State 4");
            undoRedoManager.addState("State 5");

            System.out.println("Current: " + undoRedoManager.currentState.state);

            // undo tests
            undoRedoManager.undo();
            System.out.println("Current: " + undoRedoManager.currentState.state);

            undoRedoManager.undo();
            System.out.println("Current: " + undoRedoManager.currentState.state);

            undoRedoManager.undo();
            System.out.println("Current: " + undoRedoManager.currentState.state);

            undoRedoManager.undo();
            System.out.println("Current: " + undoRedoManager.currentState.state);

            undoRedoManager.undo();
            System.out.println("Current: " + undoRedoManager.currentState.state);

            // redo tests
            System.out.println("\n==== REDO ====");

            undoRedoManager.redo();
            System.out.println("Current: " + undoRedoManager.currentState.state);

            undoRedoManager.redo();
            System.out.println("Current: " + undoRedoManager.currentState.state);

            // add new state
            System.out.println("\n==== ADD NEW STATE AFTER UNDO ====");

            undoRedoManager.addState("State 6");
            System.out.println("Current: " + undoRedoManager.currentState.state);

            // attempt redo -- should fail
            undoRedoManager.redo();
        }
}