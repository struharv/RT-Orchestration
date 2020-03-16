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

class RtContainer(Container):
    def __init__(self, resources, rt_interfaces):
      super(RtContainer, self).__init__(resources)
      self.rt_interfaces = rt_interfaces
  
class Node:
  def __init__(self, resources):
    self.resources_total = resources
    self.containers = []
    

class Orchestrator:
  def __init__(self, nodes, requirements):
    self.nodes = []


  def placement():
    pass

