from model_utils import Choices
from enum import Enum

LANGUAGE_CHOICES = Choices(
    (0, 'en', 'English'),
    (1, 'ko', 'Korean')
)

class DATA_SOURCE(Enum):
    google = 0, "Google", LANGUAGE_CHOICES.en
    docdocdoc = 1, "청년의사", LANGUAGE_CHOICES.ko
    medigatenews = 2, "메디게이트뉴스", LANGUAGE_CHOICES.ko
    medicaltimes = 4, "메디칼타임즈", LANGUAGE_CHOICES.ko
    dailymedi = 5, "데일리메디", LANGUAGE_CHOICES.ko
    biospectator = 6, "바이오스펙테이터", LANGUAGE_CHOICES.ko
    doctorsnews = 7, "의협신문", LANGUAGE_CHOICES.ko
    yakup = 8, "약업신문", LANGUAGE_CHOICES.ko
    bosa = 9, "의학신문", LANGUAGE_CHOICES.ko
    ibric = 10, "브릭", LANGUAGE_CHOICES.ko
    biospace = 11, "Biospace", LANGUAGE_CHOICES.en
    prnewswire = 12, "PRNewswire", LANGUAGE_CHOICES.en
    globenewswire = 13, "Globenewswire", LANGUAGE_CHOICES.en
    businesswire = 14, "Businesswire", LANGUAGE_CHOICES.en
    pmlive = 15, "Pmlive", LANGUAGE_CHOICES.en
    medical_news = 16, "Medical news", LANGUAGE_CHOICES.en
    nord_news = 17, "NORD_news", LANGUAGE_CHOICES.en
    rarediseaseadvisor = 18, "RarediseaseAdvospr", LANGUAGE_CHOICES.en
    ajmc = 19, "AJMC", LANGUAGE_CHOICES.en

    def __init__(self, _: int, description: str, locale: LANGUAGE_CHOICES):
        self._value_ = _
        self._description = description
        self._locale = locale

    def __str__(self):
        return self.value

    @property
    def locale(self):
        return self._locale

    @property
    def description(self):
        return self._description
    
g = DATA_SOURCE.google

print(g.value)
# print(g._value_)
