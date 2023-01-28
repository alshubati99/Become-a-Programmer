// Lined list:
public class LinkedLists{
    Node head;
    // Create Add method:
    public void add(int data){
        // Linked List is empty:
        if(this.head == null){
            this.head = new Node (data);} 
            else {
                // Lined list is not empty:
                Node NodeToAdd = new Node(data);
                NodeToAdd.next = this.head;
                this.head = NodeToAdd;
            }
        }
        public static void main(String[] args){
            LinkedLists myList= new LinkedLists();
            myList.add(11);
            myList.add(10);
            System.out.println(myList.head.data);
            System.out.println(myList.head.next.data);

        }
}
// Node:
class Node {
    int data;
    Node next;
    Node (int d) {this.data = d;}
}