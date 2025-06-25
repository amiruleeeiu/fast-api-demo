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
    username="admin",
    password="admin",  # Keycloak admin
    realm_name="master",
    client_id="admin-cli",
    verify=True,
)
