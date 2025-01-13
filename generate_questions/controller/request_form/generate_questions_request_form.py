from pydantic import BaseModel

from generate_questions.service.request.generate_questions_request import GenerateQuestionsRequest


class GenerateQuestionsRequestForm(BaseModel):
    userToken: str

    def toGenerateQuestionsRequest(self) -> GenerateQuestionsRequest:
        return GenerateQuestionsRequest(userToken=self.userToken)