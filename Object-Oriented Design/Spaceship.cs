public class Spaceship{
    // instance variables:
    public String CallSign;
    private int shieldStrength;
    // methods:
    public String fireMissile(){
        return "pew!";
    }
    public void reduceShield(int amount){
        shieldStrength -= amount;
    }
}

