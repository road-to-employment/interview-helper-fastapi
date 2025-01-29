from pydantic import BaseModel


class SearchQuestionsRequestForm(BaseModel):
    userToken: str

    def toSearchQuestionsRequest(self):
        return SearchQuestionsRequest(userToken=self.userToken)