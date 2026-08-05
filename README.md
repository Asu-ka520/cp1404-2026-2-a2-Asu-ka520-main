# CP1404 Assignment 2: Album Archive 2.0 by YOURNAME

_Edit this README, replacing this line and above with your own assignment details._  
_At the end of the project, complete the project reflection below by answering the questions (replace the ... parts)._
_Note that to get high marks for this, your reflection should match the "exemplary" description from the rubric:_

> The project reflection is complete and describes development and learning well, shows careful thought, highlights
> insights made during code development.

## 1. How many hours did you spend working on this assignment 2 project?

I spent approximately 2days on this project, distributed across planning the class structures, writing unit tests, refactoring the console version, and learning the Kivy framework for the GUI application
## 2. What are you most satisfied with?

I am most satisfied with the seamless integration of the Album and AlbumCollection classes across both the console and GUI programs.

It perfectly demonstrated the power of Object-Oriented Programming and modularity.

Generating dynamic widgets in Kivy utilizing the object list was a major success.

## 3. What are you least satisfied with?

I am least satisfied with my initial attempts at styling the Kivy GUI.

Learning the kv language hierarchy required multiple iterations, and ensuring the interface layouts adjusted cleanly with text spacing took more trial and error than I anticipated.

## 4. What worked well in your development process?

The test-driven approach worked exceptionally well.

By building and testing album.py and albumcollection.py thoroughly with assertions before beginning the GUI, I ensured that any errors encountered later were purely UI-related rather than backend logic issues.

## 5. What about your process could be improved the next time you do a project like this?

Next time, I will spend more time mapping out the GUI layouts on paper before writing the kv code.

A visual sketch of the widget tree would have saved me significant time during Kivy debugging

## 6. Describe what learning resources you used and how you used them.

I heavily relied on the subject materials, specifically the KivyDemos provided in the GitHub repository.

dynamic_widgets.py was instrumental for understanding how to instantiate buttons from a list of objects, and spinner_demo.py assisted with implementing the sorting functionality successfully.

## 7. Describe the main challenges or obstacles you faced and how you overcame them.

A significant challenge was managing state and updating the GUI dynamically.

When a user clicks a button to mark an album as completed, the button color must update, and the sorting potentially needs to refresh.

I overcame this by binding the click event to a method handler that directly mutates the object state, updates the text label, and triggers a complete re-sort and redraw of the widget box
