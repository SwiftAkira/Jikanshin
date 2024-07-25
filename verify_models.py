import os

# Base path to vosk models
base_model_path = 'C:\\Jikanshin\\vosk_models'

# List of model directories to check
model_dirs = [
    "vosk-model-ar-mgb2-0.4",
    "vosk-model-br-0.8",
    "vosk-model-small-cn-0.22",
    "vosk-model-small-cs-0.4-rhasspy",
    "vosk-model-small-de-0.15",
    "vosk-model-small-en-us-0.15",
    "vosk-model-small-en-us-zamia-0.5",
    "vosk-model-small-eo-0.42",
    "vosk-model-small-es-0.42",
    "vosk-model-small-fa-0.4",
    "vosk-model-small-fr-0.22",
    "vosk-model-small-gu-0.42",
    "vosk-model-small-hi-0.22",
    "vosk-model-small-it-0.22",
    "vosk-model-small-ja-0.22",
    "vosk-model-small-ko-0.22",
    "vosk-model-small-kz-0.15",
    "vosk-model-small-nl-0.22",
    "vosk-model-small-pl-0.22",
    "vosk-model-small-pt-0.3",
    "vosk-model-small-ru-0.22",
    "vosk-model-small-sv-rhasspy-0.15",
    "vosk-model-small-tg-0.22",
    "vosk-model-small-tr-0.3",
    "vosk-model-small-uk-v3-small",
    "vosk-model-small-uz-0.22",
    "vosk-model-small-vn-0.4",
    "vosk-model-spk-0.4",
    "vosk-model-tl-ph-generic-0.6"
]

# Check and print the contents of each model directory
for model_dir in model_dirs:
    path = os.path.join(base_model_path, model_dir)
    print(f"Checking contents of {path}:")
    if os.path.exists(path) and os.path.isdir(path):
        files = os.listdir(path)
        print(f"  Contains: {files}")
    else:
        print("  Directory does not exist or is not a directory.")
    print()
