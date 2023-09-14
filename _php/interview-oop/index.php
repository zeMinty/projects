<?php
class Person {
	public $fname;
	public $lname;
	public $s;
	public $age;

	public function __construct($fname, $lname, $age){
		$this->fname = $fname;
		$this->lname = $lname;
		$this->s = $s;
		$this->age = $age;
	}

	public function introduce(){
		return 'Hello, I am ' . $this->fname . ' ' . $this->lname . ". I'm " . $this->age . $this->s;
	}

	public function saySecret(){
		return 'My secret is ' . $this->fname;
	}
}

$john = new Person('Johaness', 'Kempler', 25, 'Loving books', 1 , 1);

echo $john->introduce();
// echo $john->lname;
echo $john->saySecret();
?>