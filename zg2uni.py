# -*- coding: utf-8 -*-
import re

def re_sub(pattern, replacement, string):
    def _r(m):
        class _m():
            def __init__(self, m):
                self.m=m
                self.string=m.string
            def group(self, n):
                return m.group(n) or ""

        return re._expand(pattern, _m(n), replacement)

    return re.sub(pattern, _r, string) 


def convert(input):
	tallAA = u'\u102B'
	AA = u'\u102C'
	vi = u'\u102D'
	# lone gti tin
	ll = u'\u102E'
	v = u'\u102F'
	uu = u'\u1030'
	ve = u'\u1031'
	ai = u'\u1032'
	ans = u'\u1036'
	db = u'\u1037'
	visarga = u'\u1038'

	asat = u'\u103A'

	ya = u'\u103B'
	ra = u'\u103C'
	wa = u'\u103D'
	ha = u'\u103E'
	zero = u'\u1040'
	output = input

	output = output.replace(u'\u106A', u'\1009')
	#  nya lay

	output = output.replace(u'\u106B', u'\u100A')
	#  nya

	output = output.replace(u'\u103D', u'\u103E')
	output = output.replace(u'\u1087', u'\u103E')
	#  hahtoe

	output = output.replace(u'\u103C', u'\u103D')
	#  wa swae

	output = output.replace(u'\u103B', u'\u103C')
	output = output.replace(u'\u107E', u'\u103C')
	output = output.replace(u'\u107F', u'\u103C')
	output = output.replace(u'\u1080', u'\u103C')
	output = output.replace(u'\u1081', u'\u103C')
	output = output.replace(u'\u1082', u'\u103C')
	output = output.replace(u'\u1083', u'\u103C')
	output = output.replace(u'\u1084', u'\u103C')
	#  ya yit

	output = output.replace(u'\u103A', u'\u103B')
	output = output.replace(u'\u107D', u'\u103B')
	#  ya pin

	output = output.replace(u'\u1039', u'\u103A')
	#  athet

	output = output.replace(u'\u1090', u'\u101B')
	#  ya kaut

	output = output.replace(u'\u108F', u'\u1014')
	#  nanage

	output = output.replace(u'\u1097', u'\u100B')
	#  datalin


	output = output.replace(u'\u1033', u'\u102F')
	#  onechaung
	output = re.sub(u'\u1060', u'\u1039\u1000', output) # ka_gyi
        output = re.sub(u'\u1060', u'\u1039\u1001', output) # ka_kwae

     
        





	return output
