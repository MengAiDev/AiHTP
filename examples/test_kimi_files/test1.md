Sure! I'll provide a comprehensive demonstration of various methods for executing system commands in Python using the `subprocess` module and other modules like `os` and `shlex`.

```python name=execute_commands.py
import subprocess
import os
import shlex

def execute_command_with_subprocess_call(command):
    """
    Execute a system command using subprocess.call()
    """
    return subprocess.call(command, shell=True)

def execute_command_with_subprocess_run(command):
    """
    Execute a system command using subprocess.run()
    """
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr, result.returncode

def execute_command_with_subprocess_popen(command):
    """
    Execute a system command using subprocess.Popen()
    """
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    return stdout, stderr, process.returncode

def execute_command_with_os_system(command):
    """
    Execute a system command using os.system()
    """
    return os.system(command)

def execute_command_with_shlex(command):
    """
    Execute a system command using shlex.split() and subprocess.run()
    """
    args = shlex.split(command)
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout, result.stderr, result.returncode

if __name__ == "__main__":
    command = "echo Hello, World!"

    # Using subprocess.call()
    print("Using subprocess.call():")
    call_returncode = execute_command_with_subprocess_call(command)
    print(f"Return code: {call_returncode}\n")

    # Using subprocess.run()
    print("Using subprocess.run():")
    run_stdout, run_stderr, run_returncode = execute_command_with_subprocess_run(command)
    print(f"STDOUT: {run_stdout}")
    print(f"STDERR: {run_stderr}")
    print(f"Return code: {run_returncode}\n")

    # Using subprocess.Popen()
    print("Using subprocess.Popen():")
    popen_stdout, popen_stderr, popen_returncode = execute_command_with_subprocess_popen(command)
    print(f"STDOUT: {popen_stdout}")
    print(f"STDERR: {popen_stderr}")
    print(f"Return code: {popen_returncode}\n")

    # Using os.system()
    print("Using os.system():")
    os_system_returncode = execute_command_with_os_system(command)
    print(f"Return code: {os_system_returncode}\n")

    # Using shlex.split() and subprocess.run()
    print("Using shlex.split() and subprocess.run():")
    shlex_stdout, shlex_stderr, shlex_returncode = execute_command_with_shlex(command)
    print(f"STDOUT: {shlex_stdout}")
    print(f"STDERR: {shlex_stderr}")
    print(f"Return code: {shlex_returncode}\n")
```

### Explanation
- **subprocess.call()**: Executes the command and waits for it to complete.
- **subprocess.run()**: A more modern and recommended approach that provides more control and options (e.g., capturing output).
- **subprocess.Popen()**: Provides more flexibility for streaming data to and from the process.
- **os.system()**: A simpler but less flexible way to execute a command.
- **shlex.split()**: Useful for safely splitting a command into arguments; typically used with `subprocess.run()` or `subprocess.Popen()`.

This script demonstrates how to execute the same command ("echo Hello, World!") using different methods. Each method prints the standard output, standard error, and return code of the command execution.