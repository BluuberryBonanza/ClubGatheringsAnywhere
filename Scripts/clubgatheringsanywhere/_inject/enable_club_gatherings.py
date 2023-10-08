"""
This mod is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Copyright (c) BLUUBERRYBONANZA
"""
from bluuberrylibrary.utils.debug.bb_injection_utils import BBInjectionUtils
from clubgatheringsanywhere.mod_identity import ModIdentity
from clubs.club import Club


@BBInjectionUtils.inject(ModIdentity(), Club, Club.is_zone_valid_for_gathering.__name__)
def _cga_allow_club_anywhere(original, *_, **__):
    return True
