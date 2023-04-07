import pandas as pd
import numpy as np


chat_id = 778100570 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    x = np.log(x)
    return np.mean(x)
