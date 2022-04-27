# Clientes_API

1. Activate the virtual environment: `venv/Scripts/Activate`
   <br />
   (In case you don't have it, create a new one: `python -m venv venv`)
2. Install all the necessary packages from the requirements.txt file: `pip install -r requirements.txt`
4. Run the local server with the manage.py file located in the backend folder: `python manage.py runserver 8000`
5. To create a new client, enter to POSTMAN and send a POST request to the url: localhost:8000/clientes/ ![Captura de pantalla (406)](https://user-images.githubusercontent.com/65636793/165578200-2d83e005-ae61-42b4-b3e6-77dab0454d22.png)
6. To see this recently created client and the list of client, enter to POSTMAN and send a GET request to the url: localhost:8000/clientes/ ![Captura de pantalla (407)](https://user-images.githubusercontent.com/65636793/165578747-100c3338-6b51-494a-8f20-365e208ab081.png)
7. To update the data of the 1st client, enter to POSTMAN and send a PUT request to the url: localhost:8000/clientes/1/update/![Captura de pantalla (408)](https://user-images.githubusercontent.com/65636793/165579076-9a9e01bf-6d8a-49bf-a336-3bb62e6f2020.png)
8. To check these changes in the list of clients, enter to POSTMAN and send again a GET request to the url: localhost:8000/clientes/![Captura de pantalla (409)](https://user-images.githubusercontent.com/65636793/165579350-140e30af-4e19-4631-af7d-e7ce8a9c603e.png)
9. To delete the 1st client, enter to POSTMAN and send a DELETE request to the url: localhost:8000/clientes/1/delete/![Captura de pantalla (410)](https://user-images.githubusercontent.com/65636793/165579639-5a4d4f84-159d-479d-a1f6-25c81708d34f.png)
10. To check if the 1st client was deleted, enter to POSTMAN and send again a GET request to the url: localhost:8000/clientes/![Captura de pantalla (411)](https://user-images.githubusercontent.com/65636793/165579907-0dc7fde6-3b84-44d8-a00b-25a22d99f00b.png)

Also to check field validations we can send a POST request with blanks and wrong formats: ![Captura de pantalla (412)](https://user-images.githubusercontent.com/65636793/165580395-b675cb5a-700a-4bb4-ab75-1a09079be5ea.png)
... and the API will ask you to enter valid fields: ![Captura de pantalla (419)](https://user-images.githubusercontent.com/65636793/165580527-a2146970-de85-444b-b09e-c1864804467a.png)
