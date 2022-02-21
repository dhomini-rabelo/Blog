export function fetchPost(url, data) {
    return fetch(url, {
        method: 'POST',
        ...data
    }).then(data => data.json())
}