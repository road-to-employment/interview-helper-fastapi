from pydantic import BaseModel


class GenerateQuestionsRequest(BaseModel):
    userToken: str

    def toUserToken(self) -> str:
        return self.userToken
