public class Dog{
  private long AgeDog = 0;
  private long Weight = 0;
  private String Name = "";

  public long getAgeDog(){
    return this.AgeDog;
  }
  public void setAgeDog(long AgeDog){
    this.AgeDog = AgeDog;
  }
  public long getWeight(){
    return this.Weight;
  }
  public void setWeight(long Weight){
    this.Weight = Weight;
  }
  public String getName(){
    return this.Name;
  }
  public void setName(String Name){
    this.Name = Name;
  }

  // to test:
  public static void main(String[] args){
    Dog doge = new Dog();
    doge.setName("Doge");
    doge.setAgeDog(12);
    
    System.out.println(doge.getName()+" is "+doge.getAgeDog()+" years old.");
  }
}

