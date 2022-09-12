import gdsfactory as gf

c = gf.components.version_stamp(labels=['demo_label'], with_qr_code=False, layer='WG', pixel_size=1, version='5.25.1', text_size=10)
c.plot()