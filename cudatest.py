import torch
import sys

print("Python version:", sys.version)
print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("CUDA version:", torch.version.cuda)
    print("Number of GPUs:", torch.cuda.device_count())
    for i in range(torch.cuda.device_count()):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
        print(f"  Memory: {torch.cuda.get_device_properties(i).total_memory / 1024**3:.1f} GB")
else:
    print("CUDA is not available. Possible reasons:")
    print("1. No CUDA-compatible GPU")
    print("2. CUDA drivers not installed")
    print("3. PyTorch not installed with CUDA support")
    print("4. Version mismatch between CUDA and PyTorch")

# Check if MPS (Apple Silicon) is available
if hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
    print("MPS (Apple Silicon GPU) available:", torch.backends.mps.is_available())