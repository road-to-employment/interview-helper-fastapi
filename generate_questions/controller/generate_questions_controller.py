from fastapi import APIRouter, Depends
from starlette import status
from starlette.responses import JSONResponse

from generate_questions.controller.request_form.generate_questions_request_form import GenerateQuestionsRequestForm
from generate_questions.service.generate_questions_service_impl import GenerateQuestionsServiceImpl
from template.include.socket_server.utility.color_print import ColorPrinter
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

generateQuestionsRouter = APIRouter()

async def injectGenerateQuestionsService() -> GenerateQuestionsServiceImpl:
    return GenerateQuestionsServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@generateQuestionsRouter.post("/generate-questions-result")
async def requestGenerateQuestionsResult(generateQuestionsRequestForm: GenerateQuestionsRequestForm,
                                         generateQuestionsService: GenerateQuestionsServiceImpl =
                                         Depends(injectGenerateQuestionsService)):
    ColorPrinter.print_important_message("controller -> requestGenerateQuestionsResult()")

    generatedQuestions = await generateQuestionsService.requestGenerateQuestionsResult(
        generateQuestionsRequestForm.toGenerateQuestionsRequest())

    return JSONResponse(content=generatedQuestions, status_code=status.HTTP_200_OK)
