import pandas as pd
import numpy as np


chat_id = 778100570 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x = x - 443
    return np.log(np.mean(x)) - np.std(x)**2 / 2
