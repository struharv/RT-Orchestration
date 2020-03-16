from Definitions import *  

def init_nodes():
  node_1 = Node([Resource("RAM", 1024), Resource("Storage", 2000)])
  node_2 = Node([Resource("RAM", 1024), Resource("Storage", 2000)])

  return [node_1, node_2]



def init_requirements():
  container_1 = Container([Resource("RAM", "500"), Resource("Storage", "200") ]);
  container_2 = Container([Resource("RAM", "500"), Resource("Storage", "200") ]);

  rt_container_1 = RtContainer([Resource("RAM", "500"), Resource("Storage", "200")],
                               [RtInterface(50, 10), RtInterface(100, 25)]);

  return [container_1, container_2, rt_container_1]




# init_requirements()
orchestrator = Orchestrator(init_nodes())
orchestrator.print_nodes()









