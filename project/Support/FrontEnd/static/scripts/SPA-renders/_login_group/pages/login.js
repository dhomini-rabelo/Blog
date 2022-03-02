import { getCookie } from './../../../features/core/utils.js'


export let loginSPA = {
    group: 'login_group',
    individualStyles: [
        '/static/styles/apps/accounts/login_group/login.css',
    ],
    content: `
    <div class="form-group">
    <div class="field-group">
    <label for="id_email">Email:</label>
    <input type="text" name="email" id="id_email" placeholder="Digite seu email" inputmode="email">

    <div class="error"></div>
</div>

<div class="field-group">
    <label for="id_password">Senha:</label>
    <input type="password" name="password" id="id_password" placeholder="Digite sua senha">
    <div class="block-forgot-password"><a href="">Esqueceu a senha?</a></div>
    <div class="error"></div>
</div>

<input type="hidden" name="csrfmiddlewaretoken" value="${getCookie('csrftoken')}">
<button class="bl-wh" type="submit">LOGIN</button>
<div class="js-check">
<span><input type="checkbox" name="javascript" id="id_javascript" value="on" checked>Usar javascript para validação</span>
</div>            
</div>
<div class="shortcut center-r"><a href="{% url 'register' %}" class="link-login-group" destiny="register">Fazer cadastro</a>
</div>
    `,
    individualScripts: [
        ['/static/scripts/managers/apps/accounts/login_group/login.js', true],
    ]
}