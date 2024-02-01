# Object-oriented programming (OOP) in Python Note
`Class` and `Object` are fundamental concepts in object-oriented programming.

## Principles of OOPs
- <h3>Inheritance</h3>
-  <h3>Polymorphisum</h3>
-  <h3>Encapsulation</h3>
- <h3>Abstraction</h3>


## Class (ক্লাস)
A class is a blueprint of object. (ক্লাস হল অবজেক্ট এর ব্লু প্রিন্ট।)<br>
 <br>

```python
Class Student:
    def __init__(self, name, rol):
        self.name = name
        self.roll = roll

    def info(self):
        print(f'Name: {self.name} Roll: {self.roll}')

```
- এখানে `Student` হল ক্লাস। <br>
- এখানে `def __init__(...):` হল `Student` ক্লাসের Constructor Method. যখন কোনো
ক্লাসের অবজেক্ট তৈরি করা হয়, তখন `__init__ method(Constructor Method)`  automatically কল হয় ।
- এবং `def __init__(self, name, rol):` এ `self` হল ওই ক্লাসের অবজেক্ট বা instance কে রেফার করে। `name, roll` হল ক্লাস parameter। 
- `def info(self):` হল সাধারণ মেথড । যা object বা instence এর informetion আউটপুট হিসাবে প্রিন্ট করে।  

## Object (অবজেক্ট)
An object is an instance of a class.(অবজেক্ট হল একটি ক্লাসের instance।)

```python
student1 = Student(name='Refat', roll=1)
student2 = Student(name='Jamil', roll=2)

student1.info()
student2.info()
```
- এখানে `student1, student2` হল `Student` ক্লাসের অবজেক্ট। যেখানে `name=` এ আর্গুমেন্ট হিসাবে string `Refat, Jamil` এবং `roll=` এ  integer `1, 2` data দেওয়া হয়েছে। 
- `student1.info()` এখানে student1 এর information আউটপুট হিসাবে প্রিন্ট করার জন্য  সাধারণ মেথড  `info()` কল করা হয়েছে। 

## Inheritance (ইনহেরিটেন্স)
Inheritance হলো Object-oriented programming একটি মেকানিজম যেখানে একটি class (Sub Class বা Child Class বা Derived class) অন্য একটি class (Super Class বা Parent Class বা Base class) থেকে বৈশিষ্ট্য এবং আচার ধারণ করে। <br>
সাধারণত দু প্রকারের ইনহেরিটেন্স থাকে:

1. <b>সিঙ্গল ইনহেরিটেন্স:</b> একটি সাবক্লাস শুধুমাত্র একটি সুপারক্লাস থেকে ইনহেরিট করে।
2. <b>মাল্টিপল ইনহেরিটেন্স:</b> একটি সাবক্লাস একেবারে একাধিক সুপারক্লাস থেকে ইনহেরিট করতে পারে।

```python
# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def view_name(self):
        print(f"Name: {self.name}")

# Derived class
class Dog(Animal):
   pass

animal_instance = Animal("Generic Animal")
dog_instance = Dog("Buddy")

animal_instance.view_name()  
dog_instance.view_name()

```
- এখানে `Animal` হলো বেস ক্লাস।
- `def __init__(self, name): `হলো কনস্ট্রাক্টর মেথড, যা অবজেক্ট তৈরি করার সময় অটোমেটিকভাবে কল হয়। এটি name এবং self হল অবজেক্টের নাম সংরক্ষণ করার জন্য।
- `def view_name(self):` হল একটি মেথড, যা অবজেক্টের নাম প্রদর্শন করে।

- `Dog` হল ডেরাইভড ক্লাস, যা `Animal` ক্লাস থেকে ইনহেরিট করেছে।
- `animal_instance` এবং `dog_instance` হল `Animal` এবং `Dog` ক্লাসের ইনস্ট্যান্স।
- `animal_instance.view_name()` এখানে `Animal` ক্লাসের ইনস্ট্যান্স তৈরি করার পর `view_name` মেথডটি কল করা হয়েছে এবং` "Name: Generic Animal"` আউটপুট হচ্ছে।
- `dog_instance.view_name()` এখানে `Dog` ক্লাসের ইনস্ট্যান্স তৈরি করার পর `Animal` ক্লাসের `view_name` মেথডটি কল করা হয়েছে এবং `"Name: Buddy"` আউটপুট হচ্ছে।

### Method Overriding
```python
class Dog(Animal):
    
    def view_name(self):
        print(f"Dog name is: {self.name}")
```
- `view_name` মেথড ওভাররাইড করা হয়েছে যাতে কুকুরের নাম প্রিন্ট করতে নতুন কোড `"Dog name is:"` যোগ করা যায়।

### Superclass Initialization
`super()` ফাংশনটি base class বোঝাতে ব্যবহৃত হয়। এটি sub class থেকে base class এর method গুলোকে কল করার অনুমতি দেয়।

```python
# Derived class
class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def view_dog_color(self):
        print(f"Color: {self.color}")

dog_instance = Dog("Buddy", "Blue")

dog_instance.view_dog_color()
```

- `class Dog(Animal):` ক্লাসের নিজস্ব কনস্ট্রাক্টর আছে যা বেস ক্লাসের কনস্ট্রাক্টরকে কল করে `super().__init__(name)` যাতে নাম এট্রিবিউট সেট হয় এবং একটি নতুন এট্রিবিউট `color` প্রস্তুত করে।
- `view_dog_color` মেথডটি কুকুরের রঙ প্রিন্ট করে।
### Access to Superclass Methods
You can access methods and attributes of the superclass using super().

```python
class Dog(Animal):
    def view_dog_name(self):
        super().view_name() 
```

### Multiple Inheritance
A class can inherit from more than one class. However, it can lead to complexities, and care should be taken to avoid ambiguity.

```python
class ChildClass(ParentClass1, ParentClass2):
    # Class definition
```