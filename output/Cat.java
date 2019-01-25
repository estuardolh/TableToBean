public class Cat {
  private String id_cat;
  private String age;

  public Cat(String id_cat, String age){
    this.id_cat = id_cat;
    this.age = age;
  }

  public String getIdCat(){
    return this.id_cat;
  }

  public void setIdCat(String id_cat){
    this.id_cat = id_cat;
  }

  public String getAge(){
    return this.age;
  }

  public void setAge(String age){
    this.age = age;
  }
}
