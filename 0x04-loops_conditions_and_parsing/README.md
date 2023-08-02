# Loops, conditions and parsing
In Bash, loops, conditions, and parsing are fundamental concepts that empower developers to control the flow of their scripts and manipulate data effectively.


## Description
In Bash, loops, conditions, and parsing are fundamental concepts that empower developers to control the flow of their scripts and manipulate data effectively. By combining these concepts, developers can create sophisticated Bash scripts to automate tasks, process data, and respond to various conditions, making Bash a versatile and efficient language for scripting and automation needs.

## Features
 * **Loops:** Bash provides two main types of loops - for and while. for loops iterate over a list of items, executing a code block for each item. On the other hand, while loops repeatedly execute a code block as long as a given condition remains true. These loops enable automation and repetitive processing tasks.

 * **Conditions:** Conditional statements, primarily represented by the if statement, allow developers to make decisions based on certain conditions. By evaluating expressions, scripts can take different paths, execute specific code blocks, or handle different scenarios dynamically.

 * **Parsing:** Parsing involves extracting and manipulating data from strings or files. Bash offers powerful tools like grep, awk, and sed for searching patterns, processing text data in columns, and performing text transformations. These tools are essential for text processing, data extraction, and reporting tasks
.

## Examples
```bash
read -p "Enter a number: " num

if ((num % 2 == 0)); then
    echo "The number is even."
else
    echo "The number is odd."
fi
```

## Usage
```bash
# Printing numbers from 1 to 5 using a for loop.
for i in 1 2 3 4 5; do
    echo "Number: $i"
done

# Printing numbers from 1 to 5 using a while loop.
count=1
while [ $count -le 5 ]; do
    echo "Count: $count"
    ((count++))
done
```

## Credits
 * [The for loop](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html)
 * [Operators](https://tldp.org/LDP/abs/html/ops.html)
 * [Other Comparison Operators](https://tldp.org/LDP/abs/html/comparison-ops.html)
 * [File test operators](https://tldp.org/LDP/abs/html/fto.html)
 * [Make Linux/Unix Script Portable With #!/usr/bin/env As a Shebang](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html)

## Contact
 * [Sakhile Ndlazi](https://www.twitter.com/sakhilelindah)
