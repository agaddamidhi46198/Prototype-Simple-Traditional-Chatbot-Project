# The Student Support Chatbot has been created with Python and the Microsoft Bot Framework to respond to questions from students based on pre-prepared rules. 
# The application provided study guidance, information about the courses, support for assignments, date and time responses, and error handling.


# Importing required libraries
import sys
import traceback
import re
from datetime import datetime

from aiohttp import web
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.core.integration import aiohttp_error_middleware
from botbuilder.integration.aiohttp import (
    CloudAdapter,
    ConfigurationBotFrameworkAuthentication,
)
from botbuilder.schema import Activity, ActivityTypes


# Setting application details
class BotConfig:
    PORT = 3978
    APP_ID = ""
    APP_PASSWORD = ""
    APP_TYPE = "MultiTenant"
    APP_TENANTID = ""


# Loading application settings
settings = BotConfig()


# Creating authentication and adapter
authentication = ConfigurationBotFrameworkAuthentication(settings)
adapter = CloudAdapter(authentication)


# Creating the student support chatbot
class StudentSupportBot(ActivityHandler):

    # Receiving and reading user messages
    async def on_message_activity(self, turn_context: TurnContext):

        # Getting user input
        user_input = turn_context.activity.text or ""

        # Removing extra spaces
        user_input = user_input.strip()

        # Converting text to lowercase
        message = user_input.lower()

        # Checking empty messages
        if not message:
            reply = "Please enter a question or type 'help'."

        # Checking invalid symbols
        elif not any(character.isalnum() for character in message):
            reply = "Invalid input. Please enter a meaningful message."

        # Checking reverse text requests
        elif message.startswith("reverse:"):
            text_value = user_input.split(":", 1)[1].strip()

            # Reversing the entered text
            if text_value:
                reply = "Reversed text: " + text_value[::-1]
            else:
                reply = "Please provide text after 'reverse:'."

        # Responding to greetings
        elif re.search(r"\b(hello|hi|hey|good morning)\b", message):
            reply = (
                "Hello! Welcome to Student Support Chatbot. "
                "How can I assist you today?"
            )

        # Displaying chatbot capabilities
        elif re.search(r"\b(help|menu|capabilities)\b", message):
            reply = (
                "I can help you with:\n"
                "1. Course information\n"
                "2. Assignment guidance\n"
                "3. Study tips\n"
                "4. Exam preparation\n"
                "5. Current date and time\n"
                "6. Reversing text\n"
                "7. General greetings\n"
                "Type a question to get started."
            )

        # Providing course information
        elif re.search(r"\b(course|subject|class)\b", message):
            reply = (
                "Course information: Check your course syllabus "
                "for topics, learning objectives, and deadlines."
            )

        # Providing assignment guidance
        elif re.search(r"\b(assignment|project|homework)\b", message):
            reply = (
                "Assignment Tip: Review the instructions carefully, "
                "plan your work, complete the implementation, "
                "test your results, and document your progress."
            )

        # Providing exam preparation tips
        elif re.search(r"\b(exam|test|quiz)\b", message):
            reply = (
                "Exam Preparation: Review lecture notes, "
                "practice important concepts, and revise regularly."
            )

        # Suggesting study methods
        elif re.search(r"\b(study|learning|revision)\b", message):
            reply = (
                "Study Tip: Use a study timetable, "
                "take short breaks, and practice consistently."
            )

        # Displaying the current date
        elif re.search(r"\b(date|today)\b", message):
            reply = (
                "Today's date is "
                + datetime.now().strftime("%B %d, %Y")
            )

        # Displaying the current time
        elif re.search(r"\b(time|clock)\b", message):
            reply = (
                "Current time: "
                + datetime.now().strftime("%I:%M %p")
            )

        # Introducing the chatbot
        elif "who are you" in message or "your name" in message:
            reply = (
                "I am Student Support Bot, developed using "
                "Python and traditional rule-based programming."
            )

        # Responding to appreciation
        elif re.search(r"\b(thank you|thanks)\b", message):
            reply = "You're welcome! Happy to help."

        # Responding to goodbye messages
        elif re.search(r"\b(bye|goodbye|exit)\b", message):
            reply = "Goodbye! Best wishes for your studies."

        # Handling unknown questions
        else:
            reply = (
                "Sorry, I do not understand that question. "
                "Type 'help' to see the available options."
            )

        # Sending the chatbot response
        await turn_context.send_activity(reply)


# Creating the chatbot object
student_bot = StudentSupportBot()


# Handling unexpected errors
async def on_error(turn_context: TurnContext, error: Exception):

    # Displaying error details
    print("Chatbot Error:", error, file=sys.stderr)
    traceback.print_exc()

    # Sending an error message
    await turn_context.send_activity(
        "Sorry, an unexpected error occurred. Please try again."
    )

    # Checking emulator connection
    if turn_context.activity.channel_id == "emulator":

        # Creating error trace details
        trace_activity = Activity(
            type=ActivityTypes.trace,
            timestamp=datetime.utcnow(),
            label="Bot Error",
            name="BotError",
            value=str(error),
            value_type="https://www.botframework.com/schemas/error",
        )

        # Sending error trace details
        await turn_context.send_activity(trace_activity)


# Assigning the error handler
adapter.on_turn_error = on_error


# Receiving messages from the emulator
async def messages(request):

    # Processing incoming messages
    return await adapter.process(request, student_bot)


# Creating the web application
app = web.Application(
    middlewares=[aiohttp_error_middleware]
)


# Registering the message endpoint
app.router.add_post("/api/messages", messages)


# Starting the chatbot server
if __name__ == "__main__":

    # Displaying server information
    print("Student Support Chatbot is starting...")
    print("Bot endpoint: http://localhost:3978/api/messages")

    # Running the chatbot application
    web.run_app(
        app,
        host="localhost",
        port=settings.PORT,
    )
