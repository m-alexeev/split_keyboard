from kmk.modules.layers import Layers as _Layers
from configs import HUES, rgb


class Layers(_Layers):
    last_top_layer = 0
    hues = HUES

    def after_hid_send(self, keyboard):
        if keyboard.active_layers[0] != self.last_top_layer:
            self.last_top_layer = keyboard.active_layers[0]
            rgb.set_hsv_fill(self.hues[self.last_top_layer], 255, 255)


layers = Layers()
