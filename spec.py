import platform
import psutil
import GPUtil

def get_system_info():
    # Get CPU information
    cpu_info = platform.processor()

    # Get memory (RAM) information
    memory = psutil.virtual_memory()
    total_memory = round(memory.total / (1024 ** 3), 2)  # Convert to GB

    # Get operating system information
    os_info = f"{platform.system()} {platform.release()} {platform.architecture()[0]}"

    # Get GPU information
    try:
        gpu = GPUtil.getGPUs()[0]
        gpu_info = f"{gpu.name} (VRAM: {gpu.memoryTotal} MB)"
    except Exception as e:
        gpu_info = "No NVIDIA GPU found"  # Handle the case where no NVIDIA GPU is present

    # Display the information
    print("System Information:")
    print(f"CPU: {cpu_info}")
    print(f"Total Memory (RAM): {total_memory} GB")
    print(f"Operating System: {os_info}")
    print(f"GPU: {gpu_info}")

if __name__ == "__main__":
    get_system_info()
