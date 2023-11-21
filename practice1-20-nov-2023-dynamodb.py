#librerias
import boto3

num1=5
num2=6
suma=num1+num2
print(suma)

#crear funcion para listar tablas en DynamoDB
def listar_tablas():
    dynamodb = boto3.resource('dynamodb')
    for table in dynamodb.tables.all():
        print(table.name)
     

listar_tablas()

#crear funcion para sumar 2 numeros












