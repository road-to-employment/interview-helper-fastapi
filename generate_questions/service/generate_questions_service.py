from abc import ABC, abstractmethod


class GenerateQuestionsService(ABC):
    @abstractmethod
    def requestGenerateQuestionsResult(self, generateQuestionsRequest):
        pass
