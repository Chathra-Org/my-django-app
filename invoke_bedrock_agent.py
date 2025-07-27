import os
import boto3

def invoke_bedrock_agent(agent_id, prompt, session_id, region):
    client = boto3.client('bedrock-agent-runtime', region_name=region)
    print(f"Invoking agent with ID: {agent_id}, session ID: {session_id}")
    response = client.invoke_agent(
        agentId=agent_id,
        sessionId=session_id,
        inputText=prompt,
        agentAliasId=os.environ.get("AWS_BEDROCK_AGENT_ALIAS_ID", "default-alias"),
    )
    print("Agent response:")
    print(response)
    return response

if __name__ == "__main__":
    agent_id = os.environ.get("AWS_BEDROCK_AGENT_ID")
    #read from first python argument
    prompt = os.environ.get("PROMPT_TEXT")
    region = os.environ.get("AWS_REGION", "us-east-1")
    session_id = os.environ.get("AWS_BEDROCK_SESSION_ID", "default-session")
    print(f"Agent ID: {agent_id}, Prompt: {prompt}, Region: {region}, Session ID: {session_id}")
    print(f"AWS_BEDROCK_AGENT_ID: {agent_id}")
    print(f"PROMPT_TEXT: {prompt[:100]}..." if prompt else "PROMPT_TEXT: None")
    print(f"AWS_REGION: {region}")
    print(f"AWS_BEDROCK_SESSION_ID: {session_id}")
    if not agent_id:
        print("Missing AWS_BEDROCK_AGENT_ID environment variable.")
        exit(2)
    if not prompt:
        print("Missing PROMPT_TEXT environment variable.")
        exit(2)
    try:
        invoke_bedrock_agent(agent_id, prompt, session_id, region)
    except Exception as e:
        print(f"Script failed: {e}")
        exit(2)
