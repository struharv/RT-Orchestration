class Resource:
  def __init__(self, name, value):
    self.name = name
    self.value = value

class RtInterface:
  def __init__(self, period, quota):
    self.period = period
    self.quota = quota


class Container(object):
  def __init__(self, resources):
    self.resources = resources

  def __str__(self):
    return "Container"
    
class RtContainer(Container):
    def __init__(self, resources, rt_interfaces):
      super(RtContainer, self).__init__(resources)
      self.rt_interfaces = rt_interfaces
  
class Node:
  def __init__(self, resources):
    self.resources_total = resources
    self.containers = []
  
  def __str__(self):
    res = ""    
    for c in self.containers:
      res += c.toString()
    
    return res
    

class Orchestrator:
  def __init__(self, nodes):
    self.nodes = nodes

  def print_nodes(self):
    for node in self.nodes:
      print node
  

  def placement(self):
    pass

