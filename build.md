Started by an SCM change
Running as SYSTEM
Building in workspace C:\Users\Haris\.jenkins\workspace\game2048
No credentials specified
 > C:\Program Files\Git\bin\git.exe rev-parse --is-inside-work-tree # timeout=10
Fetching changes from the remote Git repository
 > C:\Program Files\Git\bin\git.exe config remote.origin.url https://github.com/rimsha-ssa/2048 # timeout=10
Fetching upstream changes from https://github.com/rimsha-ssa/2048
 > C:\Program Files\Git\bin\git.exe --version # timeout=10
 > C:\Program Files\Git\bin\git.exe fetch --tags --force --progress -- https://github.com/rimsha-ssa/2048 +refs/heads/*:refs/remotes/origin/* # timeout=10
 > C:\Program Files\Git\bin\git.exe rev-parse "refs/remotes/origin/master^{commit}" # timeout=10
 > C:\Program Files\Git\bin\git.exe rev-parse "refs/remotes/origin/origin/master^{commit}" # timeout=10
Checking out Revision 946798503e2c0aad9dc7c993d031581c7c402281 (refs/remotes/origin/master)
 > C:\Program Files\Git\bin\git.exe config core.sparsecheckout # timeout=10
 > C:\Program Files\Git\bin\git.exe checkout -f 946798503e2c0aad9dc7c993d031581c7c402281 # timeout=10
Commit message: "Merge branch 'master' of github.com:rimsha-ssa/2048"
 > C:\Program Files\Git\bin\git.exe rev-list --no-walk 06c81db336a75544c99b468a55cf0905d0d08721 # timeout=10
Injecting SonarQube environment variables using the configuration: SonarQube
[game2048] $ C:\Users\Haris\.jenkins\tools\hudson.plugins.sonar.SonarRunnerInstallation\null\bin\sonar-scanner.bat ******** -Dsonar.projectKey=sonarkey -Dsonar.projectName=sonarkey2048 -Dsonar.language=py -Dsonar.sourceEncoding=UTF-8 -Dsonar.login=87e89725653aaba616d9b0286b0414fd67467b89 -Dsonar.projectVersion=1.0 -Dsonar.my.property=value -Dsonar.projectBaseDir=C:\Users\Haris\.jenkins\workspace\game2048
INFO: Scanner configuration file: C:\Users\Haris\.jenkins\tools\hudson.plugins.sonar.SonarRunnerInstallation\null\bin\..\conf\sonar-scanner.properties
INFO: Project root configuration file: NONE
INFO: SonarQube Scanner 4.2.0.1873
INFO: Java 11.0.6 Oracle Corporation (64-bit)
INFO: Windows 10 10.0 amd64
INFO: User cache: C:\Users\Haris\.sonar\cache
INFO: SonarQube server 8.1.0
INFO: Default locale: "en_GB", source code encoding: "UTF-8"
INFO: Load global settings
INFO: Load global settings (done) | time=140ms
INFO: Server id: BF41A1F2-AXBFEeluEyLlJGJCnHZA
INFO: User cache: C:\Users\Haris\.sonar\cache
INFO: Load/download plugins
INFO: Load plugins index
INFO: Load plugins index (done) | time=108ms
INFO: Load/download plugins (done) | time=280ms
INFO: Process project properties
INFO: Process project properties (done) | time=0ms
INFO: Execute project builders
INFO: Execute project builders (done) | time=8ms
INFO: Project key: sonarkey
INFO: Base dir: C:\Users\Haris\.jenkins\workspace\game2048
INFO: Working dir: C:\Users\Haris\.jenkins\workspace\game2048\.scannerwork
INFO: Load project settings for component key: 'sonarkey'
INFO: Load project settings for component key: 'sonarkey' (done) | time=24ms
INFO: Load quality profiles
INFO: Load quality profiles (done) | time=120ms
INFO: Detected Jenkins
INFO: Load active rules
INFO: Load active rules (done) | time=1720ms
INFO: Indexing files...
INFO: Project configuration:
INFO: 16 files indexed
INFO: 0 files ignored because of scm ignore settings
INFO: Quality profile for py: Sonar way
INFO: Quality profile for xml: Sonar way
INFO: ------------- Run sensors on module sonarkey2048
INFO: Load metrics repository
INFO: Load metrics repository (done) | time=96ms
WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by net.sf.cglib.core.ReflectUtils$1 (file:/C:/Users/Haris/.sonar/cache/a2b6a8802525720c8af2ca4fa85a2513/sonar-javascript-plugin.jar) to method java.lang.ClassLoader.defineClass(java.lang.String,byte[],int,int,java.security.ProtectionDomain)
WARNING: Please consider reporting this to the maintainers of net.sf.cglib.core.ReflectUtils$1
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release
INFO: Sensor Python Sensor [python]
INFO: Load project repositories
INFO: Load project repositories (done) | time=35ms
INFO: Sensor Python Sensor [python] (done) | time=2631ms
INFO: Sensor Cobertura Sensor for Python coverage [python]
INFO: Sensor Cobertura Sensor for Python coverage [python] (done) | time=80ms
INFO: Sensor PythonXUnitSensor [python]
INFO: Sensor PythonXUnitSensor [python] (done) | time=40ms
INFO: Sensor JaCoCo XML Report Importer [jacoco]
INFO: Sensor JaCoCo XML Report Importer [jacoco] (done) | time=8ms
INFO: Sensor JavaXmlSensor [java]
INFO: 5 source files to be analyzed
INFO: Sensor JavaXmlSensor [java] (done) | time=456ms
INFO: Sensor HTML [web]
INFO: Sensor HTML [web] (done) | time=4ms
INFO: Sensor XML Sensor [xml]
INFO: 5 source files to be analyzed
INFO: 5/5 source files have been analyzed
INFO: Sensor XML Sensor [xml] (done) | time=385ms
INFO: 5/5 source files have been analyzed
INFO: ------------- Run sensors on project
INFO: Sensor Zero Coverage Sensor
INFO: Sensor Zero Coverage Sensor (done) | time=24ms
INFO: SCM Publisher SCM provider for this project is: git
INFO: SCM Publisher 4 source files to be analyzed
INFO: SCM Publisher 0/4 source files have been analyzed (done) | time=204ms
WARN: Missing blame information for the following files:
WARN:   * .idea/ant.xml
WARN:   * coverage.xml
WARN:   * .idea/workspace.xml
WARN:   * nosetests.xml
WARN: This may lead to missing/broken features in SonarQube
INFO: CPD Executor Calculating CPD for 3 files
INFO: CPD Executor CPD calculation finished (done) | time=20ms
INFO: Analysis report generated in 275ms, dir size=134 KB
INFO: Analysis report compressed in 88ms, zip size=33 KB
INFO: Analysis report uploaded in 40ms
INFO: ANALYSIS SUCCESSFUL, you can browse http://localhost:9000/dashboard?id=sonarkey
INFO: Note that you will be able to access the updated dashboard once the server has processed the submitted analysis report
INFO: More about the report processing at http://localhost:9000/api/ce/task?id=AXBLHvjaEyLlJGJCnJoC
INFO: Analysis total time: 10.798 s
INFO: ------------------------------------------------------------------------
INFO: EXECUTION SUCCESS
INFO: ------------------------------------------------------------------------
INFO: Total time: 13.766s
INFO: Final Memory: 13M/47M
INFO: ------------------------------------------------------------------------
[game2048] $ cmd /c call C:\Users\Haris\AppData\Local\Temp\jenkins3392938184440962444.bat

