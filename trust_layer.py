def unified_trust_layer(user, transaction):
    if not authenticate(user):
        return "Access Denied"
    
    if not kyc_verified(user):
        return "KYC Required"
    
    if fraud_detected(transaction):
        return "Transaction Blocked (Fraud)"
    
    return "Transaction Successful"


def authenticate(user):
    return user == "valid_user"

def kyc_verified(user):
    return True

def fraud_detected(transaction):
    return transaction > 100000  # simple rule
user = "valid_user"
transaction = 150000

result = unified_trust_layer(user,transaction)
print(result)