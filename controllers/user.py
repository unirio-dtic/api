# -*- coding: utf-8 -*-
@auth.requires_login()
def index():
    apiKeysGrid = SQLFORM.grid(( db.api_auth.user_id == auth.user.id ),
                               fields=(db.api_auth.auth_key, db.api_auth.dt_creation, db.api_auth.active),
                               deletable=False,
                               create=False,
                               editable=False,
                               searchable=False,
                               maxtextlength=160,
                               csv=False)

    return dict(apiKeysGrid=apiKeysGrid)


@auth.requires_login()
def createKeyAuth():
    from APIKey import APIKey

    apiKey = APIKey()
    currentAPIKey = APIKey.getCurrentActiveKeyForUser(auth.user.id)

    # Se ainda não existir uma chave válida
    if not currentAPIKey:
        currentAPIKey = apiKey.genarateNewKeyForUser(auth.user.id)

    form = FORM(
        "Sua chave de API (API KEY) é: ",
        INPUT(_value=currentAPIKey, _name="apiKey", _size='600', _readonly=True),
        INPUT(_value="Gerar nova Chave", _type="submit")
    )

    if form.process().accepted:
        apiKey.genarateNewKeyForUser(auth.user.id)
        redirect(URL('user', 'index'), client_side=True)

    return dict(form=form)


def createKeyGuest():
    pass


# ===============================================================================
# Utilizado para gerar novas chaves para Sistemas
# TODO: melhorar a aparência desta porra porque está uma merda
#===============================================================================
@auth.requires(auth.has_membership('Desenvolvedor'))
def createNewSystemKey():
    key = ''

    # Retorna todos os usuários cadastrados como sistemas
    sistemas = db((db.auth_user.id == db.auth_membership.user_id)
                  & (db.auth_membership.group_id == 4)).select(db.auth_user.id, db.auth_user.first_name)

    form = FORM(
        SELECT([OPTION(sistema.first_name, _value=sistema.id) for sistema in sistemas], _name='user_id'),
        INPUT(_value="Gerar nova Chave", _type="submit")
    )
    if form.process().accepted:
        from APIKey import APIKey

        apiKey = APIKey()
        currentAPIKey = APIKey.getCurrentActiveKeyForUser(form.vars.user_id)

        #Se ainda não existir uma chave válida
        if not currentAPIKey:
            currentAPIKey = apiKey.genarateNewKeyForUser(form.vars.user_id)

        key = currentAPIKey

    return dict(form=form, key=key)


#===============================================================================
# Requer uma chave válida
#===============================================================================
def ldapLogin():
    from APIKey import APIKey
    from SIEUser import *

    response.view = 'generic.json'
    if APIKey.isValidKey(request.vars.API_KEY):
        user = auth.login_bare(request.vars.username, request.vars.password)
        if not user:
            return {'error': 'Usuário ou senha inválido.'}
        else:
            sieUser = SIEUser()
            return sieUser.pessoaForCPF(user)
    else:
        return {'error': 'Chave Inválida', 'request': request.vars}
