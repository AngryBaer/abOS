# abLaunch
Run apps from the command line

## Usage
from command line
```bash
>>> python -m abLaunch.cmd maya      # launch app in production mode
>>> python -m abLaunch.cmd maya dev  # launch app in development mode
```
from python
```python
>>> from abLaunch import run_app
>>> run_app("maya")
```