import gdsfactory as gf

c = gf.components.add_fidutials_offsets(offsets=[[0, 100], [0, -100]])
c.plot()