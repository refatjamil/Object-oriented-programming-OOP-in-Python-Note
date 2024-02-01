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

```
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
```
student1 = Student(name='Refat', roll=1)
student2 = Student(name='Jamil', roll=2)

student1.info()
student2.info()
```
- এখানে `student1, student2` হল `Student` ক্লাসের অবজেক্ট। যেখানে `name=` এ আর্গুমেন্ট হিসাবে string `Refat, Jamil` এবং `roll=` এ  integer `1, 2` data দেওয়া হয়েছে। 
- `student1.info()` এখানে student1 এর information আউটপুট হিসাবে প্রিন্ট করার জন্য  সাধারণ মেথড  `info()` কল করা হয়েছে। 

## Inheritance (ইনহেরিটেন্স)
Inheritance হলো Object-oriented programming একটি মেকানিজম যেখানে একটি class (Sub Class বা Child Class) অন্য একটি class (Super Class বা Parent Class) থেকে বৈশিষ্ট্য এবং আচার ধারণ করে। <br>
সাধারণত দু প্রকারের ইনহেরিটেন্স থাকে:

1. <b>সিঙ্গল ইনহেরিটেন্স:</b> একটি সাবক্লাস শুধুমাত্র একটি সুপারক্লাস থেকে ইনহেরিট করে।
2. <b>মাল্টিপল ইনহেরিটেন্স:</b> একটি সাবক্লাস একেবারে একাধিক সুপারক্লাস থেকে ইনহেরিট করতে পারে।

```
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

animal_instance = Animal("Generic Animal")
dog_instance = Dog("Buddy")

animal_instance.speak()  # Output: Generic Animal makes a sound
dog_instance.speak()     # Output: Buddy barks

```
- `Class Animal:` একটি কন্সট্রাক্টর `(__init__)` method এবং একটি `def speak` method সহ একটি (Super Class বা Parent Class)।
- `Class Dog(Animal):` লেখার মাধ্যমে Animal class কে Dog class এ inherit করে। ফলে Animal class এর সকল বৈশিষ্ট্য Dog class পায়। 