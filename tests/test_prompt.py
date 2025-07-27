import pytest

def test_prompt_content():
    """
    Test that the .github/prompt.txt file contains the expected content.
    """
    with open('.github/prompt.txt', 'r') as f:
        prompt_content = f.read()
    
    assert 'Given feature branch is' in prompt_content
    assert 'You must execute below tasks in order:' in prompt_content
    assert '1. Find out the root cause(s) of the unit test case issues' in prompt_content
    assert '2. Create a branch' in prompt_content
    assert '3. Generate unit test case updates' in prompt_content
    assert '4. Commit the generated test files to this new branch' in prompt_content
    assert '5. Create pull request with proper details' in prompt_content
    assert 'MUST FOLLOW INSTRUCTIONS:' in prompt_content
