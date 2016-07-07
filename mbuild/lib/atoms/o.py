import numpy as np

import mbuild as mb


class O(mb.Compound):
    """An oxygen atom with two overlayed ports."""
    def __init__(self):
        super(O, self).__init__()

        self.add(mb.Particle(name='O'))

        self.add(mb.Port(anchor=self[0]), 'up')
        mb.translate(self['up'], np.array([0, 0.07, 0]))

        self.add(mb.Port(anchor=self[0]), 'down')
        mb.translate(self['down'], np.array([0, 0.07, 0]))
        mb.rotate_around_z(self['down'], np.pi * 2/3)

if __name__ == '__main__':
    m = O()
    m.visualize(show_ports=True)
