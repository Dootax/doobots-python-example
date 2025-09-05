from doobots import Request, Response

def main(request: Request) -> Response:
    name = request.get("name")
    
    response = Response()
    response.put("greeting", f"Ola, {name}!")
    
    return response