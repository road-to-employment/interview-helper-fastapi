from abc import ABC, abstractmethod


class GenerateQuestionsRepository(ABC):
    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel, userToken):
        pass