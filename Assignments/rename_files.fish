#!/usr/bin/env fish

for file in q*.py
    set number (string replace .py '' $file)   # Remove .py extension
    set number (string replace q '' $number)  # Remove 'q' prefix
    mv "$file" "Conditional Statements Q$number.py"
end
