import kagglehub #type: ignore
import shutil
from pathlib import Path

# 1) Descarga (cache interna de kagglehub)
cache_path = kagglehub.dataset_download(
    "uciml/default-of-credit-card-clients-dataset"
)

print("Cache path:", cache_path)

# 2) Carpeta destino en tu proyecto
dest = Path("../data/raw")
dest.mkdir(parents=True, exist_ok=True)

# 3) Dataset -> destino
shutil.copytree(cache_path, dest, dirs_exist_ok=True)

print("Dataset copiado a:", dest.resolve())