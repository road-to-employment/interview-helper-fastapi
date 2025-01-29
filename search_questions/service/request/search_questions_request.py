from pydantic import BaseModel


class SearchQuestionsRequest(BaseModel):
    userToken: str

    def toUserToken(self):
        return self.userToken