# Andelabs2
MISSING NUMBER
```python
def find_missing(lst1,lst2):
	if not lst1 and not lst2:
		return 0
		if not set(lst1) ^ set(lst2):
			return 0
		else:
			return list(set(lst1)^ set(lst2))[0]
```
Above is a python function that compares contents of two lists ,lst1 and lst2.
If the two lists are empty,the function returns 0(`if not lst1 and not lst2:`) The function passes to the next `if` if both lists have content and returns 0 if the conntents of the lists are the same and equal e.g `[1,2,3]` and `[1,2,3]`.Otherwise the function returns the differnce of the two lists i.e `else:return list(set(lst1)^ set(lst2))[0]` as a number .



BINARY SEARCH CLASS

The binary search is used to find an item in an ORDERED list.
For example, to find a number in the list below:
`2, 5, 7, 12, 14, 21, 28, 31, 36`

To search for an item, look in the middle of the list and see if the number you want is in the middle, above the middle or below the middle. If it is in the middle, you have found the item. If it is higher than the middle value, then adjust the bottom of the list so that you search in a smaller list starting one above the middle of the list. If the number is lower than the middle value, then adjust the top of the list so that you search in a smaller list which has its highest position one less than the middle position.
Below is a simple algorithm for a binary saerch 
```python
Found <- False
while not Found and first <= top
    Midpoint <- (First + Last) DIV 2
    If List[Midpoint] = ItemSought Then
        ItemFound <- True
    Else
        If First >= Last Then
            SearchFailed <- True
        Else
            If List[Midpoint] > ItemSought Then
                Last <- Midpoint - 1
            Else
                First <- Midpoint + 1
            EndIf
        EndIf
    EndIf
```
I HAVE USED THE ABOVE CONCEPT TO DO A BINARY SEARCH OF AN ELEMENT IN A LIST AS BELOW:



```python
class BinarySearch(list):

    def __init__(self, length, diff):
        super(BinarySearch, self).__init__()
        value = diff
        for i in range(length):
            self.append(value)
            value = value + diff
        self.length = len(self)

    def search(self, value):
        first = 0
        last = len(self) - 1
        mid = 0
        found = False
        count = 0

        if value == self[first]:
            mid = first
            found = True
        elif value == self[last]:
            mid = last
            found = True

        if value not in self:
            found = True
            mid = -1

        while first <= last and not found:
            mid = (first + last) // 2
            if self[mid] == value:
                found = True
            else:
                count += 1
                if value < self[mid]:
                    last = mid - 1
                else:
                    first = mid + 1

        return {'count': count, 'index': mid}

if __name__ == '__main__':
    binSearch = BinarySearch(100, 10)
    print(BinarySearch(20, 2).search(40))
    print(binSearch.search(30))
    print(binSearch.search(700))
    print(binSearch.search(10000))
    ```
   
    
SIMPLE USER INTERFACE CREATED USING HTML AND CSS

HTML is the standard markup language for creating Web pages.HTML stands for Hyper Text Markup Languag and describes the structure of Web pages using markup language.HTML elements are the building blocks of HTML pages.It's elements are represented by tags.HTML tags label pieces of content such as "heading", "paragraph", "table", and so on.Browsers do not display the HTML tags, but use them to render the content of the page.Cascading Style Sheets (CSS) on the other hand  is a style sheet language used for describing the presentation of a document written in a markup languag e.g color,fonts and spacing.The following link show a simple webpage which incorporates the use of html and css.

Click here:``https://github.com/fredrickochieng/Andelabs2/blob/master/front-end.html``

CODE
```python
<!DOCTYPE html>
<html>
<head>
<style>
div.container {
    width: 110%;
    border: 1px solid gray;
}

header, footer {
    padding: 1em;
    color: red;
    background-color: black;
    clear: left;
    text-align: center;
}

nav {
    float: left;
    max-width: 190px;
    margin: 0;
    padding: 1em;
}

nav ul {
    list-style-type: none;
    padding: 0;
}
   
nav ul a {
    text-decoration: none;
}

article {
    margin-left: 10px;
    border-left: 1px solid gray;
    padding: 1em;
    overflow: hidden;
}
</style>
</head>
<body>

<div class="container">

<header>
   <h1>RIPTS INC</h1>
</header>
  
<nav>
  <ul>
    <li><a href="#">Nairobi</a></li>
    <li><a href="#">Lagos</a></li>
    <li><a href="#">New York</a></li>
  </ul>
</nav>

<article>
  <h1>RIPTS INC</h1>
  <p>Research,IT,Printing and Training Solutions Limited (RIPTs) is a private limited company established to respond to the growing needs for professional services required by stakeholders to address contemporary challenges in the society. It provides capacity building services to individuals and institutions providing services to underprivileged. We provide quality consultancy and professional advisory services through training, policy advisory services and applied research in the fields of training, organization capacity development, project management, research, and conducting monitoring, evaluation and learning from where it documents and shares good practices..</p>
  <p>We draw our strength from the expertise of the pool of associate consultants who have strong academic and professional backgrounds, vast experience and refined skills on their areas of specialization. It encourages mentoring of emerging practitioners and provides a platform from where theory and practice synergize..</p>
</article>
<footer>Copyright &copy; RIPTS INC</footer>
</div>
</body>
</html>
```
