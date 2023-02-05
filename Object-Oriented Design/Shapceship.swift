public class Spaceship{
    // instance variables:
    public var CallSign: String
    private var _shieldStrength: int
    // methods:
    func fireMissile() -> String {
        return "pew!"
    }
    func reduceShield( amount: int){
        _shieldStrength -= amount;
    }
}

