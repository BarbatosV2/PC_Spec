import platform
import psutil
import GPUtil
import cpuinfo
import platform

def get_system_info():
    # Get CPU information
    cpu_info = cpuinfo.get_cpu_info()
    cpu_name = cpu_info['brand_raw']
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)

    # Get memory (RAM) information
    memory = psutil.virtual_memory()
    total_memory = round(memory.total / (1024 ** 3), 2)  # Convert to GB
    used_memory = round(memory.used / (1024 ** 3), 2)  # Convert to GB
    available_memory = round(memory.available / (1024 ** 3), 2)  # Convert to GB

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
    print(f"CPU: {cpu_name}")
    print(f"CPU Cores: {cpu_cores}")
    print(f"CPU Threads: {cpu_threads}")
    print(f"Total Memory (RAM): {total_memory} GB")
    print(f"Used Memory: {used_memory} GB")
    print(f"Available Memory: {available_memory} GB")
    print(f"Operating System: {os_info}")
    print(f"GPU: {gpu_info}")

if __name__ == "__main__":
    get_system_info()
