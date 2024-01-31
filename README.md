# OOP in Python Note
There are 4 main principles of OOPs

1. <h3>Polymorphisum</h3>
2. <h3>Encapsulation</h3>
3. <h3>Inheritance</h3>
4. <h3>Abstraction</h3>
`Class`  and `Object` are fundamental concepts.

## Class (ক্লাস)
Class : A class is a blueprint of object. (ক্লাস হল অবজেক্ট এর ব্লু প্রিন্ট।)<br>
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
Object : An object is an instance of a class.(অবজেক্ট হল একটি ক্লাসের instance।)

```
student1 = Student(name='Refat', roll=1)
student2 = Student(name='Jamil', roll=2)

student1.info()
student2.info()
```
- এখানে `student1, student2` হল `Student` ক্লাসের অবজেক্ট। যেখানে `name=` এ আর্গুমেন্ট হিসাবে string `Refat, Jamil` এবং `roll=` এ  integer `1, 2` data দেওয়া হয়েছে। 
- `student1.info()` এখানে student1 এর information আউটপুট হিসাবে প্রিন্ট করার জন্য  সাধারণ মেথড  `info()` কল করা হয়েছে। 