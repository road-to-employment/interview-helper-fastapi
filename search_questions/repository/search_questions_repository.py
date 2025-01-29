from abc import ABC, abstractmethod


class SearchQuestionsRepository(ABC):
    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel, userToken):
        pass