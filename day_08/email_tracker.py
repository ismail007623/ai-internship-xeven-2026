valid_domains = {"gmail.com", "yahoo.com", "outlook.com", "hotmail.com"}
register_email = set()

def verify_email(email: str):
    """
    Docstring for verify_email
    
    :param email: Description
    :type email: str
    """

    try :
        user_name , domain = email.split('@')

        if '@' not in email :
            return "this is not valid email"

        if domain not in valid_domains :
            return f"this is not valid domain , valid domain  {valid_domains}"
        
        if email in register_email :
            return f"Email already exists {user_name}"

        register_email.add(email)
        return (f"User : {user_name} register sucessfully")

    except ValueError :
         print("Invalid format email must contain @")

def specific_domain(domain : str) -> set :
    """
    Docstring for specific_domain
    
    :param domain: Description
    :type domain: str
    :return: Description
    :rtype: set
    """

    return {email for email in register_email if email.endswith('@' + domain)}
    


print( verify_email('ismailgmail.com'))
print(verify_email('hassan@yahoo.com'))
print(verify_email('ali@gmail.com'))
print(verify_email('ismail@hotmail.com'))

specific_domain_user = specific_domain('gmail.com')

print(specific_domain_user)



