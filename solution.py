import pandas as pd
import numpy as np


chat_id = 345534690 # Ваш chat ID, не меняйте название переменной


import numpy as np
from scipy.stats import ks_2samp

def solution(x: np.array, y: np.array) -> bool:
    """
    Функция принимает две выборки параметра F и возвращает bool-значение,
    отвечая на вопрос: "Отклонить ли гипотезу однородности выборок на заданном уровне значимости".
    
    Параметры:
    - x (np.array): Первая выборка параметра F.
    - y (np.array): Вторая выборка параметра F.
    
    Возвращаемое значение:
    - bool: True, если гипотеза об однородности выборок отклонена на уровне значимости 0.1, иначе False.
    """
    # Уровень значимости
    alpha = 0.1
    
    # Проведение теста Колмогорова-Смирнова
    stat, p_value = ks_2samp(x, y)
    
    # Проверка, отклоняется ли нулевая гипотеза на уровне значимости 0.1
    return p_value < alpha
