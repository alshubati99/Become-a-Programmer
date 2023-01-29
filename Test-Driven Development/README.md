# Programming Foundations: Test-Driven Development (TDD)
# [*Course Certificate*](https://www.linkedin.com/learning/certificates/18edc26efcded3ffa5b4e1d1dcf1c1b800a6e1c7c178df14506f57b1d3436823)

### Test-Driven Development:
- Start with a plan then develop on it. 
- Start with the requirments then design then the code to implement the design and lastly write a test. 
- Unit testing. 
- System testing.
- Integragion testing.
- Test Code Refactor Cycle: 
    1. Test case.
    2. Code.
    3. Refactor.
    - Refactoring: improving the internal structure of the code without changing the external behavior.
- Test last approach:
    - Understand Requirements then start the design process: Use case and class diagrams. 
- xUnit framework:
    - SUnit for smalltalk.
    - JUnit for Java. 
    - xUnit components:
        - Test case.
        - Test fixture.
        - Test suite.
        - Test result.
        - Test runner. 
- JUnit Framework:
    - For jave.
    - Lack flexibility that a developer require.
    - JUnit 5 Modules:
        - Vintage.
        - Jupiter.
        - Platform.
- Writing Test Cases:
    - Requirements.
> Assertions
### TDD Methodology:
- You code to pass the test. 
- Fake it approach.
- Where to start?
    - Prioritize use cases in sprint planning.
    - Identify the acceptance criteria.
    - Start with unit test cases for the acceptance criteria.
    - Test the big picture.
- Refactroing:
    - Take longer than few minutes. 
    - To make the code easy to read and understand. 
    - Make it cheaper to modify without changing its external behavior. 
- Intention vs. Implementation:
    - Extract Function Refactroing. 
    > Check refactoring.com
### TDD Structure and Syntax:
- Typically, one test class per code, class. 
- Design test cases to test requirements, not to test methods.
- Test casee:
    - Arrange.
    - Act.
    - Assert.
- Test Fixtures:
    - A fixed state of the system required at the sart of a test. 
    - Ensure that a test is repeatable.
    - Set up before the test runs and torn down after it has finished. 
    - Can be shared by test cases needing same state.
- Assert in programming languages:
    - Assertion: an idion for defensive programming.
    - Supported in many languages, including c, c++, java, js, python.
    - Has a condition that is expected to be true when executed, else it throw an assertion error.
    - Assert condition: by default assertions are disabled.
    - Junit supports some assertions that are static.
- Testing Exceptions:
    - Test cases to test exceptions are designed a little differently.
    - Junit4 test cases for exceptions are different from those in Junit5  
### Scaling TDD:
- A system is developed using IDEs.
- Large scale systems are build using certain frameworks. 
- Junit5 frameworks:
    - AssertJ
    - Hamcrest.
    - Truth
- Test Doubles => Oject under test:
    - Dummy object. 
    - Stub.
    - Mock.
    - Spy.
    - Fake object. 
- Mocking:
    - Preprogrammed with expectations which form a specification. 
    - Stub is hand coded while Mock is generated.
    - Stub offers canned responses while Mock offers expected behavior.
    - Stub focuses on state of the dependency while Mock focuses on behavior of the dependency.
    - Mocks are defined using frameworks. 
    - Mocking API changing according to the language used. 

> Checkout this [course link](https://www.linkedin.com/learning/programming-foundations-test-driven-development-3/2915494?autoplay=true&contextUrn=urn%3Ali%3AlyndaLearningPath%3A56db2b643dd5596be4e4989b&u=60693444) for exercises in java. 





