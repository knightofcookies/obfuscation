from typing import List, Sequence

from obfuscation.common_helper import create_int_range
from obfuscation.processors.modules.age_modifier.types import AgeModifierModel

age_modifier_models : List[AgeModifierModel] = [ 'styleganex_age' ]

age_modifier_direction_range : Sequence[int] = create_int_range(-100, 100, 1)
