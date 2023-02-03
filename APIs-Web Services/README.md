# Programming Foundations: APIs and Web Services.
# [*Course Certificate*](https://www.linkedin.com/learning/certificates/f9ca19ce57cb63bd000a424f9284d63fd08eacdd11759a03ca87b8c1f6a3fe61)

> Tools used: Postman, SoapUI, GraphQl.

### Web services:
- Interactions between clients and servers.
- A client sends a request (massage) to a server and then the server responds. 
- Data is communicated through **XML**.
- Web services have two typs: 
    - SOAP => Simple Object Access Protocol:
        - Sends massages using XML.
        - XML document is sent with data.
    - RESTful =>  Representaional State Transfer:
        - Uses HTTP to access resources.
- Advantages of web services:
    - Reusibility:
        - Reusable component that can be used by multiple systems.
    - Language Transparency:
        - Communicate with different languages.
    - Usability:
        - Data more accessable to other systems securly.
    - Deployability:
        - Easly available on global level.
- Consideratoins of web services:
    - *Latency*: time it takes a request to return a response.
    - *Partial Failure*: when server or network fails to respond.
- Secure web services:
    - Only trusted individuals should have access.
    - Authentication:
        - Validates identity of client.
        - Unlock phone with password.
    - Authorization:
        - Determines level of clients access.
        - What data they can view or edit.
        - google docs.
        - API key authentication.
- Microservices:
    - APIs: falicitate information sharing.
    - Web service can be an API.
    - Web services:
        - Dependent on SOAP protocol.
        - Requires more work to pack and unpack data.
    - Microservice looks at business problem, type of application to be build and capabilities of your calling clients.
### RESTFull APIs:
- API = menue has bunch of options. 
- API call = Ordering.
- APIs Principles:
    - URI: Uniform Resource Identifier
    - Operations:
        - Get: Retrieve a resource.
        - Post: Creates a resource.
        - Put: Updates a resource.
        - Delete: Removes a resource.
    - Formats:
        - HTML.
        - XML.
        - Plain text.
    - Stateless communication:  
        - Server will not store any state the client made.
- Benefits of REST:
    - Payload: data send back and forth between clients and servers. 
    - SOAP only allow for XML while REST allows multiple like XML, JSON.
- HATEOAS: Hypermedia As The Engine Of Application State.
    - Client interacts  with a REST API entirely through the responses by the server.
    - Princebles:
        - Resources should be discoverable through the publication of links.
- Postman: used to test APIs.
    - Gives you a status code. 
    - You can save a request onto a collection.
    - Interface is nicer.
> Swagger.io: Documenting an API.
### SOAP API:
- SOAP: Simple Object Access Protocol.
    - *ACID*: Atomicity, Consistency, Isolation, Durability.
    - *WSDL*: Web Service Description Language => contains information like data typs being used in SOAP messages, and operations available via the web service.
    - SOAP Message:
        1. Enelope.
        2. Header.
        3. Body.
        4. Fualt.
> More bandwidth is required. 
- SOAP used for for enterprised-level web services:
    - Financial services.
    - Payment gateways.
    - CRM software.
    - Identity management.
    - Telecommunication services.
> SoapUI used to test APIs
### GraphQL:
- GraphQL = Query language: a syntax describing how to ak for data, which is usually used to load data.
- Read-only operations.
- Type systems: 
    - Schema.
    - Queries.
    - Resolvers.
> Field names, Argumentns. 
> Mutation, Subscription.
> Yelp provides a GraphQL.
- GraphQL is more flexible.
- Many languages support GraphQL.












