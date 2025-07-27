import os
import boto3

def invoke_bedrock_agent(agent_id, prompt, region):
    client = boto3.client('bedrock-agent-runtime', region_name=region)
    response = client.retrieve(
        agentId=agent_id,
        inputText=prompt
    )
    print(response)
    return response

if __name__ == "__main__":
    agent_id = os.environ.get("AWS_BEDROCK_AGENT_ID")
    prompt = os.environ.get("PROMPT_TEXT")
    region = os.environ.get("AWS_REGION", "us-east-1")
    print(f"Agent ID: {agent_id}, Prompt: {prompt}, Region: {region}")
    print(f"AWS_BEDROCK_AGENT_ID: {agent_id}")
    print(f"PROMPT_TEXT: {prompt[:100]}..." if prompt else "PROMPT_TEXT: None")
    print(f"AWS_REGION: {region}")
    if not agent_id:
        print("Missing AWS_BEDROCK_AGENT_ID environment variable.")
        exit(2)
    if not prompt:
        print("Missing PROMPT_TEXT environment variable.")
        exit(2)
    try:
        invoke_bedrock_agent(agent_id, prompt, region)
    except Exception as e:
        print(f"Script failed: {e}")
        exit(2)
    invoke_bedrock_agent(agent_id, prompt, region)
