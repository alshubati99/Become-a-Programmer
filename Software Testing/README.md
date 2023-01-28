# Programming Foundations: Software Testing /Quality Assurance
# [*Course Certificate*](https://www.linkedin.com/learning/certificates/c3f2b375356e9e0a0b727ae4c8b5449ecc7969c077fc431c2a46bd598bf6d56d)

### Quality Assurance:
- Quality Assurance is a systematic process used to determine whether a product meets specifications. 
- Specialists in Software Testing: 
    - QA
    - QA engineer
    - QA analyst
    - Software engineer in test.
    - Tester
- Ensure the team is building the right product correctly. 
- Quality can be assured throughout the code. 
- The team is responsible for: 
    - Clear specification.
    - Code implementing.
    - Code testing.
    - Code releasing.
- Ongoing process that the whole team is involved in.
- Roles of QAs:
    - ***Technical aptitude***:
        - Needed for manual and automated testing.
        - Programming and scripting.
    - ***Business knowledge***:
        - Feature scoping.
        - Test planning.
        - Test case management.
        - Bug management. 
    - ***DevOps principles***:
        - Configure tools.
        - Set up CI.
        - Set up test environments.
        - Automate processes.      
    - ***Process and release expertise***:
        - Define and improve testing practices.
        - Optimize release process.
> All will wear different hats.
### SDLC:
- SDLC => Software Development Life Cycle:
    - ***Plan***:
        - QA identify risks.
        - Identify use
        cases.
    - ***Define***:
        - Write specs and acceptance criteria.
        - Decide what's in scope.
        - Write test strategy.
    - ***Design***:
        - Solidify test scenarios.
        - Get feedback on scenarios from team.
        - Manual and automation tests.
    - ***Build***:
        - Solidify test scenarios.
        - Get feedback on scenarios from team.
        - Manual and automation tests.
    - ***Test***:
        - Manual and automation tests.
    - ***Deploy***:
        - Validate functionality.
        - Release.
        - Test in production.
### Collaborate with the team:
- A typical software delivery team must have:
    - Developer.
    - Designer.
    - QA tester.
    - Product manager/ business analyst.
- SDLC involvment of the team: 
    - Plan, Define, Design phase:include a representitive from each role.
    - Build, Test phase: include a developer, a tester and a designer.
    - Deply phase: include a developer, tester and a business analyst. 
- Determine acceptance criteria and scope. 
- Provide feedbacks on scenarios. 
- The more collaboration the better. 
- Set expectations and goals.
- Build a relationship with teammates.
- Know responsibilities of each role. 
- Collaborate.
- Sharing goals with team will help the tester's accountability, awareness and raise support. 
- Regularly check in with teammates. 
- Ask for help.
- Give and recieve feedback and align it to the goals. 
### Test Planning:
- *Create a test stratigy*:
    - [Sample Test Strategy](Sample Test Strategy.pdf)
- *Make a test plan*:
    - Scenario:
        - Click a button to add a new user.
    - Expected result:
        - create user model opens and has two required fields for username and email. There is a create user button that becomes enabled once the fieldss are complete.
    - Latest result:
        - Pass or fail
    - Automated:
        - Yes or no
    - One unique scenario per row. 
    - You can have from 10 to 100 scenarios. 
    - Developers and Designer should check the made plan. 
- *Write acceptance criteria*:
    - Conditions that a software product must satisfy to be accepted by a stakeholder. 
    - It helps developer to know what to implement and business analyst to know what scope the software covers and the QA tester what scenarios to test. 
    - AC format:
        - Given => precondition of scenario. 
        - When => action or output of scenario.
        - Then => the expected outcomes. 
- *Identify when testing is complete*:
    - Test.
    - Automate.
    - Sign off AC.
### Types of testing QA focuses on:
- *Box testing*:
    - Three different types:
        1. Black kbox testing => Action in user interface: manual and UI testing. 
        2. Gray box testing => deeper understanding of the apps: integration testing and trigger some action in the UI.
        3. White box testing => tests specific functionalities of the code: Unit and System testing. 
- *Manual testing*:
    - Identify test scenarios.
    - Done at the Test phase of SDLC.
    - Happy path scenarios: no errors. 
    - Sad path scenarios: might have errors. 
- *UI automation testing*:
    - Like Manual testing but with test scripts. 
    - catch regressions. 
    - Test run on any platform or application. 
    - starts at Build and Test phases.
    - Usually Slow. 
- *Integration testing*:
    - Focuses on interactions between components. 
    - Have some of gray box testing. 
    - Write these testing during the Build and Test phases.
    - Tests interactions between Browser, Server and Database. 
- *Performance testing*:
    - Ensure the app can be used over time. 
    - Uses black box testing. 
    - Performance testing Types:
        - *Load testing*: checks the application's ability to perform under user loads.
        - *Endurance testing*: to make sure how application handles load over time => check for system problems.(longer)
        - *Stress testing*: testing an application under extreme workloads => used for testing scalability. 
        - *Common Performance Problems*:
            - Long load time.
            - Poor scalability.
            - Bottlenecking. 
- *Security testing*:
    - Looks to expose problems in the application that can cause unexpected behavior or crashes.
    - SQL Injection: is used to insert database statements into text fields and expose application information => common type of attacks used by hacker. 
    -  Denial of Service (DoS): is an attack where hackers try to take down an application's servers or networks making it unaccessable to users.
    - Vulnerabilities in dependencies can cause massive security problems.
    - Github has feature to automatically scan any harmful actions. 
    - keep an eye on for the areas that can be manipulated. 
### Bugs Reporting:
- Identify bugs. 
- Report a bug:
    - Jira, Rally, Github, Bugzilla. 
    - Bug reporting systems are different. 
    - Bug report should include details like:
        - Name and Description.
        - Steps to reproduce.
        - Expected result.
        - Actual resuls.
        - Screenshots.
        - Browers/ version.
        - Logs and Tags.
        - Priority and Status.
        [Bug Report Sample](Bug Report Template.pdf)
- Triage bugs:
    1. Severity: how impactful the bug is to the system.(X-axes)
    2. Priority: how fast the bug should be fixed. (Y-axes)
- Communicate bugs to the team:
    - Have a project board.
    - Capture analytics about bugs. 
    - Mentor where bugs come from. 
- Get bugs fixed:
    - Clarify a goal to fix a bug. 
    - Fix the most important bugs as soon as possible. 
- Have bugs bashes:
    - 2 to 4 times a year.

**For Further Informaion**: 
> Check Agile Testing by Lisa Crispin. 
> Check online resources:
> https://www.ministryoftesting.com
>https://www.softwaretestinghelp.com
>https://www.softwaretestpro.com



    











