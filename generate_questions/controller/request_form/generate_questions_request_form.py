from pydantic import BaseModel


class GenerateQuestionsRequestForm(BaseModel):
    userToken: str

    def toGenerateQuestionsRequest(self) -> GenerateQuestionRequest:
        return GenerateQuestionsRequest(userToken=self.userToken)