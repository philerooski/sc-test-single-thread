import os
import synapseclient
synapseclient.config.single_threaded = True

def handler(e, c):
    syn = synapseclient.Synapse(configPath="/var/task/.synapseConfig")
    syn.login(os.getenv("synapseUsername"), os.getenv("synapsePassword"))
    f = synapseclient.File("/var/task/.synapseConfig", parent = "syn11657334")
    syn.store(f)
