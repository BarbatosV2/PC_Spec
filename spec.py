import platform
import psutil
import GPUtil
import cpuinfo

def get_wifi_info():
    system_platform = platform.system()

    if system_platform == "Windows":
        import wmi

        wmi_obj = wmi.WMI()
        adapters = wmi_obj.Win32_NetworkAdapter()
        wifi_adapters = [adapter for adapter in adapters if "Wireless" in adapter.Name]

        if wifi_adapters:
            wifi_info = f"WiFi Adapter: {wifi_adapters[0].Name}"
        else:
            wifi_info = "No WiFi adapter found."

    elif system_platform == "Linux":
        # Note: This assumes you have the 'iwconfig' command available
        import subprocess

        try:
            iwconfig_output = subprocess.check_output(["iwconfig"], universal_newlines=True)
            wifi_adapter_line = next(line for line in iwconfig_output.splitlines() if "IEEE 802.11" in line)
            wifi_adapter_name = wifi_adapter_line.split(" ")[0]
            wifi_info = f"WiFi Adapter: {wifi_adapter_name}"
        except Exception as e:
            wifi_info = "Error retrieving WiFi information."

    else:
        wifi_info = "WiFi information not available for this platform."

    return wifi_info

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

    # Get WiFi information
    wifi_info = get_wifi_info()

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
    print(wifi_info)

if __name__ == "__main__":
    get_system_info()