C:\Users\Haris\.jenkins\workspace\game2048>set -e 
Environment variable -e not defined

C:\Users\Haris\.jenkins\workspace\game2048>pip install nose coverage nosexcover pylint 
Requirement already satisfied: nose in c:\users\haris\appdata\local\programs\python\python37-32\lib\site-packages (1.3.7)
Requirement already satisfied: coverage in c:\users\haris\appdata\local\programs\python\python37-32\lib\site-packages (5.0.3)
Requirement already satisfied: nosexcover in c:\users\haris\appdata\local\programs\python\python37-32\lib\site-packages (1.0.11)
Requirement already satisfied: pylint in c:\users\haris\appdata\roaming\python\python37\site-packages (2.3.1)
Requirement already satisfied: isort<5,>=4.2.5 in c:\users\haris\appdata\roaming\python\python37\site-packages (from pylint) (4.3.20)
Requirement already satisfied: mccabe<0.7,>=0.6 in c:\users\haris\appdata\roaming\python\python37\site-packages (from pylint) (0.6.1)
Requirement already satisfied: colorama; sys_platform == "win32" in c:\users\haris\appdata\roaming\python\python37\site-packages (from pylint) (0.4.1)
Requirement already satisfied: astroid<3,>=2.2.0 in c:\users\haris\appdata\roaming\python\python37\site-packages (from pylint) (2.2.5)
Requirement already satisfied: typed-ast>=1.3.0; implementation_name == "cpython" in c:\users\haris\appdata\roaming\python\python37\site-packages (from astroid<3,>=2.2.0->pylint) (1.3.5)
Requirement already satisfied: six in c:\users\haris\appdata\roaming\python\python37\site-packages (from astroid<3,>=2.2.0->pylint) (1.12.0)
Requirement already satisfied: lazy-object-proxy in c:\users\haris\appdata\roaming\python\python37\site-packages (from astroid<3,>=2.2.0->pylint) (1.4.1)
Requirement already satisfied: wrapt in c:\users\haris\appdata\roaming\python\python37\site-packages (from astroid<3,>=2.2.0->pylint) (1.11.1)
You are using pip version 18.1, however version 20.0.2 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

C:\Users\Haris\.jenkins\workspace\game2048>exit 0 
[game2048] $ cmd /c call C:\Users\Haris\AppData\Local\Temp\jenkins12420958912803651206.bat

C:\Users\Haris\.jenkins\workspace\game2048>set -e 
Environment variable -e not defined

C:\Users\Haris\.jenkins\workspace\game2048>nosetests -sv --with-xunit --xunit-file=nosetests.xml --with-xcoverage --xcoverage-file=coverage.xml 
test_down (test.TestPrivate2048) ... ok
test_left (test.TestPrivate2048) ... ok
test_merge_values (test.TestPrivate2048) ... ok
test_right (test.TestPrivate2048) ... ok
test_up (test.TestPrivate2048) ... ok

----------------------------------------------------------------------
XML: C:\Users\Haris\.jenkins\workspace\game2048\nosetests.xml
Name            Stmts   Miss  Cover
-----------------------------------
src\helper.py     103     30    71%
----------------------------------------------------------------------
Ran 5 tests in 0.020s

OK

C:\Users\Haris\.jenkins\workspace\game2048>exit 0 
[game2048] $ cmd.exe /C "C:\Users\Haris\.jenkins\tools\hudson.tasks.Ant_AntInstallation\ant_1.10.7\bin\ant.bat && exit %%ERRORLEVEL%%"
Buildfile: C:\Users\Haris\.jenkins\workspace\game2048\build.xml

init:

clean.module.game2048:

clean:

compile.module.game2048.production:

compile.module.game2048.tests:

compile.module.game2048:

build.modules:

all:

BUILD SUCCESSFUL
Total time: 0 seconds
Finished: SUCCESS
