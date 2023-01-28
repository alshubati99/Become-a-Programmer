class Stack{
    // create a container:
    // to store items = create a resizable array:
    var stackArray = [String]()
    // push
    fun push(item.String){
        self.stackArray.append(item) // adds items to top of the array.
    }
    // pop:
    fun pop()-> String?{
        if self.stackArray.last != nil {
            let lastString = self.stackArray.last
            self.stackArray.removelast()
            return lastString!

        }
        else{
            return nil
        }
    }
    // peek:
    func peek() -> String?{
        if self.stackArray.last != nil {
            return self.stackArray.last
        }
        else{
            return nil
        }
    }   
}

var deck:Stack = Stack()
deck.push(item:"heart: Queen")
deck.push(item:"heart: King")
deck.push(item:"heart: Jack")
print(deck.peek()!)
print(deck.peek()!)
var firstItem = deck.pop()
var secondItem = deck.pop()
print(firstItem!)
print(secondItem!)


