from pydrake.all import MultibodyPlant, DiagramBuilder, AddMultibodyPlantSceneGraph, Parser
import pydot

builder = DiagramBuilder()
plant, scene_graph = AddMultibodyPlantSceneGraph(
    builder, time_step=0.001) # The UnicodeEncodeError occurs

# plant = MultibodyPlant(0.001) # The UnicodeEncodeError does NOT happen when I use this

parser = Parser(plant)
parser.AddModels("test.sdf") 

plant.Finalize()

pydot.graph_from_dot_data(plant.GetGraphvizString())[0].write_svg("test.svg")