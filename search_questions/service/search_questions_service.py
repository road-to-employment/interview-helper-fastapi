from abc import ABC, abstractmethod


class SearchQuestionsService(ABC):
    @abstractmethod
    def requestSearchQuestionsResult(self, searchQuestionsRequest):
        pass
