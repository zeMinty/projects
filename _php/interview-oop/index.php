<?php
class Person {
	public $fname;
	public $lname;
	public $age;

	public function __construct($fname, $lname, $age){
		$this->fname = $fname;
		$this->lname = $lname;
		$this->age = $age;
	}

	public function introduce(){
		return 'Hello, I am ' . $this->fname . ' ' . $this->lname . ". I'm " . $this->age;
	}
}

$john = new Person('Johaness', 'Kempler', 25);

echo $john->introduce();
?>