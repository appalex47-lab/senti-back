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
