from vanta_lattice.adapters.pandapower.pipeline import run_pipeline

def load_data():
    return run_pipeline()

data = load_data()

# Test script
print(f'Bus State: {data.mapped["bus_states"][0]}')
