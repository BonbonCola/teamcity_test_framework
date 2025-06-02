#базовое исключение для всех ошибок
class AppException(Exception):
    def __init__(self, message="Базовое исключение"):
        super.__init__(message)

#специфичные исключения
class BadRequestException(AppException):
    def __init__(self, response, message="Запрос вернул не 200 статус код"):
        super.__init__(message)
        self.response = response
    
    def __str__(self):
        base_message = super.__str__()
        if self.response:
            base_massage += f"HTTP Method: {self.response.request.method}"
            base_massage += f"URL: {self.response.request.url}"
            base_massage += f"Headers: {self.response.status_code}"
            base_massage += f"Body: {self.response.text}"
        return base_massage




