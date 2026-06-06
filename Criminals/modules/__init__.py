import logging
from pathlib import Path

logger = logging.getLogger("criminals.modules")

module_dir = Path(__file__).parent
modules = [f.stem for f in module_dir.glob("*.py") if f.name != "__init__.py" and not f.name.startswith("_")]

logger.info(f"📦 Loading {len(modules)} module(s)...")

for mod in modules:
    try:
        __import__(f"Criminals.modules.{mod}")
        logger.info(f"✅ {mod}")
    except Exception as e:
        logger.error(f"❌ {mod}: {e}")

logger.info("✅ Modules loaded")
