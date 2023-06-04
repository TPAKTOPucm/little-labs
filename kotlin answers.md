## Коллекции. Общий обзор
### Типы коллекций
• List (список) - упорядоченная коллекция, в которой к элементам можно 
обращаться по индексам — целым числам, отражающим положение элементов в 
коллекции. Идентичные элементы (дубликаты) могут встречаться в списке более 
одного раза. Примером списка является предложение: это группа слов, их 
порядок важен, и они могут повторяться.

• Set (множество) - коллекция уникальных элементов. Отражает математическую 
абстракцию множества: группа объектов без повторов. Как правило, порядок 
расположения элементов здесь не имеет значения. Примером множества является 
алфавит.

• Map (словарь, ассоциативный список) - набор из пар "ключ-значение". Ключи 
уникальны и каждый из них соответствует ровно одному значению. Значения 
могут иметь дубликаты. Ассоциативные списки полезны для хранения логических 
связей между объектами, например, ID сотрудников и их должностей.

Стандартная библиотека Kotlin предоставляет реализации для основных типов 
коллекций: Set, List, Map. Есть два вида интерфейсов, предоставляющих каждый из 
этих типов:

• неизменяемый ( read-only) - предоставляет операции, которые дают доступ к 
элементам коллекции.

• изменяемый (mutable) - расширяет предыдущий интерфейс и дополнительно даёт 
доступ к операциям добавления, удаления и обновления элементов коллекции.

Обратите внимание, что изменяемую коллекцию не требуется объявлять с помощью 
ключевого слова var. Связано это с тем, что изменения вносятся в изначальные 
объекты коллекции без изменения ссылки на саму коллекцию. Но если вы объявите 
коллекцию с помощью val и попытаетесь ее перезаписать, то получите ошибку 
компиляции.
```kotlin
fun main() { 
val numbers = mutableListOf("one", "two", "three", "four") 
numbers.add("five") // this is OK 
//numbers = mutableListOf("six", "seven") // compilation error
}
```

