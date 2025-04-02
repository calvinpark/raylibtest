# raylib module initialization
import os
import sys
import glob
import importlib.util

# Try to import using the standard mechanism first
try:
    from ._raylib_cffi import ffi, lib as rl
except ImportError:
    # If that fails, try a more flexible approach with the available modules
    print("Standard import failed, trying alternative approach")
    
    # Find the appropriate CFFI module based on current Python version
    cffi_modules = glob.glob(os.path.join(os.path.dirname(__file__), "_raylib_cffi*.so"))
    if not cffi_modules:
        raise ImportError("No _raylib_cffi module found for any Python version")
    
    print(f"Available modules: {cffi_modules}")
    
    # Try each module until one works
    for module_path in cffi_modules:
        try:
            module_name = os.path.basename(module_path).split('.')[0]
            spec = importlib.util.spec_from_file_location(module_name, module_path)
            if spec is None:
                continue
                
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            # If we get here, the module loaded successfully
            ffi = module.ffi
            rl = module.lib
            print(f"Successfully loaded {module_path}")
            break
        except Exception as e:
            print(f"Failed to load {module_path}: {e}")
    else:
        # If we get here, none of the modules worked
        raise ImportError("Could not load any available _raylib_cffi module")

# The rest of the original file content
from .colors import *
from .enums import *
