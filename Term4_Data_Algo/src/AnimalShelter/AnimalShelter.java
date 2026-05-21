package AnimalShelter;

import java.util.LinkedList;
import java.util.Queue;

public class AnimalShelter {

    // initialize lists
    private Queue<Dog> dogs = new LinkedList<>();
    private Queue<Cat> cats = new LinkedList<>();
    private int order = 0;  // initial order

    // print animals in a readable format
    public void printAnimals() {
        System.out.println("\n---- Current Animals In Shelter ----");

        for (Dog dog : dogs) {
            System.out.println("Dog: " + dog);
        }

        for (Cat cat : cats) {
            System.out.println("Cat: " + cat);
        }

        System.out.println("--------------------------------");
    }

    // add animal
    public void enqueue(Animal animal) {
        animal.setOrder(order);
        order++;

        if (animal instanceof Dog) {
            dogs.add((Dog) animal);

        } else if (animal instanceof Cat) {
            cats.add((Cat) animal);
        }
    }

    // dequeue specific species
    public Dog dequeueDog() {
        return dogs.poll();
    }

    public Cat dequeueCat() {
        return cats.poll();
    }

    // oldest overall
    public Animal dequeueAny() {
        // if empty, remove the other
        if (dogs.isEmpty()) return dequeueCat();
        if (cats.isEmpty()) return dequeueDog();

        // look at head of queue
        Dog oldestDog = dogs.peek();
        Cat oldestCat = cats.peek();

        // compare and dequeue
        if (oldestDog.isOlder(oldestCat)) {
            return dequeueDog();

        } else {
            return dequeueCat();
        }
    }
}
