from rest_framework.views import APIView

from .models import Cake
from .serializers import CakeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

'''
All API endpoints needed no authentication currently. This can be upgraded to use token authentication in the future. 
'''

# API endpoint to list all the cakes
@swagger_auto_schema(
    method='GET',
    operation_summary="List all Cakes",
    operation_description='''
    This endpoint makes an HTTP GET request to retrieve all available cakes. The request does not require any payload 
    in the request body. The response will have a status code of 200, and it will include an array of cakes, where each 
    cake object contains an id, name, comment, image URL, and yum factor.
    '''
)
@api_view(['GET'])  # api_view doesn't allow other methods that's not in the list
def cakes_list(request):
    cakes = Cake.objects.all()  # pagination can be applied if the list is big
    serializer = CakeSerializer(cakes, many=True)
    return Response({'cakes': serializer.data}, status=status.HTTP_200_OK)


# API endpoint to pick a particular cake using id or returns 404 not found
@swagger_auto_schema(
    method='GET',
    operation_summary="Select a Cake",
    operation_description='''
    This endpoint makes an HTTP GET request to return a particular cake. Expects path variable(path parameter) {id} for 
    identifying the particular cake. The response will include the ID, name, comment, image URL, and yum factor of the 
    cake.
    The request does not contain a request body, and the response will have a status code of 200 along with the details 
    of the cake in JSON format. It returns 404 error if the cake is not found. 
    '''
)
@api_view(['GET'])
def select_cake(request, id):
    try:
        cake = Cake.objects.get(pk=id)
    except Cake.DoesNotExist:
        return Response('404 cake not found', status=status.HTTP_404_NOT_FOUND)
    serializer = CakeSerializer(cake)
    return Response(serializer.data, status=status.HTTP_200_OK)


# API endpoint to add a new cake
# Future improvement - Token authentication(via header) will be required to perform this action
class AddCake(APIView):
    """
    Add a new cake.
    """

    @swagger_auto_schema(
        operation_summary="Add a Cake",
        operation_description='''
        This endpoint allows you to add a new cake to the system through the POST method.
        Request Body:
        name (text): The name of the cake.
        comment (text): Any additional comments about the cake.
        image_url (text): The URL of the image of the cake.
        yum_factor (text): The yum factor rating of the cake.

        Response:
        Status: 201
        id: The unique identifier of the newly added cake.
        name: The name of the cake.
        comment: Any additional comments about the cake.
        image_url: The URL of the image of the cake.
        yum_factor: The yum factor rating of the cake.
        '''
    )
    def post(self, request, format=None):
        serializer = CakeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API endpoint to delete an existing cake or return 404 not found
# Future improvement - Token authentication(via header) will be required to perform this action
@swagger_auto_schema(
    method='DELETE',
    operation_summary="Add a Cake",
    operation_description='''
    This endpoint sends an HTTP DELETE request to the specified URL to delete a cake with the {id} specified in the route 
    variable. The request does not contain a request body. Upon successful deletion, the server responds with a message: 
    'Deleted the cake' and status code of 204 - No content. 
    If the {id} of cake is not found, it returns status 404 not found error.
    '''
)
@api_view(['DELETE'])
def delete_cake(request, id):
    try:
        cake = Cake.objects.get(pk=id)
    except Cake.DoesNotExist:
        return Response('404 cake not found', status=status.HTTP_404_NOT_FOUND)

    cake.delete()
    return Response('Deleted the cake', status=status.HTTP_204_NO_CONTENT)


# API endpoint to update an existing cake or return 404 not found
# Future improvement - Token authentication(via header) will be required to perform this action
@swagger_auto_schema(
    method='PATCH',
    operation_summary="Update a Cake",
    operation_description='''
    This endpoint updates a cake in the database using PATCH method. Expects path variable {id} to
    locate a cake for updating. Also expects one or more query parameters that needs updating. 
    Returns 404 if cake not found or 400 bad request if serializer is not valid. 
    '''
)
@api_view(['PATCH'])
def update_cake(request, id):
    try:
        cake = Cake.objects.get(pk=id)
    except Cake.DoesNotExist:
        return Response('404 cake not found', status=status.HTTP_404_NOT_FOUND)

    # Update cake fields based on query parameters
    if 'name' in request.query_params:
        cake.name = request.query_params['name']
    if 'comment' in request.query_params:
        cake.comment = request.query_params['comment']
    if 'image_url' in request.query_params:
        cake.image_url = request.query_params['image_url']
    if 'yum_factor' in request.query_params:
        cake.yum_factor = request.query_params['yum_factor']

    # Validate and save the updated cake object
    serializer = CakeSerializer(cake, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(f'updated cake. \n {serializer.data}')
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# done swagger api documentation plugin ---
# possibilities to implement jwt token authentication
# todo dockerize
# todo upload to github
# todo test on priya's machine using docker