from enum import Enum


class Role(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class Model(Enum):
    GPT35TURBO = "ft:gpt-3.5-turbo-0125:ochanomizu-university:emotion0-prediction:AMoI7Wts"
