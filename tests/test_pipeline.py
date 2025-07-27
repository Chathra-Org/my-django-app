import pytest
import yaml

def test_pipeline_configuration():
    """
    Test that the .github/workflows/pipeline.yml file contains the expected configuration.
    """
    with open('.github/workflows/pipeline.yml', 'r') as f:
        pipeline_config = yaml.safe_load(f)
    
    assert 'name' in pipeline_config
    assert pipeline_config['name'] == 'Run Pytest for Django'
    
    assert 'on' in pipeline_config
    assert 'push' in pipeline_config['on']
    assert 'branches' in pipeline_config['on']['push']
    assert 'main' in pipeline_config['on']['push']['branches']
    assert 'feature/**' in pipeline_config['on']['push']['branches']
    assert 'unit-tests/**' in pipeline_config['on']['push']['branches']
    
    assert 'pull_request' in pipeline_config['on']
    assert 'branches' in pipeline_config['on']['pull_request']
    assert 'main' in pipeline_config['on']['pull_request']['branches']
    assert 'feature/**' in pipeline_config['on']['pull_request']['branches']
    assert 'unit-tests/**' in pipeline_config['on']['pull_request']['branches']
    
    assert 'jobs' in pipeline_config
    assert 'test' in pipeline_config['jobs']
    assert 'runs-on' in pipeline_config['jobs']['test']
    assert pipeline_config['jobs']['test']['runs-on'] == 'ubuntu-latest'
    
    assert 'steps' in pipeline_config['jobs']['test']
    assert len(pipeline_config['jobs']['test']['steps']) == 7
    
    assert pipeline_config['jobs']['test']['steps'][0]['name'] == '📥 Checkout code'
    assert pipeline_config['jobs']['test']['steps'][1]['name'] == '🐍 Set up Python'
    assert pipeline_config['jobs']['test']['steps'][2]['name'] == '📦 Install dependencies'
    assert pipeline_config['jobs']['test']['steps'][3]['name'] == '🧹 Run pytest'
    assert pipeline_config['jobs']['test']['steps'][4]['name'] == '📊 Upload test results'
    assert pipeline_config['jobs']['test']['steps'][5]['name'] == '💾 Save custom prompt variable'