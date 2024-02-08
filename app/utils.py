from django.http import HttpResponse
from django.core.validators import EmailValidator, MinLengthValidator
from django.core.exceptions import ValidationError


def validate_first_name(first_name: str):
    if first_name == "":
        return ["Tus nombres no pueden estar vacíos."]
    return []


def validate_last_name(last_name: str):
    if last_name == "":
        return ["Tus apellidos no pueden estar vacíos."]
    return []


def validate_dni(dni: str):
    errors = []
    if dni == "":
        errors.append("El DNI no puede estar vacío.")
    if not dni.isnumeric():
        errors.append("El DNI debe ser un número.")
    return errors


def validate_cellphone(cellphone: str):
    errors = []
    cellphone = cellphone.replace("-", "")
    if cellphone == "":
        errors.append("El número de celular no puede estar vacío.")
    if not cellphone.isnumeric():
        errors.append("El valor debe ser un número.")
    return errors


def validate_email(email):
    email_validators = [
        EmailValidator(message="Escribe un e-mail válido"),
        MinLengthValidator(
            limit_value=1, message="El e-mail no puede estar vacío."
        )
    ]
    errors = []
    for validator in email_validators:
        try:
            validator(email)
        except ValidationError as e:
            errors.append(e.message)
    return errors


def validate_password(password, **kwargs):
    password_validators = [
        MinLengthValidator(
            limit_value=1, message="La contraseña no puede estar vacía."
        )
    ]
    errors = []
    for validator in password_validators:
        try:
            validator(password)
        except ValidationError as e:
            errors.append(e.message)
    return errors


def login_form_validation(email, password):
    email_errors = validate_email(email)
    password_errors = validate_password(password)

    return {
        "email_errors": email_errors,
        "password_errors": password_errors
    }


def register_form_validation(
    email,
    first_name,
    last_name,
    dni,
    date_of_birth,
    cellphone,
    password1,
    password2,
    field,
):
    errors = {
        "email_errors": [],
        "first_name_errors": [],
        "last_name_errors": [],
        "dni_errors": [],
        "date_of_birth_errors": [],
        "cellphone_errors": [],
        "password_errors": []
    }
    if field == "email":
        errors["email_errors"] = validate_email(email)
    elif field == "first_name":
        errors["first_name_errors"] = validate_first_name(first_name)
    elif field == "last_name":
        errors["last_name_errors"] = validate_last_name(last_name)
    elif field == "dni":
        errors["dni_errors"] = validate_dni(dni)
    elif field == "cellphone":
        errors["cellphone_errors"] = validate_cellphone(cellphone)
    elif field == "password1":
        errors["password_errors"] = validate_password(password1)

    return errors
