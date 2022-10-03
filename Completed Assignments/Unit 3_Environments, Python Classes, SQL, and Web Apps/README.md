Technical review:

To continue building on what we learned in Unit 2 we started Unit 3 by focusing on learning how to create, modify, and query databases using SQL, Sqlite3, and PostgreSQL and later advanced into learning about relational and non-relational databases and how each differs from one another. To begin this process we began by solidifying our understanding of Python Modules, Packages, and Environments. 

To understand what Python packages and modules are we need to have a basic understanding of what an environment is and how it is different from a basic instance of a code editor. By default, when you open an IDE  for the first time it will set you up with its default settings such as Font Size, background color, and other things which you may or may not notice. A dedicated environment is very similar to this but allows you to specify exactly what is included in the environment when it is created. For example, you could specify what language you want to use, what packages or libraries you want to be installed or you specify nothing and create an environment that is separate from your default installation in every way. This allows the programmer to be very specific about what is included in the program they are writing. Remember the saying “it works on my machine”? By creating your own environment you can avoid depending on an installation or library that you didn't intentionally specify in your code which would lead to problems down the road. The program we used to create these environments is called Pipenv which, by running the code ‘pipenv lock’, will create a new virtual environment with everything specified in the Pipfile installed. 

Now that we have a basic understanding of what an environment is and how we can use them to our advantage we can move on to packages and Modules. The first thing we need to learn about modules is how to create one. But first what is a Module? A module is a functionality in Python that is a gateway to creating large and complex projects. By creating a Module we are giving ourselves the ability to import code written in another file which will empower us to obey an important coding principle: Don't repeat yourself. To create a module all you need is a folder with a single specific python file name __init__.py. This single file tells your interpreter that this module can be imported and run by other projects in your environment. This is important in this unit because it allows us to connect multiple different files together and use functions across the project. 

Next, we can advance to the SQL section of this Unit where we learn about querying databases through DBbrowser as well as using SQL queries in python to query Sqlite3 databases. First, we need to understand that a SQL query is not so much a request but more like a demand. Our requests are taken very literally and can often be unspecific about the results of our query. For instance, if you want to remove some data from a database and you decide to drop a row of information but mistakenly drop a different row, that row is gone forever and there's nothing you can do about it. In another example, if you do an incorrect join on 2 databases you could accidentally overload your computer and crash the program, losing all your progress in the process. Despite this apparent disadvantage, this is what makes SQL such a powerful language. It can make database manipulation a breeze even when you have millions of lines of data. 

To fully harness the power of SQL and data wrangling we need a way to be able to connect our data with the users of the platform. This is where web hosting and database connections make their first appearance. To build ourselves a quick and easy web platform to connect to we use a program called Flask. This is a Python Framework that makes creating a web application a breeze. You can even start your website in less than 6 lines of code. Each page is designated by its web extension such as /home or /blog. This allows us to write python code to build in the functionality we wish our page to have. For our website we wish to be able to connect to two external programs, the first is the Twitter API which we will use to collect data about users and tweets. The Second will be our Sqlite3 database where we will transform and store our data. We can do all of this easily within our web pages. 

To fully appreciate the power of what we can create with just these tools we are going to build an application that uses many of the things that we learned previously.