from google.adk import Agent
from google.adk.tools import google_search
import subprocess


def deploy_application():
    """
    Deploy application from GitHub deployment YAML
    """

    try:
        result = subprocess.run(
            ["kubectl", "apply", "-f", "manifests/nginx-deployment.yaml"],
            capture_output=True,
            text=True
        )

        return result.stdout + result.stderr

    except Exception as e:
        return str(e)


root_agent = Agent(
    model='gemini-2.5-flash',

    name='root_agent',

    description='AI deployment and travel assistant.',

    instruction=(
        "Your name is James. "
        "If the user asks to deploy nginx application, "
        "use deployment tool. "
        "For Hyderabad tourism questions use Google Search."
    ),

    tools=[google_search, deploy_application]
)
