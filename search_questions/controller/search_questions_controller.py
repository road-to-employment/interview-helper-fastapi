from fastapi import Depends, status
from starlette.responses import JSONResponse

from search_questions.controller.request_form.search_questions_request_form import SearchQuestionsRequestForm
from template.include.socket_server.utility.color_print import ColorPrinter
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl


async def injectSearchQuestionsService() -> SearchQuestionsServiceImpl:
    return SearchQuestionsServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@generateQuestionsRouter.post("/generate-questions-result")
async def requestGenerateQuestionsResult(generateQuestionsRequestForm: SearchQuestionsRequestForm,
                                         generateQuestionsService: SearchQuestionsServiceImpl =
                                         Depends(injectSearchQuestionsService)):
    ColorPrinter.print_important_message("controller -> requestGenerateQuestionsResult()")

    generatedQuestions = await generateQuestionsService.requestGenerateQuestionsResult(
        generateQuestionsRequestForm.toGenerateQuestionsRequest())

    return JSONResponse(content=generatedQuestions, status_code=status.HTTP_200_OK)