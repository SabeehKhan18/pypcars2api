import mmap
from pypcars2api.models import GameInstance
from pypcars2api.definitions import SHARED_MEMORY_VERSION

def _get_mmapped():
    # could we use ctypes.sizeof(GameInstance) instead here? A too large value results in access denied,
    # 8k works for now
    return mmap.mmap(0, 11624, tagname='$pcars2$', access=mmap.ACCESS_READ)

def _validate_instance(instance):
    if instance.mVersion != SHARED_MEMORY_VERSION:
        #
        #Mismatch between library data structure version and game data structure version.
        #Retrieve new SharedMemory.h and run bin/generate_classes.py to regenerate the definitions file.
        return False

    return instance

def get_shared_memory_version():
    return SHARED_MEMORY_VERSION

def get_mversion():
    return GameInstance.from_buffer(_get_mmapped()).mVersion

def get_mcarname():
    return GameInstance.from_buffer(_get_mmapped()).mCarName

def live():
    return _validate_instance(GameInstance.from_buffer(_get_mmapped()))

def snapshot():
    return _validate_instance(GameInstance.from_buffer_copy(_get_mmapped()))

class InvalidSharedMemoryVersionException(Exception):
    pass
