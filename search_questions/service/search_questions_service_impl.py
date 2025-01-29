import os
import sys

from search_questions.service.search_questions_service import SearchQuestionsService
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

class SearchQuestionsServiceImpl(SearchQuestionsService):
    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__searchQuestionsRepository = SearchQuestionsRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    async def requestSearchQuestionsResult(self, searchQuestionsRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        return await self.__searchQuestionsRepository.getResult(userDefinedReceiverFastAPIChannel,
                                                                  searchQuestionsRequest.toUserToken())