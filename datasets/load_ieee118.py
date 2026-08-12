from vanta_lattice.adapters.pandapower.pipeline import run_pipeline
import pandapower as pp
import copy

def load_data():
    data = run_pipeline()
    return data

data = load_data()
print(data.simulated_net.load)
print(data.simulated_net.res_line)


copy_net = copy.deepcopy(data.raw_net)

copy_net.load['p_mw'] = copy_net.load['p_mw']*99
copy_net.load['q_mvar'] = copy_net.load['q_mvar']*99

print(copy_net.load)

pp.rundcpp(copy_net)
print(copy_net.res_line)

