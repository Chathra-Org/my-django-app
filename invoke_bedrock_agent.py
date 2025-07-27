import os
import boto3
import logging
from typing import Dict, Any
# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def invoke_agent(client, agent_id, alias_id, prompt, session_id):
        response = client.invoke_agent(
            agentId=agent_id,
            agentAliasId=alias_id,
            enableTrace=True,
            sessionId = session_id,
            inputText=prompt,
            streamingConfigurations = { 
    "applyGuardrailInterval" : 20,
      "streamFinalResponse" : False
            }
        )
        completion = ""
        print(f"The response is {response}")
        for event in response.get("completion"):
            #Collect agent output.
            if 'chunk' in event:
                chunk = event["chunk"]
                completion += chunk["bytes"].decode()
            
            # Log trace output.
            if 'trace' in event:
                trace_event = event.get("trace")
                trace = trace_event['trace']
                for key, value in trace.items():
                    logging.info("%s: %s",key,value)
                    print(f"printing trace output: {key}: {value}")

        print(f"Agent response: {completion}")


if __name__ == "__main__":
    agent_id = os.environ.get("AWS_BEDROCK_AGENT_ID")
    #read from first python argument
    prompt = os.environ.get("PROMPT_TEXT")
    region = os.environ.get("AWS_REGION", "us-east-1")
    session_id = os.environ.get("AWS_BEDROCK_SESSION_ID", "default-session")
    alias_id = os.environ.get("AWS_BEDROCK_AGENT_ALIAS_ID", "default-alias")
    print(f"Agent ID: {agent_id}, Prompt: {prompt}, Region: {region}, Session ID: {session_id}")
    print(f"AWS_BEDROCK_AGENT_ID: {agent_id}")
    print(f"PROMPT_TEXT: {prompt[:100]}..." if prompt else "PROMPT_TEXT: None")
    print(f"AWS_REGION: {region}")
    print(f"AWS_BEDROCK_SESSION_ID: {session_id}")
    client = boto3.client(service_name="bedrock-agent-runtime", region_name=region)
    if not agent_id:
        print("Missing AWS_BEDROCK_AGENT_ID environment variable.")
        exit(2)
    if not prompt:
        print("Missing PROMPT_TEXT environment variable.")
        exit(2)
    try:
        invoke_agent(client, agent_id, alias_id, prompt, session_id)
    except Exception as e:
        print(f"Script failed: {e}")
        exit(2)
