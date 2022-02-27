export let registerSPA = {
    group: 'login_group',
    individualStyles: [
        "/static/styles/apps/accounts/login_group/register.css",
    ],
    content: `
    <div class="form-group">
    <div class="field-group">
    <label for="id_name">Nome:</label>
    <input type="text" name="name" id="id_name" placeholder="Digite seu nome">
    <div class="error"></div>
</div>

<div class="field-group">
    <label for="id_email">Email:</label>
    <input type="text" name="email" id="id_email" placeholder="Digite seu email" inputmode="email">
    <div class="error"></div>
</div>

<div class="field-group">
    <label for="id_password">Senha:</label>
    <input type="password" name="password" id="id_password" placeholder="Digite sua senha">
    <div class="error"></div>
</div>

<div class="field-group">
    <label for="id_confirm_password">Confirmar senha:</label>
    <input type="password" name="confirm_password" id="id_confirm_password" placeholder="Confirme sua senha">
    <div class="error"></div>
</div>

<input type="hidden" name="csrfmiddlewaretoken" value="UPnZdhJKBYfG5RLOpyEIdrdQ4tZq5DbQqq0q7IirtwJ9XjxFm4Bhtg0siJp16yDO">
<button class="bl-wh" type="submit">CADASTRE-SE</button>
<div class="js-check">
<span><input type="checkbox" name="javascript" id="id_javascript" value="on" checked="">Usar javascript para validação</span>           
</div>
</div>
<div class="shortcut center-r"><a href="{% url 'login' %}" class="link-login-group" destiny="register">Fazer login</a>
</div>
    `,
    individualScripts: ['/static/scripts/managers/apps/accounts/login_group/register.js']
}