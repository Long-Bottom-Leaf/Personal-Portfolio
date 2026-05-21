package AnimalShelter;

public class MainApp {
    public static void main(String[] args) {

        AnimalShelter shelter = new AnimalShelter();

        shelter.enqueue(new Dog("Rex"));
        shelter.enqueue(new Cat("Whiskers"));
        shelter.enqueue(new Dog("Banjo"));
        shelter.enqueue(new Cat("Mittens"));
        shelter.enqueue(new Dog("Kansas"));
        shelter.enqueue(new Cat("Luna"));

        shelter.printAnimals();

        System.out.println("Dequeue Any: " + shelter.dequeueAny().getName());
        System.out.println("Dequeue Dog: " + shelter.dequeueDog().getName());
        System.out.println("Dequeue Cat: " + shelter.dequeueCat().getName());

        shelter.printAnimals();
    }
}
