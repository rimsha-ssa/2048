# 2048_puzzle game 
- 2048 is an interesting single-player sliding block puzzle game. The game is won when a tile with a value of 2048 appears on the board, hence the name of the game.
- For more description
<a href="https://en.wikipedia.org/wiki/2048_(video_game)">2048 (video game)</a>
[![2048 (video game)](http://blog.datumbox.com/wp-content/uploads/2014/04/game-2048-java.png)](https://en.wikipedia.org/wiki/2048_(video_game))

---
## Play the Game
- To play the game click on the link to download.
The executable was made using PyInstaller(Compatible with Windows OS)\
<a href="https://github.com/rimsha-ssa/2048/blob/master/dist/game.exe">play game</a>

---
## Table of Contents
1. [UML](#uml) at least 3 diagrams
2. [Metrics](#metrics) (at least two. Sonarcube would be great)
3. [Clean Code Development](#clean-code-development) (at least 5 points you can show me + 10 point cheat sheet)
4. [Build Management](#build-management) with any Build System as Ant, Maven, Gradle, etc. (only travis is not enough) Do e.g. generate Docs, call tests, etc.
5. [Unit Test](#unit-test) Integrate some nice Unit-Tests in your Code to be integrated in the Build
6. [Continous Delivery Pipeline](#continous-delivery-pipeline)  (show me your pipeline in e.g. Jenkins, Travis-CI, Circle-CI, etc.)
7. [Pycharm and key shortcuts](#pycharm-and-key-shortcuts) Use a good IDE and get fluent with it as e.g. IntelliJ. What are your favourite Key-Shortcuts?!
9. [Functional Programming](#functional-programming) (prove that you have covered all functional definitions in your code as
only final data structures
(mostly) side effect free functions
the use of higher order functions
functions as parameters and return values
use clojures / anonymous functions
---
<a name="uml"></a>
## 1. UML

![Class Diagram)](https://github.com/rimsha-ssa/2048/blob/master/UML.jpg)]


---
<a name="metrics"></a>
## 2. METRICS
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=rimsha-ssa_2048&metric=alert_status)](https://sonarcloud.io/dashboard?id=rimsha-ssa_2048)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=rimsha-ssa_2048&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=rimsha-ssa_2048)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=rimsha-ssa_2048&metric=sqale_index)](https://sonarcloud.io/dashboard?id=rimsha-ssa_2048)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=rimsha-ssa_2048&metric=code_smells)](https://sonarcloud.io/dashboard?id=rimsha-ssa_2048)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=rimsha-ssa_2048&metric=ncloc)](https://sonarcloud.io/dashboard?id=rimsha-ssa_2048)

- [![Capture 2](https://user-images.githubusercontent.com/61032020/74592855-85fa3200-5025-11ea-8dda-8a9624dcfccd.JPG)](https://sonarcloud.io/dashboard?id=rimsha-ssa_2048)
- To view the Sonarcloud.io project status click on the image above.
---
<a name="clean-code-development"></a>
## 3. CLEAN CODE DEVELOPMENT

- **Source Code Conventions** - <a href="https://www.python.org/dev/peps/pep-0008">PEP8</a>
               
               Docstrings were used with every function
               Constant indentation level was used throughout the code.
               Whitespaces were declared appropriately.
To view the PEP8 convention in the code click on <a href="https://github.com/rimsha-ssa/2048/blob/c8fa959b7a3890d1eed039f7a4bdfb54adabbadf/src/helper.py#L31">function</a>

- **Separation of Concerns**
               
               Each game operation is handled in a separate function and doesn't overlap i.e., 
               they are not aware of each other.
To view the SoC in the code click on <a href="https://github.com/rimsha-ssa/2048/blob/c8fa959b7a3890d1eed039f7a4bdfb54adabbadf/src/helper.py#L145">reference</a>
             
- **Open/Closed Principle (Open to extension but Closed to modification)**
              
              All game operations can be extended e.g., to add another function that reverses last 
              move or to create a grid more than 4x4 size can be made through the same game but they
              are closed to modification.
              
- **Don't Repeat Yourself**
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=rimsha-ssa_2048&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=rimsha-ssa_2048)

              (DRY principle) was used throughout the game

              
- **Single Responsibility**
              
              The code has 1 class that is solely responsible for creating/updating the grid and a 
              separate file of helper functions that handles mathematical computations. Another class 
              solely for testing the critical functions.
To view the SR in the code click on <a href="https://github.com/rimsha-ssa/2048/blob/c8fa959b7a3890d1eed039f7a4bdfb54adabbadf/src/game.py#L32">reference</a>
              



***Link to <a href="https://github.com/rimsha-ssa/2048/blob/master/cheatsheet.md">cheat sheet</a>***



---
<a name="build-management"></a>
## 4. BUILD MANAGEMENT
![Capture 5](https://user-images.githubusercontent.com/61032020/74595491-37a75c00-5042-11ea-932e-da5e7edc8cf4.JPG)

- Ant build system in Jenkins was used to run the build xml file for the project.

- View the file that was used to run ant build system <a href="https://github.com/rimsha-ssa/2048/blob/master/build.xml
">build file</a>

![Capture 6](https://user-images.githubusercontent.com/61032020/74595492-3aa24c80-5042-11ea-8d2c-9c7fa3117cab.JPG)



---
<a name="unit-test"></a>
## 5. UNIT TEST
- Pythons library UnitTest was used to test the critical functions in the game.

![Capture 3](https://user-images.githubusercontent.com/61032020/74593796-6e27ab80-502f-11ea-9cf5-ca27971b7132.JPG)

- nosetests with xunit and coverage was installed in sonar scanner. Nosetests was used to run unit tests, and generate information relating to the source code.It helped run the test runner, generates coverage information, and generates an XML test report.

![Capture 4](https://user-images.githubusercontent.com/61032020/74593885-79c7a200-5030-11ea-95ca-ff622da27b40.JPG)




---
<a name="continous-delivery-pipeline"></a>
## 6. CONTINOUS DELIVERY PIPELINE

![Capture 9](https://user-images.githubusercontent.com/61032020/74597082-0b4b0a00-5059-11ea-82ed-89a74d794405.JPG)

- The build console output can be viewed in the <a href="https://github.com/rimsha-ssa/2048/blob/master/build.text">build.md</a> file.

- Also <a href="https://github.com/rimsha-ssa/2048/blob/master/Jenkinsfile">jenkins</a> file shows the pipeline for the code.


---
<a name="intellij-and-key-shortcuts"></a>
## 7. PyCharm AND KEY SHORTCUTS

> - Ctrl+K Compare the changes and to commit changes to local repository.

> - Ctrl+ Shift+K push local commits to remote repository.

> - Double Shift to find anything related to PyCharm or the project and open it, execute it, or jump to it.

> - Ctrl+E	to select a recently opened file from the list.

> - F2 to navigate between code issues and Shift+F2 to jump to the next or previous highlighted error.

PyCharm is the default IDE to use for Python development. Among other IntelliJ products, this turns out to be one of the most comfortable IDEs, with excellent plugin support, tooling, and look and feel. It serves as an excellent support tool to develop any kind of Python application, from backend applications through data science scripts to Python web apps.

---
<a name="dsl"></a>

---
<a name="functional-programming"></a>
## 9. FUNCTIONAL PROGRAMMING
- only final data structures
 > All the data structures used in the project are final fata structures. For example, all <a href="https://github.com/rimsha-ssa/2048/tree/master/src">files</a> in the system use only final properties.
 
- <a href="https://github.com/rimsha-ssa/2048/blob/2a96bed64ed1e464bd23d935ce2bd3fa5c0ad3d5/src/helper.py#L16">(mostly)</a> side effect
<a href="https://github.com/rimsha-ssa/2048/blob/2a96bed64ed1e464bd23d935ce2bd3fa5c0ad3d5/src/helper.py#L60">free</a> functions

- the use of <a href="https://github.com/rimsha-ssa/2048/blob/2a96bed64ed1e464bd23d935ce2bd3fa5c0ad3d5/src/helper.py#L31">higher</a> order functions

- <a href="https://github.com/rimsha-ssa/2048/blob/4896d406b9856979ee2da105837329b4be909a50/src/helper.py#L131">functions</a> as parameters and return values

---
