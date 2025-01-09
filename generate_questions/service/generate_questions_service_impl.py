import os
import sys

from generate_questions.repository.generate_questions_repository_impl import GenerateQuestionsRepositoryImpl
from generate_questions.service.generate_questions_service import GenerateQuestionsService
from template.include.socket_server.utility.color_print import ColorPrinter
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

class GenerateQuestionsServiceImpl(GenerateQuestionsService):
    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__generateQuestionsRepository = GenerateQuestionsRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    async def requestGenerateQuestionsResult(self, generateQuestionsRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return await self.__generateQuestionsRepository.getResult(userDefinedReceiverFastAPIChannel,
                                                                  generateQuestionsRequest.toUserToken())
