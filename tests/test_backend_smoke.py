from pathlib import Path
import py_compile

ROOT = Path(__file__).resolve().parents[1]

def test_connection_server_compiles():
    py_compile.compile(str(ROOT / "python" / "connection_server.py"), doraise=True)

def test_backend_layout():
    assert (ROOT / "requirements.txt").exists()
    assert (ROOT / "render.yaml").exists()
    assert (ROOT / "python" / "connection_server.py").exists()
    assert (ROOT / "python" / "pipeline" / "ai.py").exists()


def test_cohere_check_connection_uses_v2_chat():
    from python.pipeline.ai import CohereService

    class FakeClient:
        def __init__(self):
            self.calls = []

        def chat(self, **kwargs):
            self.calls.append(kwargs)
            return object()

    fake = FakeClient()
    service = CohereService(api_key="test-secret", model="command-a-plus-05-2026", client=fake)
    assert service.check_connection() is True
    assert len(fake.calls) == 1
    assert fake.calls[0]["model"] == "command-a-plus-05-2026"
    assert fake.calls[0]["max_tokens"] == 8
    assert "check_api_key" not in repr(fake.calls[0])
