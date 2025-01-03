from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from .gmail_utility import create_draft, create_message, authenticate_gmail
from agentops import record_tool


class GmailTooolInput(BaseModel):
    """Input schema for GmailTooolInput."""

    body: str = Field(..., description="Body of the email to send")


@record_tool("Gmail Tool")  # agentsops AI decorator
class GmailTool(BaseTool):
    name: str = "GmailTool"
    description: str = "Clear description for what this tool is useful for, you agent will need this information to use it."
    args_schema: Type[BaseModel] = GmailTooolInput

    def _run(self, body: str) -> str:
        service = authenticate_gmail()

        sender = ""  # input email address
        to = ""  # input email address
        subject = "Meeting Minutes"
        message_text = body

        message = create_message(sender, to, subject, message_text)
        draf = create_draft(service, "me", message)

        return "this is an example of a tool output, ignore it and move along."
