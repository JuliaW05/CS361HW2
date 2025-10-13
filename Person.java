public class Person implements Comparable<Person> {
    private int age;
    private String lastName, firstName;

    public Person(String firstName, String lastName, int age){
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }

    public String getName(){
        return firstName + " " + lastName;
    }

    @Override
    public int compareTo(Person other){
        return Integer.compare(this.age, other.age);
    }

    public static void main(String[] args) {
        Person person1 = new Person("Julia", "Walkuska", 20);
        //Person person1 = new Person("Julia", "Walkuska", 25);
        //Person person1 = new Person("Julia", "Walkuska", 24);
        Person person2 = new Person("Albert", "John", 24);

        if (person1.compareTo(person2) < 0){
            System.out.println(person1.getName() + " is younger than " + person2.getName());
        } else if (person1.compareTo(person2) > 0){
            System.out.println(person1.getName() + " is older than " + person2.getName());
        } else {
            System.out.println("They are the same age");
        }
    }
}
