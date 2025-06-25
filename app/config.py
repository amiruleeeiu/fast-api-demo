from keycloak import KeycloakOpenID, KeycloakAdmin

KEYCLOAK_SERVER = "https://uat-beprc.oss.net.bd/idp/"
REALM_NAME = "BEPRC"
CLIENT_ID = "beprc-public"

# User-side Keycloak OpenID client
keycloak_openid = KeycloakOpenID(
    server_url=KEYCLOAK_SERVER,
    realm_name=REALM_NAME,
    client_id=CLIENT_ID,
)

# Admin client for user registration
keycloak_admin = KeycloakAdmin(
    server_url=KEYCLOAK_SERVER,
    username="admin",  # <- your admin username
    password="12345Q",
    realm_name="BEPRC",  # <- your target realm where user will be created
    user_realm_name="master",  # <- this is where the admin user exists
    client_id="admin-cli",     # <- this MUST be admin-cli
    verify=True
)