### Схема интерфейсов коллекций Kotlin:
![Схема](https://kiparo.com/file_uploads/blog_images/collection_200x_kiparo_com.png)

MutableCollection<T> - это Collection с операциями записи, такими как add и remove.

```kotlin
fun List<String>.getShortWordsTo(shortWords: MutableList<String>, maxLength: Int) {
this.filterTo(shortWords) { it.length <= maxLength } 
// throwing away the articles
val articles = setOf("a", "A", "an", "An", "the", "The") 
shortWords -= articles 
} 
fun main() { 
val words = "A long time ago in a galaxy far far away".split(" ") 
val shortWords = mutableListOf<String>() 
words.getShortWordsTo(shortWords, 3) 
println(shortWords) // [ago, in, far, far]
}
```

Элементы списка (в том числе null) могут дублироваться: список может содержать 
любое количество одинаковых объектов. Два списка считаются равными, если они 
имеют одинаковый размер и их элементы в одних и тех позициях структурно равны.

```kotlin
data class Person(var name: String, var age: Int) 
fun main() { 
val bob = Person("Bob", 31) 
val people = listOf(Person("Adam", 20), bob, bob) 
val people2 = listOf(Person("Adam", 20), Person("Bob", 31), bob) 
println(people == people2) // true
bob.age = 32
println(people == people2) // false
}
```

Set<T> хранит уникальные элементы; их порядок обычно не определён. null также 
является уникальным элементом: Set может содержать только один null. Два 
множества равны, если они имеют одинаковый размер и для каждого элемента 
множества есть равный элемент в другом множестве.

```kotlin
fun main() { 
val numbers = setOf(1, 2, 3, 4) 
println("Number of elements: ${numbers.size}") // Number of elements: 4
if (numbers.contains(1)) 
println("1 is in the set") 
val numbersBackwards = setOf(4, 3, 2, 1) 
println("The sets are equal: ${numbers == numbersBackwards}") // true
}
```

Map<K, V> **не является** наследником интерфейса Collection; однако это один из 
типов коллекций в Kotlin. Map хранит пары "ключ-значение" (или entries); ключи 
уникальны, но разные ключи могут иметь одинаковые значения. Интерфейс Map
предоставляет такие функции, как доступ к значению по ключу, поиск ключей и 
значений и т. д.

## Создание коллекций

списков есть конструктор, принимающий размер списка и функциюинициализатор, которая определяет значение элементов на основе их индексов.

```kotlin
fun main() { 
val doubled = List(3, { it * 2 }) // или MutableList, если вы хотите изменять содержимое
println(doubled) // [0, 2, 4]
}
```

Чтобы создать коллекцию конкретного типа, например, ArrayList или LinkedList, вы 
можете использовать их конструкторы. Аналогичные конструкторы доступны и для 
реализаций Set и Map.

```kotlin
val linkedList = LinkedList<String>(listOf("one", "two", "three")) 
val presizedSet = HashSet<Int>(32)
```

Если вам требуется создать новую коллекцию, но с элементами из существующей 
коллекции, то вы можете её скопировать. Операции копирования из стандартной 
библиотеки создают неполные копии коллекций - со ссылками на исходные 
элементы. Поэтому изменение, внесённое в элемент коллекции, будет применено ко 
всем его копиям.
Функции копирования коллекций, такие как toList(), toMutableList(), toSet() и другие, 
фиксируют состояние коллекции в определённый момент времени. Результат их 
выполнения - новая коллекция, но с элементами из исходной коллекции. Если вы 
добавите или удалите элементы из исходной коллекции, это не повлияет на копии. 
Копии также могут быть изменены независимо от источника.

```kotlin
fun main() { 
val sourceList = mutableListOf(1, 2, 3) 
val copyList = sourceList.toMutableList() 
val readOnlyCopyList = sourceList.toList() 
sourceList.add(4) 
println("Copy size: ${copyList.size}") // 3
//readOnlyCopyList.add(4) // ошибка компиляции
println("Read-only copy size: ${readOnlyCopyList.size}") // 3
}
```

Ограничение изменений коллекции
```kotlin
fun main() { 
val sourceList = mutableListOf(1, 2, 3) 
val referenceList: List<Int> = sourceList
//referenceList.add(4) // ошибка компиляции
sourceList.add(4) 
println(referenceList) // показывает текущее состояние sourceList - [1, 2, 3, 4]
}
```

Коллекции могут создаваться в результате выполнения операций над другими 
коллекциями. Например, функция filter создаёт новый список элементов, 
соответствующих заданному фильтру:

```kotlin
fun main() { 
val numbers = listOf("one", "two", "three", "four") 
val longerThan3 = numbers.filter { it.length > 3 } 
println(longerThan3) // [three, four]
}
```

## Итераторы

Итератор - это объект, который позволяет перемещаться (итерироваться) по элементам некоторой последовательности.

Как только итератор проходит через последний элемент, его больше нельзя 
использовать для извлечения элементов; его также нельзя вернуть в предыдущее 
положение. Чтобы снова перебрать коллекцию, нужно создать новый итератор.

Следующие коды эквивалентны

```kotlin
fun main() { 
val numbers = listOf("one", "two", "three", "four") 
val numbersIterator = numbers.iterator() 
while (numbersIterator.hasNext()) {
println(numbersIterator.next())
}
}
```

```kotlin
fun main() { 
val numbers = listOf("one", "two", "three", "four") 
for (item in numbers) {
println(item)
}
}
```

Также, есть полезная функция forEach(), которая позволяет автоматически 
перебирать коллекцию и выполнять заданный код для каждого элемента. Перепишем 
пример выше:

```kotlin
fun main() { 
val numbers = listOf("one", "two", "three", "four") 
numbers.forEach{ println(it) }
}
```

Для списков существует специальная реализация итератора: ListIterator. Он 
поддерживает итерацию списков в обоих направлениях: вперёд и назад.

Для итерации изменяемых коллекций существует MutableIterator, который 
расширяет Iterator с помощью функции удаления элементов remove(). Поэтому, вы 
можете удалять элементы из коллекции во время итерации.

```kotlin
fun main() { 
val numbers = mutableListOf("one", "two", "three", "four") 
val mutableIterator = numbers.iterator() 
mutableIterator.next() 
mutableIterator.remove() 
println("After removal: $numbers") // [two, three, four]
}
```

Mutable**List**Iterator помимо удаления элементов, позволяет добавлять и заменять 
элементы во время итерации.

```kotlin
fun main() { 
val numbers = mutableListOf("one", "four", "four") 
val mutableListIterator = numbers.listIterator() 
mutableListIterator.next() 
mutableListIterator.add("two") 
mutableListIterator.next() 
mutableListIterator.set("three") 
println(numbers) // [one, two, three, four]
}
```