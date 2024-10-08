import parsl
from parsl import Config
from parsl.executors.threads import ThreadPoolExecutor

# Configuring the parsl with thread pool executor
parsl_configuration = Config(executors=[ThreadPoolExecutor(max_threads=5)])


# Function to load the parsl configuration
def load_parsl_config():
    # Loading the parsl configuration
    parsl.load(parsl_configuration)
