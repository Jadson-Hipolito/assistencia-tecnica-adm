import os
import sys
import compileall
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

print("=== DIAGNÓSTICO DE COMPILAÇÃO ===\n")

# 1. Verificar estrutura
print("📁 Estrutura do projeto:")
for root, dirs, files in os.walk("backend/app"):
    level = root.count(os.sep) - 2
    indent = "  " * level
    print(f"{indent}📂 {os.path.basename(root)}/")
    subindent = "  " * (level + 1)
    for file in files[:3]:  # Mostrar apenas 3 arquivos por pasta
        if file.endswith('.py'):
            print(f"{subindent}📄 {file}")

# 2. Compilar todos os arquivos
print("\n🔧 Compilando todos os arquivos...")
success = compileall.compile_dir('backend/app', force=True, quiet=1)
if success:
    print("✅ Todos os arquivos compilados com sucesso!")
else:
    print("❌ Erros de compilação encontrados")

# 3. Testar importações críticas
print("\n📦 Testando importações:")
try:
    import backend.app.core.config as config_module
    print(f"  ✅ config.py ({config_module.__name__})")
except Exception as e:
    print(f"  ❌ config.py: {e}")

try:
    import backend.app.core.database as database_module
    print(f"  ✅ database.py ({database_module.__name__})")
except Exception as e:
    print(f"  ❌ database.py: {e}")

try:
    from backend.app.main import app
    print("  ✅ main.py")
except Exception as e:
    print(f"  ❌ main.py: {e}")

print("\n🎉 Testes concluídos!")