from typing import *
import re

pattern_str: str = "c=|c-|dz=|d-|lj|nj|s=|z="

def solution() -> None:
    input_str: str = input().strip()

    num_croatic_alpha: int = len(re.findall(pattern_str, input_str))
    num_normal_alpha: int = len(re.sub(pattern_str, "", input_str))
    
    print(num_croatic_alpha + num_normal_alpha)
