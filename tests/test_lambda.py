import importlib.util
from pathlib import Path
import json
p = Path(__file__).resolve().parents[1] / 'lambda' / 'lambda_function.py'
spec = importlib.util.spec_from_file_location('lambda_function', p)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
def test_healthcheck():
    result = module.lambda_handler({}, None)
    assert result['statusCode'] == 200
    assert json.loads(result['body'])['status'] == 'ok'
