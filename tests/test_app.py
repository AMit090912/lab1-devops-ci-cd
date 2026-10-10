from pathlib import Path

def test_app_has_http_server():
    source = Path("app.py").read_text()
    assert "HTTPServer" in source
    assert "Lab 1 CI/CD deployment is working!" in source
