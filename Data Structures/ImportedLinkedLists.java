import java.util.LinkedList;

public class ImportedLinkedLists {
    private static boolean add;

    /**
     * @param args
     */
    public static void main(String[] args){
        final LinkedList travelBucketList = new LinkedList();
        // Add items:
        add = travelBucketList.add("S, G");
        travelBucketList.addFirst("B, E");        
        travelBucketList.addLast("B, E");        
        travelBucketList.addFirst("B, E");
        System.out.println(travelBucketList);   
        // Access items:
        System.out.println(travelBucketList.get(2));  
        System.out.println(travelBucketList.getFirst()); 
        // Search items:
        System.out.println(travelBucketList.contains("B, E"));
        // Remove items:
        travelBucketList.removeFirst();
        travelBucketList.removeLast();
        System.out.println(travelBucketList);

        // You can remove items by object or index.

    }   
}
