# 2048_puzzle game 
- 2048 is an interesting single-player sliding block puzzle game. The game is won when a tile with a value of 2048 appears on the board, hence the name of the game.
- For more description
<a href="https://en.wikipedia.org/wiki/2048_(video_game)">2048 (video game)</a>
[![2048 (video game)](http://blog.datumbox.com/wp-content/uploads/2014/04/game-2048-java.png)](https://en.wikipedia.org/wiki/2048_(video_game))

---
## Play the Game
- To play the game click on the link to download. (Compatible with Windows OS)
---
## Table of Contents
1. [UML](#uml) at least 3 diagrams
2. [Metrics](#metrics) (at least two. Sonarcube would be great)
3. [Clean Code Development](#clean-code-development) (at least 5 points you can show me + 10 point cheat sheet)
4. [Build Management](#build-management) with any Build System as Ant, Maven, Gradle, etc. (only travis is not enough) Do e.g. generate Docs, call tests, etc.
5. [Unit Test](#unit-test) Integrate some nice Unit-Tests in your Code to be integrated in the Build
6. [Continous Delivery Pipeline](#continous-delivery-pipeline)  (show me your pipeline in e.g. Jenkins, Travis-CI, Circle-CI, etc.)
7. [IntelliJ and key shortcuts](#intellij-and-key-shortcuts) Use a good IDE and get fluent with it as e.g. IntelliJ. What are your favourite Key-Shortcuts?!
8. [DSL](#dsl) (Create a small DSL Demo example snippet in your code even if it does not contribute to your project)
9. [Functional Programming](#functional-programming) (prove that you have covered all functional definitions in your code as
only final data structures
(mostly) side effect free functions
the use of higher order functions
functions as parameters and return values
use clojures / anonymous functions
---
<a name="uml"></a>
## 1. UML

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
- Source Code Conventions - <a href="https://www.python.org/dev/peps/pep-0008">PEP8</a>

               were refactored to comply with PEP8 recommendations.
               
- Separation of Concerns 
- Open/Closed Principle (Open to extension but Closed to modification)
- KISS Principle (keep it simple, stupid)
- Single Responsibility

***Link to <a href="https://github.com/rimsha-ssa/2048/blob/master/cheatsheet.md">cheat sheet</a>***



---
<a name="build-management"></a>
## 4. BUILD MANAGEMENT


---
<a name="unit-test"></a>
## 5. UNIT TEST
- Pythons library UnitTest was used to test the critical functions in the game.
![Capture 3](https://user-images.githubusercontent.com/61032020/74593796-6e27ab80-502f-11ea-9cf5-ca27971b7132.JPG)
- nosetests with xunit and coverage was installed in sonar scanner. Nosetests was used to run unit tests, and generate information relating to the source code.It helped run the test runner, generates coverage information, and generates an XML test report



---
<a name="continous-delivery-pipeline"></a>
## 6. CONTINOUS DELIVERY PIPELINE

---
<a name="intellij-and-key-shortcuts"></a>
## 7. IntelliJ AND KEY SHORTCUTS

---
<a name="dsl"></a>
## 8. DSL

---
<a name="functional-programming"></a>
## 9. FUNCTIONAL PROGRAMMING

---
