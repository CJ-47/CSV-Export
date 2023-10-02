Welcome to StackIt's hiring assignment! 🚀
If you didn't get here through github classroom, are you sure you're supposed to be here? 🤨

We are glad to have you here, but before you read what you're going to beat your head over for the next few hours (maybe days?), let's get a few things straight:

We really appreciate honesty. Don't copy anyone else's assignment, it'll only sabotage your chances :P
You're free to use any stack, and library of your choice. Use whatever you can get your hands on, on the internet!
We love out of the box solutions. We prefer to call it Jugaad
This might be just the first round, but carries the most importance of all. Give your best, and we hope you have a fun time solving this problem.
✨ Problem Statement: Crafting a CSV Importer for Google Sheets ✨
Context: Data analysts around the world 🌍, handle massive amounts of data to derive meaningful insights for their organization 📊. Among the tools they use, Google Sheets 📈 stands out due to its ease of use, accessibility, and collaborative features. However, many analysts have identified a recurring pain point: the cumbersome process of importing CSV files into Google Sheets repeatedly.

A typical week of an analyst in an e-commerce company 🛒 involves receiving multiple CSV files 📁 containing sales, inventory, customer feedback, and more. The data from these files needs to be meticulously analyzed and presented in the company’s weekly meetings. However, instead of diving directly into analysis, most analysts need to spend an inordinate amount of time just importing and structuring these CSV files into Google Sheets ⏳. This repetitive, time-consuming task reduces the efficiency of these professionals and delays the extraction of crucial insights 😫.

Today, you are going to make their lives better.

Problem Statement: Make a CSV Importer for Google Sheets that lets users drag and drop CSV files onto the Google Sheet. The moment they drop the CSV file, allow them to select which columns to import 🗂️.

You get brownie points 🍪 if you can make it even easier by allowing them to filter the data as well before importing it into Google Sheets 🔍.

Other pointers:

Import to Sheet – After validation and mapping, devise a method to populate the data into a chosen Google Sheet, either appending to existing data or creating a new sheet 📥📋.
Optimize for Large Files – Large datasets are common in analytics. Your solution should effectively handle large CSV files (~15MB CSV file) without causing performance issues or prolonged waiting times 📈📦.
Submission ⏰
The timeline for this submission is: 9AM, 30th Sept, 2023 - 12PM, 2nd Oct, 2023

Some things you might want to take care of:

Make use of git and commit your steps!
Use good coding practices.
Write beautiful and readable code. Well-written code is nothing less than a work of art.
Use semantic variable naming.
Your code should be organized well in files and folders which is easy to figure out.
If there is something happening in your code that is not very intuitive, add some comments.
Add to this README at the bottom explaining your approach (brownie points 😋)
Make sure you finish the assignment a little earlier than this so you have time to make any final changes.

Once you're done, make sure you record a video showing your project working. The video should NOT be longer than 120 seconds. While you record the video, tell us about your biggest blocker, and how you overcame it! Don't be shy, talk us through, we'd love that.

We have a checklist at the bottom of this README file, which you should update as your progress with your assignment. It will help us evaluate your project.

My code's working just fine! 🥳
I have recorded a video showing it working and embedded it in the README ▶️
I have tested all the normal working cases 😎
I have even solved some edge cases (brownie points) 💪
I added my very planned-out approach to the problem at the end of this README 📜
Got Questions❓
Feel free to check the discussions tab, you might get something of help there. Check out that tab before reaching out to us. Also, did you know, the internet is a great place to explore 😛

Developer's Section
Add your video here, and your approach to the problem (optional). Leave some comments for us here if you want, we will be reading this :)

Assignment Edits :

Previous Commmits : https://github.com/CJ-47/CSV-Export

Technology Stack used :
PyCharm IDE : Project Management  and Debugging
Programming Language : Python
GUI : Tkinter,TkinterDnD,
Library Modules used : Numpy , Pandas 


My code's working just fine! 🥳
I have recorded a video showing it working and embedded it in the README ▶️ (x)
I have tested all the normal working cases 😎 :
Works : Multiple File Drag and Drop , Viewing CSV , Searching CSV , Filtering CSV , Exporting Updated CSV Offline mode
In progress : Google Sheets remote Import
Future Works : Cloud Integration , Individual User Logins , Material UI Theme Design

I have even solved some edge cases (brownie points) 💪 : Loosely Strict Inequality 😎 for searching ( i.e. == > ===)

I added my very planned-out approach to the problem at the end of this README 📜

Initially , I had initially planned to develop using Web based Application on React-NodeJS but I finalised a python environment based project as 
it will provide a hybrid environment to view/manage CSV in Offline(Export CSV) as well as Online Environment (Google Developers API ). 
The project uses TkinterDnD module for implementing Drag and Drop Feature and Entry Widget to implement User Input Space and action events .
It uses Label's for more informative GUI. It uses pandas , numpy for CSV Data manipulation which is pretty basic .

Problems I faced :
1.Lack of simple placeholders in Entry Widget,without hover events
2. Modern GUI enhancements

Optimisation I implemented : 1.In Filtering based on multiple column conditions , rather than a DFS based approach where first you check for one condition , 
then subsequently apply remaining on result set , I tried to do it in a single iteration ,where it checks all queries in a single loop , so complexity should be 
reduced from O(n *c) n=number of rows , c=number of conditions , rather than O(n^c)

2. In searching , rather than a strict search where , query only checks for equality , I tried to check as a substring , so It should be able to detect 
smallest matching terms which is helpful in searching long data formats(phone numbers , Addresses ,etc ).
Ex  : 
Name   Phone   Age       Condition Name=Hri and Phone=23               Strict Search           Loose Search
Hrit   12345   21                                                        Not Found                Found

That's it from my side. Will update my progress soon .
