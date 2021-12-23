export function showError(element, message){
    let errorImg = '<img src="/static/admin/img/icon-no.svg" alt="error-img">'

    element.innerHTML = `<span class="error-message">${errorImg}${message}</span>`
}