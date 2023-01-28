class Queue{
    // create a container:
    // to store items = create a resizable array:
    var QueueArray = [String]()
    // Enqueue
    fun enqueue(item.String){
        self.queueArray.append(item) // adds items to top of the array.
    }
    // Dequeue
    fun dequeue()-> String?{
        if self.queueArray.last != nil {
            let lastString = self.queueArray.last
            self.queueArray.removelast()
            return lastString!

        }
        else{
            return nil
        }
    }
    // peek:
    func peek() -> String?{
        if self.queueArray.last != nil {
            return self.queueArray.last
        }
        else{
            return nil
        }
    }   
}

var myQueue= Queue()
myQueue.enqueue(item: "peggy")
myQueue.enqueue(item:"sss")
print(myQueue.peek()!)
print(myQueue.peek()!)
// myQueue.dequeue() error
var firstToleave = myQueue.dequeue()
print(myQueue.peek()!)
// NO indexing with quues. 
