from .viz import Brain, TimeViewer  # noqa
from .utils import Surface, verbose, set_log_level, set_log_file  # noqa
from .io import project_volume_data  # noqa

__version__ = "0.7.dev"

set_log_file()  # initialize handlers
set_log_level()  # initialize logging level
