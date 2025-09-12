from doobots import Request, Response
import base64

def main(request: Request) -> Response:
    name = request.get("name")
    test_file_base64 = request.get_file("teste.txt").base64
    test_file_content = base64.b64decode(test_file_base64).decode("utf-8")

    response = Response()
    response.put("greeting", f"Ola, {name}!")
    response.put("fileContent", test_file_content)
    
    return response