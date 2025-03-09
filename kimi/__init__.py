print("welcome to kimi!")

# check if openai was installed

import importlib

def is_library_installed(library_name):
    try:
        importlib.import_module(library_name)
        # print(f"The {library_name} library is installed.")
        return True
    except ImportError:
        # print(f"The {library_name} library is not installed.")
        return False
    
# print(is_library_installed("openai"))

print("check openai...")
if not is_library_installed("openai"):
    print("library openai is not installed, please run pip install openai")
    quit()

else:
    print("library openai is installed, you can run kimi now.")