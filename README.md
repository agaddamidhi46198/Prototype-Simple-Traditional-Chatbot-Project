# Prototype-Simple-Traditional-Chatbot-Project
## Student Support Chatbot

### Project Overview

The Student Support Chatbot has been built with Python and Microsoft Bot Framework based on the traditional rule-based approach. The application provided fundamental academic aid without the use of large language models or generative artificial intelligence by providing predefined responses to the queries. The chatbot was able to provide greetings, course information, help with assignments, study tips, information on the current date and time, and even help with text reversal. Input validation and error handling were also added to handle invalid messages and unsupported questions.

### Project Objectives

The primary goal was to create a basic chatbot that could answer a variety of questions based on a set of rules. The work involved the development of a project that included the implementation of the academic supports, showcasing the chatbot's functionality, dealing with incorrect inputs, and giving appropriate answers. The application was also designed to be expandable for future enhancements and potential integration with more sophisticated AI services.

### Technologies Used

The project was created with the help of Python 3.8.2, Anaconda, Microsoft Bot Framework, aiohttp, and Visual Studio Code. Environment management was accomplished with Anaconda, and conversation processing was achieved with the help of Microsoft Bot Framework. The aiohttp library was used for communication with the local web server, and Bot Framework Emulator was used for testing the local bot.

### Development Environment Setup

Anaconda is used to create a separate environment called MSAI631_MBF to run Python applications without conflicts in the environment. Python 3.8.2 was chosen for the project. The following command was used to create the environment:

- conda create -- name MSAI631_MBF python=3.8.2

The environment was activated using the following command:

- conda activate MSAI631_MBF

### Installing Required Libraries

The necessary Python libraries were installed to enable the development of the chatbot and the communication with the Microsoft Bot Framework Emulator. Dependencies of the project were added into the requirements.txt file to make packages easier to install. The required packages were installed using the following command:

- pip install -r requirements.txt

During the installation, the environment was prepared for running the chatbot application and processing incoming messages.

### Chatbot Development and Implementation

The Student Support Chatbot was created with the help of conditional statements and regular expressions to identify and recognize the messages from users. The application received text input, stripped out any unnecessary spaces, and turned the text into lower case to facilitate comparison. Greetings, academic questions, help requests, date and time queries and text reversal requests were identified using predefined rules. The StudentSupportBot class handled the interaction between the students and the chatbot, and the on_message_activity function received the user's message and returned an appropriate answer.

### Chatbot Features

The chatbot had some features that offered basic academic support. The greeting messages were able to get a reaction, and the help command showed the capabilities of the program. Course-related questions provided syllabus guidance, and assignment questions returned suggestions for planning, implementation, and documentation. Preparation tips were derived from study and examination questions. Other features were the ability to show the current time and date, reverse text, send thank-you responses and goodbye messages.

### Input Validation and Error Handling

Empty messages, invalid symbols and unsupported questions were detected by input validation. Empty messages resulted in a Request for valid input message, and symbol-only messages resulted in an Invalid-input response. When an unknown question was returned, a default message was given that indicated that the help option might be useful. Further error handling was added to show unexpected errors in the development terminal, and to give appropriate responses in the chatbot interface.

### Running the Chatbot Application

The chatbot application was deployed locally by a web server using port 3978. The application started the Microsoft Bot Framework components and registered a message endpoint for handling conversations with the chatbot. The application was started from the project directory using the following command:

- python app.py

A Bot Service was set up using the Microsoft Bot Framework Emulator to receive messages and return responses from the chatbot.

### Connecting to Bot Framework Emulator

The chatbot was tested locally using the Microsoft Bot Framework Emulator, before being deployed on a cloud platform. The emulator was linked to the chatbot running via the following endpoint:

- http://localhost:3978/api/messages

The endpoint was used to communicate between the chatbot application and emulator. The connection enabled predefined responses, message processing and handling of invalid input to be studied via the conversation interface.

### Chatbot Testing

The chatbot testing process focused on different user messages and expected responses. The input hello should have produced the output hello, welcome, and help should have shown the list of what the chatbot can do. Academic enquiries including assignment, course and study tips were expected to give the appropriate guidance. The input reverse: Python was expected to return Reversed text: nohtyP. Responses to invalid messages (e.g. ???; unsupported questions) were expected. The chosen test cases enabled the evaluation of rules for answering the questions by chatbot and the handling of the conversation.

### Implementation Challenges

The project focused on technical aspects such as Configuring the environment, package compatibility, and integration with Microsoft Bot Framework. Python 3.8.2 was chosen to meet the required development needs and Anaconda was employed as a dependency manager. It is crucial to get the message endpoint and server port right to communicate with Bot Framework Emulator. Traditional keyword matching was also not effective in recognizing novel questions. Basic limitations in message processing were handled by the use of regular expressions, input validation and fallback responses.

### Knowledge Gained

The project offered hands-on experience with traditional chat bot development with Python and Microsoft Bot Framework. Environment management, dependency installation, conditional statement, regular expression, message processing and error handling were important concepts. The development process also highlighted the value of pre-established response rules, and local testing. The project demonstrated the shortcomings of conventional chatbots in handling queries that were not in their vocabulary, and set a precedent for the development of more sophisticated conversational technology.

### Future Improvements

There is scope for future development of academic topics, rules for responses and recognizing different question formats. More advanced conversation capabilities may be achievable with integration with Azure AI services or natural language processing tools. Further testing, better documentation and error handling can also help ensure the reliability and maintenance of the application.

### Conclusion

The Student Support Chatbot project was a great example on how to create a classic rule-based chatbot with Python and Microsoft Bot Framework. It involved academic support, rules for conversation, turning the text around, sealing the input and handling errors. The project involved the set-up of the environments, installation of libraries, development of chatbots, local execution, and preparation for testing. This application set the stage for further enhancements and potential integration with sophisticated artificial intelligence applications.
