# -*- encoding: utf-8
# yapf: disable


checkname = 'sansymphony_virtualdiskstatus'


info = [['testvmfs01', 'Online'], ['vmfs01', 'anything else']]


discovery = {'': [('testvmfs01', None), ('vmfs01', None)]}


checks = {'': [('testvmfs01', {}, [(0, 'Volume state is: Online', [])]),
               ('vmfs01', {}, [(2, 'Volume state is: anything else', [])])]}